from rest_framework import generics, permissions
from .models import CareerPage,CareerSubmission
from .serializers import CareerPageSerializer
from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import JWTAuthentication
from django.core.mail import send_mail
from django.conf import settings
from .serializers import CareerSubmissionSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication


class CareerPageRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = CareerPage.objects.all()
    serializer_class = CareerPageSerializer
    def get_object(self):
        # Return the single CareerPage instance
        return CareerPage.objects.first()


class IsReadOnlyOrAuthenticated(permissions.BasePermission):
    """
    Custom permission to allow authenticated users to read (list) careers forms,
    but allow everyone to create new careers forms.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # Allow read access (GET, HEAD, OPTIONS) only to authenticated users
            return request.user and request.user.is_authenticated
        return True  # Allow all other methods (e.g., POST) for creating careers forms
    

class CareerSubmissionListCreateView(generics.ListCreateAPIView):
    queryset = CareerSubmission.objects.all().order_by('-submitted_at')
    serializer_class = CareerSubmissionSerializer
    permission_classes = [IsReadOnlyOrAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        # Save the new CareerSubmission instance
        instance = serializer.save()

        # Send an email to the admin
        subject = 'New career page Submission'
        message = f"Name: {instance.name}\nEmail: {instance.email}\nPhone: {instance.phone}\nMessage: {instance.message}\nResume: {instance.resume}\nSubmission Time: {instance.submitted_at}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['smtptest@pixelboho.com']  # Replace with the admin's email address
        send_mail(subject, message, from_email, recipient_list)
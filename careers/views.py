from rest_framework import generics, permissions
from .models import CareerPage,CareerSubmission ,MetaTagscareers
from .serializers import CareerPageSerializer
from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import JWTAuthentication
from django.core.mail import send_mail
from django.conf import settings
from .serializers import CareerSubmissionSerializer ,Careers_metadataSerializers
from rest_framework_simplejwt.authentication import JWTAuthentication

#views for careers
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
        recipient_list = ['smtp.office365.com']  # Replace with the admin's email address
        try:
            send_mail(subject, message, from_email, recipient_list)
        except Exception as e:
            # Handle email sending error
            print(f"Error sending email: {e}")
            # You can log the error or handle it in any appropriate way)

class CareersMetaListView(generics.ListAPIView):
    queryset = MetaTagscareers.objects.all()
    serializer_class = Careers_metadataSerializers

class CareersMetaRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MetaTagscareers.objects.all()
    serializer_class = Careers_metadataSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        # Since we want only one contactmeta data record, always retrieve the first one
        homemeta, created = MetaTagscareers.objects.get_or_create(pk=1)
        return homemeta
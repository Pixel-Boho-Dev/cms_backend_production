from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import ContactHeader, Section, ContactForm,MetaTagsContacts,FAQ
from .serializers import ContactHeaderSerializer, SectionSerializer, ContactFormSerializer,Contact_metadataSerializers,FAQSerializer
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.core.mail import send_mail
from django.conf import settings


#views for header and section of contacts
class HeaderRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = ContactHeader.objects.all()
    serializer_class = ContactHeaderSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    authentication_classes=[JWTAuthentication]

    def get_object(self):
        # Return the single header instance always
        return ContactHeader.objects.first()

class SectionRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    authentication_classes=[JWTAuthentication]

    def get_object(self):
        # Return the single Section instance always
        return Section.objects.first()

class IsReadOnlyOrAuthenticated(permissions.BasePermission):
    """
    Custom permission to allow authenticated users to read (list) contact forms,
    but allow everyone to create new contact forms.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # Allow read access (GET, HEAD, OPTIONS) only to authenticated users
            return request.user and request.user.is_authenticated
        return True  # Allow all other methods (e.g., POST) for creating contact forms
    
#views for contactform
class ContactFormListCreateView(generics.ListCreateAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer
    permission_classes=[IsReadOnlyOrAuthenticated]
    authentication_classes=[JWTAuthentication]
    def perform_create(self, serializer):
        # Save the new ContactForm instance
        instance = serializer.save()

        # Send an email to the admin
        subject = 'New Contact Form Submission'
        message = f"Name: {instance.name}\nEmail: {instance.email}\nPhone: {instance.phone}\nMessage: {instance.message}\nSubmission Time: {instance.timestamp}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['ajayrenjith03@gmail.com','bibinofficial3@gmail.com']  # Replace with the admin's email address later
        send_mail(subject, message, from_email, recipient_list)

class ContactFormRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_read = True  # mark as read 
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# views for contact page meta data
class ContactMetaListView(generics.ListAPIView):
    queryset = MetaTagsContacts.objects.all()
    serializer_class = Contact_metadataSerializers

class ContactMetaRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MetaTagsContacts.objects.all()
    serializer_class = Contact_metadataSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        # Since we want only one contactmeta data record, always retrieve the first one
        homemeta, created = MetaTagsContacts.objects.get_or_create(pk=1)
        return homemeta

# views for frequently asked questions
class FAQListCreateView(generics.ListCreateAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    authentication_classes=[JWTAuthentication]

class FAQRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    authentication_classes=[JWTAuthentication]
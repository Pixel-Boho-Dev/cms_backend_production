
from rest_framework import generics
from .models import Footer
from .serializers import FooterSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class FooterListCreate(generics.ListCreateAPIView):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer
    
class FooterRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


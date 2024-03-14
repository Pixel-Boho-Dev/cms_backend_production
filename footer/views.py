# views.py

from django.shortcuts import render

from rest_framework import generics
from .models import Footer
from .serializers import AppFooterSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class AppFooterListCreate(generics.ListCreateAPIView):
    queryset = Footer.objects.all()
    serializer_class = AppFooterSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class AppFooterRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Footer.objects.all()
    serializer_class = AppFooterSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


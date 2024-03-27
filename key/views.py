from django.shortcuts import render

from rest_framework import generics
from .models import key_diffrentiates
from .serializers import key_diffrentiatesSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class key_diffrentiatesListCreate(generics.ListCreateAPIView):
    queryset = key_diffrentiates.objects.all()
    serializer_class = key_diffrentiatesSerializer
    

class key_diffrentiatesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = key_diffrentiates.objects.all()
    serializer_class = key_diffrentiatesSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


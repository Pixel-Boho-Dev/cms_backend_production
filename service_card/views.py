from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import ServicesCard
from .serializers import ServicesCardSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class ServicesCardListCreateView(generics.ListCreateAPIView):
    queryset = ServicesCard.objects.all()
    serializer_class = ServicesCardSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class ServicesCardRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServicesCard.objects.all()
    serializer_class = ServicesCardSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
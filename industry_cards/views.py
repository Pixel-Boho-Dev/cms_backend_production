from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import IndustryCard,IndustryTitles
from .serializers import  IndustryCardSerializer,IndustryTitleSerializer


class IndustryCardListAPIView(generics.ListCreateAPIView):
    queryset = IndustryCard.objects.all()
    serializer_class = IndustryCardSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    


class IndustryCardDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IndustryCard.objects.all()
    serializer_class = IndustryCardSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class IndustryTitleListCreateAPIView(generics.ListCreateAPIView):
    queryset = IndustryTitles.objects.all()
    serializer_class = IndustryTitleSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
class IndustryTitleDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IndustryTitles.objects.all()
    serializer_class = IndustryTitleSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
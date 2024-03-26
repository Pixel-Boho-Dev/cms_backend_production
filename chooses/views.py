from django.shortcuts import render

# Create your views here.

#

from rest_framework import generics
from .models import ChoosesSection
from .serializers import ChoosesSectionSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework import status

class ChoosesSectionListCreateView(generics.ListCreateAPIView):
    queryset = ChoosesSection.objects.all()
    serializer_class = ChoosesSectionSerializer

class ChoosesSectionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChoosesSection.objects.all()
    serializer_class = ChoosesSectionSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

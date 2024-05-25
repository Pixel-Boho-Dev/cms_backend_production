from django.shortcuts import render
from rest_framework import generics
from .models import ChoosesSection
from .serializers import ChoosesSectionSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


#views for choose
class ChoosesSectionListCreateView(generics.ListCreateAPIView):
    queryset = ChoosesSection.objects.all()
    serializer_class = ChoosesSectionSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class ChoosesSectionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChoosesSection.objects.all()
    serializer_class = ChoosesSectionSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

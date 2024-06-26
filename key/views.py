from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import key_diffrentiates,key_diffrentiatesSection
from .serializers import key_diffrentiatesSerializer,key_diffrentiatesSectionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination

#views for keydiffrentiates
class NoPagination(PageNumberPagination):
    page_size = None
    
class key_diffrentiatesListCreate(generics.ListCreateAPIView):
    queryset = key_diffrentiates.objects.all()
    serializer_class = key_diffrentiatesSerializer
    pagination_class = NoPagination
    
class key_diffrentiatesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = key_diffrentiates.objects.all()
    serializer_class = key_diffrentiatesSerializer


#views for keydiffrentiates title
class key_diffrentiatesSectionListCreate(generics.ListCreateAPIView):
    queryset = key_diffrentiatesSection.objects.all()
    serializer_class = key_diffrentiatesSectionSerializer
 
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
class key_diffrentiatesSectionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = key_diffrentiatesSection.objects.all()
    serializer_class = key_diffrentiatesSectionSerializer
    
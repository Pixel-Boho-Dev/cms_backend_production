from django.shortcuts import render
from rest_framework import viewsets
from socialmedia.models import Service
from socialmedia.serializers import SubServiceSerializer,ServiceSubServiceSerializer
from .models import SubService,MetaTagsservices
from .serializers import Service_metadataSerializers
from socialmedia.serializers import ServiceSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from rest_framework import permissions


# Create your views here.
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    @action(detail=True, methods=['GET'])
    def subservices(self, request, pk=None):
        # Retrieve the Service object
        service = self.get_object()

        # Retrieve associated SubServices
        subservices = SubService.objects.filter(related_service=service)

        # Serialize the SubServices
        # Serialize the Service and SubServices together
        serializer = ServiceSubServiceSerializer({'service': service, 'subservices': subservices}, context={'request': request})

        return Response(serializer.data)
    
class SubServiceViewSet(viewsets.ModelViewSet):
    queryset = SubService.objects.all().order_by('-id')  # Order by '-id'
    serializer_class = SubServiceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]


class ServicesMetaListView(generics.ListAPIView):
    queryset = MetaTagsservices.objects.all().order_by('-id') 
    serializer_class = Service_metadataSerializers

class ServicesMetaRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = MetaTagsservices.objects.all().order_by('-id') 
    serializer_class = Service_metadataSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        # Since you want only one Homemeta data record, always retrieve the first one
        servicemeta, created = MetaTagsservices.objects.get_or_create(pk=1)
        return servicemeta
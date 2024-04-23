from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import status
from socialmedia.models import Service
from socialmedia.serializers import SubServiceSerializer,ServiceheadingSubServiceSerializer
from .models import SubService,MetaTagsservices,Subheading
from .serializers import Service_metadataSerializers, subheadingSerializers
from socialmedia.serializers import ServiceSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import JsonResponse
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

        # Retrieve the Subheadings related to the Service
        subheadings = Subheading.objects.filter(related_service=service)

        # Serialize the Service
        service_data = ServiceSerializer(service).data

        # Serialize the Subheadings and their associated SubServices
        subheadings_data = []
        for subheading in subheadings:
            subservices = SubService.objects.filter(related_heading=subheading)
            subservice_data = SubServiceSerializer(subservices, many=True).data
            subheading_data = {
                'id': subheading.id,
                'subheading': subheading.title,
                'subservices': subservice_data
            }
            subheadings_data.append(subheading_data)

        # Construct the response data
        response_data = {
            'service': service_data,
            'subheadings': subheadings_data
        }

        # Return the response
        return Response(response_data)


class SubheadingCreateView(generics.CreateAPIView):
    queryset = Subheading.objects.all()
    serializer_class = subheadingSerializers
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class SubheadingListView(generics.ListAPIView):
    queryset = Subheading.objects.all()
    serializer_class = subheadingSerializers

    def get(self, request):
        industries = Subheading.objects.all()
        serializer = subheadingSerializers(industries, many=True)
        return Response(serializer.data)
    

class SubheadingRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subheading.objects.all()
    serializer_class = subheadingSerializers

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
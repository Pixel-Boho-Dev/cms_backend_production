from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import status
from socialmedia.models import Service
from socialmedia.serializers import SubServiceSerializer,ServiceheadingSubServiceSerializer
from .models import SubService,MetaTagsservices,Subheading,SpecializedService,SpecializedSubService
from .serializers import Service_metadataSerializers, subheadingSerializers,SpecializedServiceSerializer,SpecializedSubServiceSerializer
from socialmedia.serializers import ServiceSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from rest_framework import permissions

#views for service full page
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
                'subheading': subheading.subheading,
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
    
    @action(detail=True, methods=['DELETE'])
    def delete_subservices(self, request, pk=None):
        service = self.get_object()
        subheadings = Subheading.objects.filter(related_service=service)
        
        for subheading in subheadings:
            SubService.objects.filter(related_heading=subheading).delete()
        subheadings.delete()

         # Delete the service itself
        service.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

#views for subheading
class SubheadingCreateView(generics.CreateAPIView):
    queryset = Subheading.objects.all()
    serializer_class = subheadingSerializers
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class SubheadingListView(generics.ListAPIView):
    queryset = Subheading.objects.all()
    serializer_class = subheadingSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        industries = Subheading.objects.all()
        serializer = subheadingSerializers(industries, many=True)
        return Response(serializer.data)
    
class SubheadingRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subheading.objects.all()
    serializer_class = subheadingSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

#views for subservice
class SubServiceViewSet(viewsets.ModelViewSet):
    queryset = SubService.objects.all().order_by('-id')  # Order by '-id'
    serializer_class = SubServiceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

#views for servicemeta
class ServiceMetaCreateView(generics.CreateAPIView):
    queryset = MetaTagsservices.objects.all()
    serializer_class = Service_metadataSerializers
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class ServicesMetaListView(generics.ListAPIView):
    queryset = MetaTagsservices.objects.all()
    serializer_class = Service_metadataSerializers

class ServicesMetaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MetaTagsservices.objects.all().order_by('-id') 
    serializer_class = Service_metadataSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        service_id = self.kwargs.get('pk')  # Get the service ID from URL
        try:
            servicemeta = MetaTagsservices.objects.get(pk=service_id)
            return servicemeta
        except MetaTagsservices.DoesNotExist:
            # If the service ID does not exist, return 404 Not Found
            return Response(status=status.HTTP_404_NOT_FOUND)

#views for specialized service
class SpecializedServiceListCreate(generics.ListCreateAPIView):
    queryset = SpecializedService.objects.all()
    serializer_class = SpecializedServiceSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
  
class SpecializedServiceRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = SpecializedService.objects.all()
    serializer_class = SpecializedServiceSerializer

#views for specialized subservice
class SpecializedSubServiceListCreate(generics.ListCreateAPIView):
    queryset = SpecializedSubService.objects.all()
    serializer_class = SpecializedSubServiceSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class SpecializedSubServiceRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = SpecializedSubService.objects.all()
    serializer_class = SpecializedSubServiceSerializer

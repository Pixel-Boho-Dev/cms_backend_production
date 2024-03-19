from rest_framework.response import Response
from django.http import Http404
from rest_framework import generics
from .models import Office,Location_page,MetaTagsLocation,office_location
from .serializers import OfficeSerializer,Location_pageSerializer,Location_metadataSerializers,Office_locationSerializers
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status

class OfficeListCreateView(generics.ListCreateAPIView):
    queryset = Office.objects.all().order_by('-id') 
    serializer_class = OfficeSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class OfficeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Office.objects.all().order_by('-id') 
    serializer_class = OfficeSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class OfficeListByLocationView(generics.ListAPIView):
    serializer_class = OfficeSerializer

    def get_queryset(self):
        location_id = self.kwargs['location_id']
        return Office.objects.filter(location_id=location_id)


class Location_pageCreateView(generics.CreateAPIView):
    queryset = Location_page.objects.all().order_by('-id') 
    serializer_class = Location_pageSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can create
    authentication_classes = [JWTAuthentication]
    
    def create(self, request, *args, **kwargs):
        # Check if any instances of Location_page exist, if yes, prevent creation
        if Location_page.objects.exists():
            return Response({"detail": "Location page already exists. Cannot create another."}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

class Location_pageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location_page.objects.all().order_by('-id') 
    serializer_class = Location_pageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def retrieve(self, request, *args, **kwargs):
        # Ensure that there's at least one Location_page object to retrieve
        if not Location_page.objects.exists():
            return Response({"detail": "Location page does not exist"}, status=status.HTTP_404_NOT_FOUND)

        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        # Ensure that there's at least one Location_page object to update
        if not Location_page.objects.exists():
            return Response({"detail": "Location page does not exist"}, status=status.HTTP_404_NOT_FOUND)

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

# views for locationpage meta data 

class LocationMetaListView(generics.ListAPIView):
    queryset = MetaTagsLocation.objects.all().order_by('-id') 
    serializer_class = Location_metadataSerializers

class LocationMetaRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = MetaTagsLocation.objects.all().order_by('-id') 
    serializer_class = Location_metadataSerializers
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        # Since you want only one Homemeta data record, always retrieve the first one
        locationmeta, created = MetaTagsLocation.objects.get_or_create(pk=1)
        return locationmeta

class Office_locationListCreateView(generics.ListCreateAPIView):
    queryset = office_location.objects.all().order_by('-id') 
    serializer_class = Office_locationSerializers
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class Office_locationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = office_location.objects.all().order_by('-id') 
    serializer_class = Office_locationSerializers
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    lookup_field = 'pk'


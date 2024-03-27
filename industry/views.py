from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import IndustriesPage,MetaTagsIndustries
from .serializers import IndustriesPageSerializer, Industries_metadataSerializers
from rest_framework_simplejwt.authentication import JWTAuthentication

class IndustriesPageListCreateView(generics.ListCreateAPIView):
    queryset = IndustriesPage.objects.all()
    serializer_class = IndustriesPageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]


    # def get_queryset(self):
    #     # Check if an instance already exists, and return it if found
    #     queryset = IndustriesPage.objects.all()
    #     if queryset.exists():
    #         return queryset

    #     # If no instance exists, return an empty queryset
    #     return IndustriesPage.objects.none()

    # def create(self, request, *args, **kwargs):
    #     # Check if an instance already exists
    #     if IndustriesPage.objects.exists():
    #         return Response(
    #             {"detail": "IndustriesPage already exists and cannot be created again."},
    #             status=status.HTTP_400_BAD_REQUEST
    #         )
        
    #     # If no instance exists, proceed with creation
    #     return super().create(request, *args, **kwargs)
    
class IndustriesPageRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IndustriesPage.objects.all()
    serializer_class = IndustriesPageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        # Retrieve the first (and only) instance of IndustriesPage
        return IndustriesPage.objects.first()

class IndustriesMetaListView(generics.ListAPIView):
    queryset = MetaTagsIndustries.objects.all()
    serializer_class = Industries_metadataSerializers
    

class IndustriesMetaRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = MetaTagsIndustries.objects.all()
    serializer_class = Industries_metadataSerializers
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        # Since you want only one Homemeta data record, always retrieve the first one
        industriesmeta, created = MetaTagsIndustries.objects.get_or_create(pk=1)
        return industriesmeta

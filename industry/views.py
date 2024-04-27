from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import IndustriesPage,MetaTagsIndustries
from .serializers import IndustriesPageSerializer, Industries_metadataSerializers
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404


class IndustriesPageListCreateView(generics.ListCreateAPIView):
    queryset = IndustriesPage.objects.all()
    serializer_class = IndustriesPageSerializer
    
class IndustriesPageRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IndustriesPage.objects.all()
    serializer_class = IndustriesPageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        # Retrieve the IndustriesPage instance by primary key (pk)
        pk = self.kwargs.get('pk')
        return get_object_or_404(IndustriesPage, pk=pk)
    

class IndustriesMetaListView(generics.ListAPIView):
    queryset = MetaTagsIndustries.objects.all()
    serializer_class = Industries_metadataSerializers
    

class IndustriesMetaRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MetaTagsIndustries.objects.all()
    serializer_class = Industries_metadataSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        # Since you want only one Homemeta data record, always retrieve the first one
        industriesmeta, created = MetaTagsIndustries.objects.get_or_create(pk=1)
        return industriesmeta

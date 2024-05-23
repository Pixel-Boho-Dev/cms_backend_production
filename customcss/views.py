from rest_framework import generics
from .models import HomeHeaderCustom,AboutPageSectionCustom
from .serializers import HomeHeaderCustomSerializer,AboutPageSectionCustomSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response

class HomeHeaderCustomListCreateView(generics.ListCreateAPIView):
    queryset = HomeHeaderCustom.objects.all()
    serializer_class = HomeHeaderCustomSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class HomeHeaderCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HomeHeaderCustom.objects.all()
    serializer_class = HomeHeaderCustomSerializer


#views for 

class AboutPageSectionCustomListCreateView(generics.ListCreateAPIView):
    queryset = AboutPageSectionCustom.objects.all()
    serializer_class = AboutPageSectionCustomSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class AboutPageSectionCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AboutPageSectionCustom.objects.all()
    serializer_class = AboutPageSectionCustomSerializer


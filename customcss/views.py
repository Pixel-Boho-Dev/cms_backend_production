from rest_framework import generics
from .models import HomeHeaderCustom,AboutPageSectionCustom,ourstoryCustom,milestoneCustom,ourteamCustom
from .serializers import HomeHeaderCustomSerializer,AboutPageSectionCustomSerializer,ourstoryCustomSerializer,milestoneCustomserializers,ourteamCustomserializers
from rest_framework.permissions import IsAuthenticated
from .models import HomeHeaderCustom,ServicecardsCustom
from .serializers import HomeHeaderCustomSerializer,ServicecardCustomSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response

#views s for headersection

class HomeHeaderCustomListCreateView(generics.ListCreateAPIView):
    queryset = HomeHeaderCustom.objects.all()
    serializer_class = HomeHeaderCustomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class HomeHeaderCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HomeHeaderCustom.objects.all()
    serializer_class = HomeHeaderCustomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]
    

#views for  aboupage section

class AboutPageSectionCustomListCreateView(generics.ListCreateAPIView):
    queryset = AboutPageSectionCustom.objects.all()
    serializer_class = AboutPageSectionCustomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]


class AboutPageSectionCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AboutPageSectionCustom.objects.all()
    serializer_class = AboutPageSectionCustomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]
    
    
    #views of service cards
class ServicecardCustomListCreateView(generics.ListCreateAPIView):
    queryset = ServicecardsCustom.objects.all()
    serializer_class = ServicecardCustomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
  
class ServiceRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServicecardsCustom.objects.all()
    serializer_class = ServicecardCustomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

#views for ourstory

class ourstoryCustomListCreateView(generics.ListCreateAPIView):
    queryset = ourstoryCustom.objects.all()
    serializer_class = ourstoryCustomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class ourstoryCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ourstoryCustom.objects.all()
    serializer_class = ourstoryCustomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

#views for milestones

class milestoneListCreateView(generics.ListCreateAPIView):
    queryset = milestoneCustom.objects.all()
    serializer_class = milestoneCustomserializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class milestoneCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = milestoneCustom.objects.all()
    serializer_class = milestoneCustomserializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

#views for ourteam

class ourteamCustomListCreateView(generics.ListCreateAPIView):
    queryset = ourteamCustom.objects.all()
    serializer_class = ourteamCustomserializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class ourteamCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ourteamCustom.objects.all()
    serializer_class = ourteamCustomserializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]





from rest_framework import generics
from .models import HomeHeaderCustom,ServicecardsCustom
from .serializers import HomeHeaderCustomSerializer,ServicecardCustomSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response

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


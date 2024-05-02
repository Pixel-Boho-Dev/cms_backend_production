from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import ServicesCard,ServiceTitle
from .serializers import ServicesCardSerializer,ServiceTitleSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class ServicesCardListCreateView(generics.ListCreateAPIView):
    queryset = ServicesCard.objects.all()
    serializer_class = ServicesCardSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class ServicesCardRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServicesCard.objects.all()
    serializer_class = ServicesCardSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class ServiceTitleListCreateView(generics.ListCreateAPIView):
    queryset = ServiceTitle.objects.all()
    serializer_class = ServiceTitleSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class ServiceTitleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceTitle.objects.all()
    serializer_class = ServiceTitleSerializer
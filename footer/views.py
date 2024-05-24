from rest_framework import generics
from .models import Footer
from .serializers import FooterSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response


class FooterListCreate(generics.ListCreateAPIView):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
class FooterRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


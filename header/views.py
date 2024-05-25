from rest_framework import generics, permissions
from .models import HomeHeader
from .serializers import HeaderSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

#views for header
class HeaderCreateView(generics.CreateAPIView):
    queryset = HomeHeader.objects.all()
    serializer_class = HeaderSerializer

class HeaderRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HomeHeader.objects.all()
    serializer_class = HeaderSerializer

    def get_object(self):
        # There should be only one instance of the Header model
        if HomeHeader.objects.exists():
            return HomeHeader.objects.first()
        else:
            return None

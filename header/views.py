from rest_framework import generics, permissions
from .models import HomeHeader
from .serializers import HeaderSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

class HeaderCreateView(generics.CreateAPIView):
    queryset = HomeHeader.objects.all()
    serializer_class = HeaderSerializer
   #only authenticated users can create a header for the home page

class HeaderRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HomeHeader.objects.all()
    serializer_class = HeaderSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes= [JWTAuthentication]

    def get_object(self):
        # There should be only one instance of the Header model
        if HomeHeader.objects.exists():
            return HomeHeader.objects.first()
        else:
            return None

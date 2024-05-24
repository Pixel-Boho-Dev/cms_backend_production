from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response

#views for headersection
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

#views for chooseUs
class ChooseusCustomListCreateView(generics.ListCreateAPIView):
    queryset = ChooseusCustom.objects.all()
    serializer_class = ChooseusCustomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class ChooseusCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChooseusCustom.objects.all()
    serializer_class = ChooseusCustomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

#views for ournetwork
class OurnetworkCustomListCreateView(generics.ListCreateAPIView):
    queryset = OurnetworkCustom.objects.all()
    serializer_class = OurnetworkCustomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class OurnetworkCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OurnetworkCustom.objects.all()
    serializer_class = OurnetworkCustomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

#views for keydiffrentiates
class KeydiffretiatesCustomListCreateView(generics.ListCreateAPIView):
    queryset = KeydiffrentiatorsCustom.objects.all()
    serializer_class = KeydiffrentiatorsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class KeydiffrentiatesCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = KeydiffrentiatorsCustom
    serializer_class = KeydiffrentiatorsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

#views for Acheievements
class AcheievmentCustomListCreateView(generics.ListCreateAPIView):
    queryset = AcheievementCustom.objects.all()
    serializer_class = AcheievementCustomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
class AcheievementCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset   = AcheievementCustom.objects.all()
    serializer_class = AcheievementCustomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication] 

#views for highlights
class HighlightsCustomListCreateView(generics.ListCreateAPIView):
    queryset = HighlightsCustom.objects.all()
    serializer_class = HighlightsCustomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
class HighlightsCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset   = HighlightsCustom.objects.all()
    serializer_class = HighlightsCustomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication] 

#views for industriescards
class IndustriesCardsCustomListCreateView(generics.ListCreateAPIView):
    queryset = IndustriesCardsCustom.objects.all()
    serializer_class = IndustriesCardsCustomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class IndustriesCardsCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset   = IndustriesCardsCustom.objects.all()
    serializer_class = IndustriesCardsCustomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication] 

#views for marketupdates
class MarketUpdatesCustomListCreateView(generics.ListCreateAPIView):
    queryset = MarketUpdatesCustom.objects.all()
    serializer_class = MarketUpdatesCustomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class MarketUpdatesCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset   = MarketUpdatesCustom.objects.all()
    serializer_class = MarketUpdatesCustomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication] 
    
#views for  aboupagesection
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

#views for whatweare

class whatweareCustomListCreateView(generics.ListCreateAPIView):
    queryset = whatweareCustom.objects.all()
    serializer_class = whatweareCustomserializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class whatweareCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = whatweareCustom.objects.all()
    serializer_class = whatweareCustomserializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

#views for certification

class certificationCustomListCreateView(generics.ListCreateAPIView):
    queryset = certificationCustom.objects.all()
    serializer_class = certificationCustomserializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class certificationCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = certificationCustom.objects.all()
    serializer_class = certificationCustomserializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

#views for contactform
class contactformCustomListCreateView(generics.ListCreateAPIView):
    queryset = contactformCustom.objects.all()
    serializer_class = contactformCustomserializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class contactformCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = contactformCustom.objects.all()
    serializer_class = contactformCustomserializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

#views for footer
class footerCustomCListCreateView(generics.ListCreateAPIView):
    queryset = footerCustom.objects.all()
    serializer_class = footerCustomserializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class footerCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = footerCustom.objects.all()
    serializer_class = footerCustomserializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

#views for headerournetwork

class headerournetworkCustomListCreateView(generics.ListCreateAPIView):
    queryset = headerournetworkCustom.objects.all()
    serializer_class = headerournetworkCustomserializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class headerournetworkCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = headerournetworkCustom.objects.all()
    serializer_class = headerournetworkCustomserializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]


#views for ournetwork description
class ournetworkdescriptioncustomListCreateView(generics.ListCreateAPIView):
    queryset = ournetworkdescriptionCustom.objects.all()
    serializer_class = ournetworkdescriptionCustomSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class ournetworkdescriptionCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ournetworkdescriptionCustom.objects.all()
    serializer_class = ournetworkdescriptionCustomSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

#views for service
class ServiceCustomListCreateView(generics.ListCreateAPIView):
    queryset = ServiceCustom.objects.all()
    serializer_class = ServiceCustomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
class ServiceCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceCustom.objects.all()
    serializer_class = ServiceCustomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]


#views for ournetwork location
class ournetworklocationcustomListCreateView(generics.ListCreateAPIView):
    queryset = ournetworklocationCustom.objects.all()
    serializer_class = ournetworklocationCustomSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class ournetworklocationCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ournetworklocationCustom.objects.all()
    serializer_class = ournetworklocationCustomSerializers
    permissionclasses = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

#views for ournetwork location
class ournetworkofficesCustomListCreateView(generics.ListCreateAPIView):
    queryset = ournetworkofficesCustom.objects.all()
    serializer_class = ournetworkofficesCustomSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class ournetworkofficesCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ournetworkofficesCustom.objects.all()
    serializer_class = ournetworkofficesCustomSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

#views for careerspage
class careerspageCustomListCreateView(generics.ListCreateAPIView):
    queryset = careerspageCustom.objects.all()
    serializer_class = careerspageCustomSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class careerspageCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = careerspageCustom.objects.all()
    serializer_class = careerspageCustomSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]






from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView



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
class OurstoryCustomListCreateView(generics.ListCreateAPIView):
    queryset = OurstoryCustom.objects.all()
    serializer_class = OurstoryCustomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class OurstoryCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OurstoryCustom.objects.all()
    serializer_class = OurstoryCustomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

#views for milestones
class MilestoneListCreateView(generics.ListCreateAPIView):
    queryset = MilestoneCustom.objects.all()
    serializer_class = MilestoneCustomserializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class MilestoneCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MilestoneCustom.objects.all()
    serializer_class = MilestoneCustomserializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

#views for ourteam
class OurteamCustomListCreateView(generics.ListCreateAPIView):
    queryset = OurteamCustom.objects.all()
    serializer_class = OurteamCustomserializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class OurteamCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OurteamCustom.objects.all()
    serializer_class = OurteamCustomserializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

#views for whatweare
class WhatweareCustomListCreateView(generics.ListCreateAPIView):
    queryset = WhatweareCustom.objects.all()
    serializer_class = WhatweareCustomserializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class WhatweareCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WhatweareCustom.objects.all()
    serializer_class = WhatweareCustomserializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

#views for certification
class CertificationCustomListCreateView(generics.ListCreateAPIView):
    queryset = CertificationCustom.objects.all()
    serializer_class = CertificationCustomserializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class CertificationCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CertificationCustom.objects.all()
    serializer_class = CertificationCustomserializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

#views for contactform
class ContactformCustomListCreateView(generics.ListCreateAPIView):
    queryset = ContactformCustom.objects.all()
    serializer_class = ContactformCustomserializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class ContactformCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactformCustom.objects.all()
    serializer_class = ContactformCustomserializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

#views for footer
class FooterCustomCListCreateView(generics.ListCreateAPIView):
    queryset = FooterCustom.objects.all()
    serializer_class = FooterCustomserializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class FooterCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FooterCustom.objects.all()
    serializer_class = FooterCustomserializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

#views for headerournetwork
class HeaderournetworkCustomListCreateView(generics.ListCreateAPIView):
    queryset = HeaderournetworkCustom.objects.all()
    serializer_class = HeaderournetworkCustomserializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class HeaderournetworkCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HeaderournetworkCustom.objects.all()
    serializer_class = HeaderournetworkCustomserializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]


#views for ournetwork description
class OurnetworkdescriptioncustomListCreateView(generics.ListCreateAPIView):
    queryset = OurnetworkdescriptionCustom.objects.all()
    serializer_class = OurnetworkdescriptionCustomSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class OurnetworkdescriptionCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OurnetworkdescriptionCustom.objects.all()
    serializer_class = OurnetworkdescriptionCustomSerializers
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
class OurnetworklocationcustomListCreateView(generics.ListCreateAPIView):
    queryset = OurnetworklocationCustom.objects.all()
    serializer_class = OurnetworklocationCustomSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class OurnetworklocationCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OurnetworklocationCustom.objects.all()
    serializer_class = OurnetworklocationCustomSerializers
    permissionclasses = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

#views for ournetwork location
class OurnetworkofficesCustomListCreateView(generics.ListCreateAPIView):
    queryset = OurnetworkofficesCustom.objects.all()
    serializer_class = OurnetworkofficesCustomSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class OurnetworkofficesCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OurnetworkofficesCustom.objects.all()
    serializer_class = OurnetworkofficesCustomSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

#views for careerspage
class CareerspageCustomListCreateView(generics.ListCreateAPIView):
    queryset = CareerspageCustom.objects.all()
    serializer_class = CareerspageCustomSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class CareerspageCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CareerspageCustom.objects.all()
    serializer_class = CareerspageCustomSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]


#views for headermarketupdatescustom

class headermarketupdatescustomListCreateView(generics.ListCreateAPIView):
    queryset = headermarketupdatescustom.objects.all()
    serializer_class = headermarketupdatescustomserializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class headermarketupdatescustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = headermarketupdatescustom.objects.all()
    serializer_class = headermarketupdatescustomserializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]


#views for marketcustom

class marketcustomListCreateView(generics.ListCreateAPIView):
    queryset = marketcustom.objects.all()
    serializer_class = marketscustomserializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class marketscustomserializersRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = marketcustom.objects.all()
    serializer_class = marketscustomserializers
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]


#views for industries page
class IndustriesHeaderCustomListCreateView(generics.ListCreateAPIView):
    queryset = IndustriesHeaderCustom.objects.all()
    serializer_class = IndustriesHeaderCustomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
class IndustriesHeaderCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IndustriesHeaderCustom.objects.all()
    serializer_class = IndustriesHeaderCustomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

#views for industriesBlocks
class IndustriesBlockCustomListCreateView(generics.ListCreateAPIView):
    queryset = IndustriesBlocksCustom.objects.all()
    serializer_class = IndustriesBlockCustomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

class IndustriesBlockCustomRetrieveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IndustriesBlocksCustom.objects.all()
    serializer_class = IndustriesBlockCustomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

class IndustriesHeaderCustomViewSet(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def get(self, request, pk=None):
        # Retrieve the IndustriesHeaderCustom object
        header = IndustriesHeaderCustom.objects.get(pk=pk)

        # Serialize the header
        header_data = IndustriesHeaderCustomSerializer(header).data

        # Retrieve related blocks
        blocks = IndustriesBlocksCustom.objects.filter(header=header)
        blocks_data = IndustriesBlockCustomSerializer(blocks, many=True).data

        # Combine data
        response_data = {
            'header': header_data,
            'blocks': blocks_data
        }

        return Response(response_data)
    
    def delete(self, request, pk=None):
        try:
            # Retrieve the IndustriesHeaderCustom object
            header = IndustriesHeaderCustom.objects.get(pk=pk)
        except IndustriesHeaderCustom.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        # Retrieve related blocks
        blocks = IndustriesBlocksCustom.objects.filter(header=header)
        
        # Delete related blocks
        blocks.delete()
        
        # Delete the IndustriesHeaderCustom object
        header.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)


    
 

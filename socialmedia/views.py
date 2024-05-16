from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import SocialMedia,Service,Location,HomeHighlights,Industry,Market,Achievement,MetaTagsHome,AchievementSection,HighlightsSection,MarketTitle,OurNetworkTitle
from .serializers import SocialMediaSerializer,ServiceSerializer,LocationSerializer,HighlightSerializer,IndustrySerializer,MarketSerializer,AchievementSerializer,MetaTagsHomeSerializer,AchievementSectionSerializer,HighlightsSectionSerializer,MarketTitleSerializer,ServiceheaderSerializer,OurNetworkTitleSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication

class SocialMediaCreateView(generics.CreateAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can create
    authentication_classes = [JWTAuthentication]

class SocialMediaListView(generics.ListAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer

class SocialMediaRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can update and delete
    authentication_classes = [JWTAuthentication]


# views for services
class ServiceCreateView(generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceheaderSerializer
    pagination_class = PageNumberPagination

class ServiceRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceheaderSerializer
    

# views for locations
class LocationCreateView(generics.CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class LocationListView(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    pagination_class = None

class LocationRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

#views for ournetwork
class OurNetworkTitleCreateView(generics.CreateAPIView):
    queryset = OurNetworkTitle.objects.all()
    serializer_class = OurNetworkTitleSerializer

class OurNetworkTitleListView(generics.ListAPIView):
    queryset = OurNetworkTitle.objects.all()
    serializer_class = OurNetworkTitleSerializer

class OurNetworkTitleRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OurNetworkTitle.objects.all()
    serializer_class = OurNetworkTitleSerializer
    
# views for achievements
class AchievementCreateView(generics.CreateAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class AchievementListView(generics.ListAPIView):
    queryset = Achievement.objects.all().order_by('-id')
    serializer_class = AchievementSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class AchievementRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
class AchievementSectionListCreate(generics.ListCreateAPIView):
    queryset = AchievementSection.objects.all()
    serializer_class = AchievementSectionSerializer


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
class AchievementSectionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = AchievementSection.objects.all()
    serializer_class = AchievementSectionSerializer
    
    
# views for highlights
class HighlightCreateView(generics.CreateAPIView):
    queryset = HomeHighlights.objects.all()
    serializer_class = HighlightSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class HighlightListView(generics.ListAPIView):
    queryset = HomeHighlights.objects.all()
    serializer_class = HighlightSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
class HighlightRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HomeHighlights.objects.all()
    serializer_class = HighlightSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

class HighlightSectionListCreate(generics.ListCreateAPIView):
    queryset = HighlightsSection.objects.all()
    serializer_class = HighlightsSectionSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class HighlightSectionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = HighlightsSection.objects.all()
    serializer_class = HighlightsSectionSerializer

# views for Industries
class IndustryCreateView(generics.CreateAPIView):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class IndustryListView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        industries = Industry.objects.all()
        serializer = IndustrySerializer(industries, many=True)
        return Response(serializer.data)

class IndustryUpdateView(generics.UpdateAPIView):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]
    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# views for market news
class MarketCreateView(generics.CreateAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class MarketListView(generics.ListAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class MarketRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

#views for market title
class MarketTitleCreateView(generics.CreateAPIView):
    queryset = MarketTitle.objects.all()
    serializer_class = MarketTitleSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class MarketTitleListView(generics.ListAPIView):
    queryset = MarketTitle.objects.all()
    serializer_class = MarketTitleSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
class MarketTitleRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MarketTitle.objects.all()
    serializer_class = MarketTitleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]


# # views for home details
# class HomeListView(generics.ListAPIView):
#     queryset = Home.objects.all()
#     serializer_class = HomeSerializer

# class HomeRetrieveUpdateView(generics.RetrieveUpdateAPIView):
#     queryset = Home.objects.all()
#     serializer_class = HomeSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     authentication_classes = [JWTAuthentication]

#     def get_object(self):
#         # Since you want only one Home record, always retrieve the first one
#         home, created = Home.objects.get_or_create(pk=1)
#         return home

# views for home meta tags    
class HomeMetaListView(generics.ListAPIView):
    queryset = MetaTagsHome.objects.all()
    serializer_class = MetaTagsHomeSerializer

class HomeMetaRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MetaTagsHome.objects.all()
    serializer_class = MetaTagsHomeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        # Since you want only one Homemeta data record, always retrieve the first one
        homemeta, created = MetaTagsHome.objects.get_or_create(pk=1)
        return homemeta
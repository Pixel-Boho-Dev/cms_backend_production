from rest_framework import generics
from .models import AboutPageSection,OurStory,Milestone,OurTeam,WhatWeAre,Certifications,MetaTagsAbout
from .serializers import AboutPageSectionSerializer,OurStorySerializer,MilestoneSerializer,OurTeamSerializer,WhatWeAreSerializer,CertificationSerializer,About_metadataSerializers
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions


# view for creating about page section.
class AboutPageSectionListCreateView(generics.ListCreateAPIView):
    queryset = AboutPageSection.objects.all()
    serializer_class = AboutPageSectionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

# update a specif section with the help of pk
class AboutPageSectionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AboutPageSection.objects.all()
    serializer_class = AboutPageSectionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]


# views for ourstory
class OurStoryCreateView(generics.CreateAPIView):
    queryset = OurStory.objects.all()
    serializer_class = OurStorySerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get_object(self):
        # There should be only one instance of the OurStory model
        if OurStory.objects.exists():
            return OurStory.objects.first()
        else:
            return None

# views for updating and for unauthenticated users to see our story
class OurStoryRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OurStorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        # There should be only one instance of the OurStory model
        if OurStory.objects.exists():
            return OurStory.objects.first()
        else:
            return None
        
# views for milestones
class MilestoneCreateView(generics.CreateAPIView,generics.ListAPIView):
    queryset = Milestone.objects.all()
    serializer_class = MilestoneSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

class MilestoneRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Milestone.objects.all()
    serializer_class = MilestoneSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

# views for our team
class OurTeamCreateView(generics.CreateAPIView):
    queryset = OurTeam.objects.all()
    serializer_class = OurTeamSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class OurTeamRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OurTeam.objects.all()
    serializer_class = OurTeamSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    lookup_field = 'pk'  # This tells DRF to use 'pk' as the lookup field.

class OurTeamListView(generics.ListAPIView):
    queryset = OurTeam.objects.all().order_by('-id')
    serializer_class = OurTeamSerializer

# views for what we are
class WhatWeAreCreateView(generics.CreateAPIView):
    queryset = WhatWeAre.objects.all()
    serializer_class = WhatWeAreSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class WhatWeAreRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WhatWeAre.objects.all()
    serializer_class = WhatWeAreSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    lookup_field = 'pk'  # This tells DRF to use 'pk' as the lookup field.

class WhatWeAreListView(generics.ListAPIView):
    queryset = WhatWeAre.objects.all().order_by('-id')
    serializer_class = WhatWeAreSerializer

# views for certifications
class CertificationCreateView(generics.CreateAPIView):
    queryset=Certifications.objects.all()
    serializer_class=CertificationSerializer
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class CertificationRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Certifications.objects.all()
    serializer_class=CertificationSerializer
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    lookup_field = 'pk'


class CertificatioListView(generics.ListAPIView):
    queryset = Certifications.objects.all().order_by('-id')
    serializer_class = CertificationSerializer


class AboutMetaListView(generics.ListAPIView):
    queryset = MetaTagsAbout.objects.all()
    serializer_class = About_metadataSerializers

class AboutMetaRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = MetaTagsAbout.objects.all()
    serializer_class = About_metadataSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        # Since we want only one Aboutmeta data record, always retrieve the first one
        aboutmeta, created = MetaTagsAbout.objects.get_or_create(pk=1)
        return aboutmeta
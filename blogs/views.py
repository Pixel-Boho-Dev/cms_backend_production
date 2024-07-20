import logging
from rest_framework import permissions, viewsets ,generics
from rest_framework.pagination import PageNumberPagination  # Import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import BlogPost, MetaTagsBlogs
from .serializers import BlogPostSerializer, Blogs_metadataSerializers
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all().order_by('id')
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]
    pagination_class = None  # Disable pagination for this viewset

    def get_object(self):
        queryset = self.get_queryset()
        slug = self.kwargs.get("slug")
        obj = queryset.filter(slug=slug).first()
        self.check_object_permissions(self.request, obj)
        return obj

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# Views for BlogMeta
class BlogMetaCreateView(generics.CreateAPIView):
    queryset = MetaTagsBlogs.objects.all()
    serializer_class = Blogs_metadataSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

class BlogMetaListView(generics.ListAPIView):
    queryset = MetaTagsBlogs.objects.all()
    serializer_class = Blogs_metadataSerializers

class BlogMetaRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MetaTagsBlogs.objects.all()
    serializer_class = Blogs_metadataSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

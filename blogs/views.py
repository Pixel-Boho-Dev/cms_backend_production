import logging
from rest_framework import permissions, generics, viewsets
from .models import BlogPost, MetaTagsBlogs
from .serializers import BlogPostSerializer, Blogs_metadataSerializers
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions,generics
from rest_framework import viewsets

logger = logging.getLogger(__name__)

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all().order_by('id')
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]
    pagination_class = None  # Ensure pagination is disabled

    def list(self, request, *args, **kwargs):
        logger.debug(f"Pagination class: {self.pagination_class}")
        response = super().list(request, *args, **kwargs)
        logger.debug(f"Response data: {response.data}")
        return response

    def get_object(self):
        queryset = self.get_queryset()
        slug = self.kwargs.get("slug")
        obj = queryset.filter(slug=slug).first()
        self.check_object_permissions(self.request, obj)
        return obj

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


#views for blogmeta
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


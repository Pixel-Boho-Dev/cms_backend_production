import logging
from rest_framework import permissions, viewsets, generics
from rest_framework.pagination import PageNumberPagination
from .models import BlogPost, MetaTagsBlogs
from .serializers import BlogPostSerializer, Blogs_metadataSerializers
from rest_framework_simplejwt.authentication import JWTAuthentication

logger = logging.getLogger(__name__)

class BlogPostPagination(PageNumberPagination):
    page_size = 50  # Number of blog posts per page

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all().order_by('id')
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]
    pagination_class = BlogPostPagination

    def list(self, request, *args, **kwargs):
        # Check for query parameter to disable pagination
        if request.query_params.get('paginate', 'true') == 'false':
            self.pagination_class = None
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

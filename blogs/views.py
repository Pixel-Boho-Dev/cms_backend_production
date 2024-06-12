from rest_framework import permissions,generics
from rest_framework import viewsets
from .models import BlogPost, MetaTagsBlogs
from .serializers import BlogPostSerializer, Blogs_metadataSerializers
from rest_framework_simplejwt.authentication import JWTAuthentication

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all().order_by('id')
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        queryset = self.get_queryset()
        slug = self.kwargs.get("slug")
        obj = queryset.filter(slug=slug).first()
        self.check_object_permissions(self.request, obj)
        return obj

    def perform_create(self, serializer):
        # Associate the logged-in user with the new blog post
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


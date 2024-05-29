from rest_framework import permissions,generics
from rest_framework import viewsets
from .models import BlogPost, Highlight, MetaTagsBlogs
from .serializers import BlogPostSerializer, HighlightSerializer, Blogs_metadataSerializers
from rest_framework_simplejwt.authentication import JWTAuthentication

#views for blogpost
class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all().order_by('-id')
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        # Associate the logged-in user with the new blog post
        serializer.save(author=self.request.user)

#views for highlightviewset
class HighlightViewSet(viewsets.ModelViewSet):
    queryset = Highlight.objects.all().order_by('-id')
    serializer_class = HighlightSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

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

    def get_object(self):
        # Since we want only one Homemeta data record, always retrieve the first one
        homemeta, created = MetaTagsBlogs.objects.get_or_create(blog_post_id=1)
        return homemeta
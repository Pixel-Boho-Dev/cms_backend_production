from rest_framework import serializers
from .models import BlogPost, MetaTagsBlogs

#serializers for blogpost
class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'

#serializers for blogmetadata
class Blogs_metadataSerializers(serializers.ModelSerializer):
    class Meta:
        model   =   MetaTagsBlogs
        fields  =   '__all__'


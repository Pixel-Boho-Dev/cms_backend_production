from rest_framework import serializers
from .models import BlogPost, Highlight,MetaTagsBlogs



class HighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Highlight
        fields = '__all__'
        ref_name = 'unique_ref_name_for_this_serializer'

class BlogPostSerializer(serializers.ModelSerializer):
    highlights = HighlightSerializer(many=True, read_only=True)

    class Meta:
        model = BlogPost
        fields = '__all__'


class Blogs_metadataSerializers(serializers.ModelSerializer):
    class Meta:
        model   =   MetaTagsBlogs
        fields  =   '__all__'


from rest_framework import serializers
from .models import BlogPost, BlogImage, Highlight, Quote,MetaTagsBlogs


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogImage
        fields = '__all__'

class HighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Highlight
        fields = '__all__'
        ref_name = 'unique_ref_name_for_this_serializer'

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'

class BlogPostSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    highlights = HighlightSerializer(many=True, read_only=True)
    quotes = QuoteSerializer(many=True, read_only=True)

    class Meta:
        model = BlogPost
        fields = '__all__'


class Blogs_metadataSerializers(serializers.ModelSerializer):
    class Meta:
        model   =   MetaTagsBlogs
        fields  =   '__all__'


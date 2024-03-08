from django.contrib import admin
from .models import BlogPost, BlogImage, Highlight, Quote, MetaTagsBlogs

class ImageInline(admin.TabularInline):
    model = BlogImage
    extra = 1

class HighlightInline(admin.TabularInline):
    model = Highlight
    extra = 1

class QuoteInline(admin.TabularInline):
    model = Quote
    extra = 1

class MetaTagsBlogsInline(admin.StackedInline):
    model = MetaTagsBlogs
    extra = 1 
    
class BlogPostAdmin(admin.ModelAdmin):
    inlines = [ImageInline, HighlightInline, QuoteInline, MetaTagsBlogsInline]

admin.site.register(BlogPost, BlogPostAdmin)

from django.contrib import admin
from .models import BlogPost, Highlight,  MetaTagsBlogs


class HighlightInline(admin.TabularInline):
    model = Highlight
    extra = 1

class MetaTagsBlogsInline(admin.StackedInline):
    model = MetaTagsBlogs
    extra = 1 
    
class BlogPostAdmin(admin.ModelAdmin):
    inlines = [HighlightInline, MetaTagsBlogsInline]

admin.site.register(BlogPost, BlogPostAdmin)

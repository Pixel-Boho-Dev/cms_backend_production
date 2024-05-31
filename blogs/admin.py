from django.contrib import admin
from .models import BlogPost, MetaTagsBlogs



class MetaTagsBlogsInline(admin.StackedInline):
    model = MetaTagsBlogs
    extra = 1 
    
class BlogPostAdmin(admin.ModelAdmin):
    inlines = [ MetaTagsBlogsInline]

admin.site.register(BlogPost, BlogPostAdmin)

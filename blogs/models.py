from django.db import models

class BlogPost(models.Model):
    header_image = models.ImageField(upload_to='blog_headers/')
    header_title = models.CharField(max_length=255)
    publish_date = models.DateTimeField()
    description = models.TextField()    
    author = models.CharField(max_length=50,null=True,blank=True)
 # atlernative tags for header_image -->Arya
    alt_img_text = models.TextField(max_length=300, null=True, blank=True)
    alt_img_title = models.TextField(max_length=300, null=True, blank=True)
    alt_img_Caption = models.TextField(max_length=300, null=True, blank=True)
    alt_img_description = models.TextField(max_length=300, null=True, blank=True)
  # atlernative content for header_image -->Arya


    def __str__(self):
        return self.header_title

# for adding multiple images for a single blog post
class BlogImage(models.Model):
    blog_post = models.ForeignKey(BlogPost, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(blank=True,null=True,upload_to='blog_images/')
    # atlernative content for image
    alt_img_text = models.TextField(max_length=300, null=True, blank=True)
    alt_img_title = models.TextField(max_length=300, null=True, blank=True)
    alt_img_Caption = models.TextField(max_length=300, null=True, blank=True)
    alt_img_description = models.TextField(max_length=300, null=True, blank=True)
    # atlernative content for image 

    def __str__(self):
        return f"Image for {self.blog_post.header_title}"

# adding highlights for a blog post
class Highlight(models.Model):
    blog_post = models.ForeignKey(BlogPost, related_name='highlights', on_delete=models.CASCADE)
    text = models.TextField(blank=True,null=True)

    def __str__(self):
        return f"Highlight for {self.blog_post.header_title}"

# for adding quotes for a blog
class Quote(models.Model):
    blog_post = models.ForeignKey(BlogPost, related_name='quotes', on_delete=models.CASCADE)
    text = models.TextField(blank=True,null=True)

    def __str__(self):
        return f"Quote for {self.blog_post.header_title}"

# adding meta tags for blog page
class MetaTagsBlogs(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='meta_tags')
    charset = models.CharField(max_length=150,null=True,blank=True)
    viewport = models.CharField(max_length=150,null=True,blank=True)
    title = models.CharField(max_length=150,null=True,blank=True)
    description = models.CharField(max_length=150,null=True,blank=True)
    keywords = models.CharField(max_length=150,null=True,blank=True)
    author = models.CharField(max_length=150,null=True,blank=True)
    robots = models.CharField(max_length=150,null=True,blank=True)
    copyright = models.CharField(max_length=150,null=True,blank=True)
    referrer = models.CharField(max_length=150,null=True,blank=True)
    og_title = models.CharField(max_length=150,null=True,blank=True)
    og_type = models.CharField(max_length=150,null=True,blank=True)
    og_url = models.CharField(max_length=150,null=True,blank=True)
    og_image = models.ImageField(upload_to='meta_tags_blogs/', null=True, blank=True)
    og_description = models.CharField(max_length=150,null=True,blank=True)
    og_site_name = models.CharField(max_length=150,null=True,blank=True)
    og_locale = models.CharField(max_length=150,null=True,blank=True)
    twitter_card = models.CharField(max_length=150,null=True,blank=True)
    twitter_site = models.CharField(max_length=150,null=True,blank=True)
    twitter_title = models.CharField(max_length=150,null=True,blank=True)
    twitter_description = models.CharField(max_length=150,null=True,blank=True)
    twitter_image = models.ImageField(upload_to='meta_tags_blogs/', null=True, blank=True)
    twitter_image_alt = models.CharField(max_length=150,null=True,blank=True)
    
    def __str__(self):
        return self.title


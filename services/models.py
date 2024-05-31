from django.db import models
from socialmedia.models import Service

#model for subheading
class Subheading(models.Model):
    subheading = models.CharField(max_length=200)
    related_service = models.ForeignKey(Service, on_delete=models.CASCADE)    

    def __str__(self):
        return self.title

#model for subservice
class SubService(models.Model):
    image = models.ImageField(upload_to='subservice_images/')
    sub_title = models.CharField(max_length=200)
 # atlernative content for bg_image
    alt_img_text = models.TextField(max_length=300, null=True,blank=True)
    alt_img_title = models.TextField(max_length=300, null=True,blank=True)
    alt_img_Caption = models.TextField(max_length=300,null=True,blank=True)
    alt_img_description = models.TextField(max_length=300,null=True,blank=True)
    related_heading = models.ForeignKey(Subheading, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.sub_title

#model for servicemeta
class MetaTagsservices(models.Model):
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
    og_image = models.ImageField(upload_to='meta_tags_services/', null=True, blank=True)
    og_description = models.CharField(max_length=150,null=True,blank=True)
    og_site_name = models.CharField(max_length=150,null=True,blank=True)
    og_locale = models.CharField(max_length=150,null=True,blank=True)
    twitter_card = models.CharField(max_length=150,null=True,blank=True)
    twitter_site = models.CharField(max_length=150,null=True,blank=True)
    twitter_title = models.CharField(max_length=150,null=True,blank=True)
    twitter_description = models.CharField(max_length=150,null=True,blank=True)
    twitter_image = models.ImageField(upload_to='meta_tags_services/', null=True, blank=True)
    twitter_image_alt = models.CharField(max_length=150,null=True,blank=True)


    def __str__(self):
        return self.title

#model for specialized service
class SpecializedService(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='specializedservice_images/')
    alt_img_text = models.TextField(max_length=300, null=True,blank=True)
    alt_img_title = models.TextField(max_length=300, null=True,blank=True)
    alt_img_Caption = models.TextField(max_length=300,null=True,blank=True)
    alt_img_description = models.TextField(max_length=300,null=True,blank=True)
    link = models.URLField(max_length=1000)

    def __str__(self):
        return self.title

#model for specialized subservice
class SpecializedSubService(models.Model):
    description = models.CharField(max_length=200)
    title = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(upload_to='specializedsubservice_images/',null=True,blank=True)
    alt_img_text = models.TextField(max_length=300, null=True,blank=True)
    alt_img_title = models.TextField(max_length=300, null=True,blank=True)
    alt_img_Caption = models.TextField(max_length=300,null=True,blank=True)
    alt_img_description = models.TextField(max_length=300,null=True,blank=True)

    def __str__(self):
        return self.title
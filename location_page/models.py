from django.db import models
from socialmedia.models import Location

# Create your models here.
# Model for location page

class Office(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    place_name = models.CharField(max_length=100)
    office_address = models.CharField(max_length=100)
    phone_number1 = models.CharField(max_length=20)
    phone_number2 = models.CharField(max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()
    country_manager_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    country_manager_phone1 = models.CharField(max_length=20)
    country_manager_phone2 = models.CharField(max_length=20, blank=True, null=True)
    country_manager_email = models.EmailField()
    is_head_office = models.BooleanField(default=False)
    office_url = models.URLField()
    office_desccription = models.TextField()

    def __str__(self):
        return f"Office at {self.location.place_name}"

class office_location(models.Model):
    country_name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
     
    def __str__(self):
        return self.country_name
# class Location_page(models.Model):
#     Location_header_image=models.ImageField(upload_to='Location_header_image/')
#     location_title=models.CharField(max_length=100)
#     location_subtitle=models.TextField()
#     location_description=models.TextField()
#
#     def __str__(self):
#         return self.location_title


class Location_page(models.Model):
    Location_header_image = models.ImageField(upload_to='Location_header_image/')
    location_title = models.CharField(max_length=100)
    location_subtitle = models.TextField()
    location_description = models.TextField()
  # atlernative content for Location_header_image -->Arya
    # alt_img_text = models.TextField(max_length=300, null=True, blank=True)
    # alt_img_title = models.TextField(max_length=300, null=True, blank=True)
    # alt_img_Caption = models.TextField(max_length=300, null=True, blank=True)
    # alt_img_description = models.TextField(max_length=300, null=True, blank=True)
 # atlernative content for Location_header_image -->Arya

    def __str__(self):
        return self.location_title

    def __str__(self):
        return self.location_title


# model for Location page meta data

class MetaTagsLocation(models.Model):
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
    og_image = models.ImageField(upload_to='meta_tags_location/', null=True, blank=True)
    og_description = models.CharField(max_length=150,null=True,blank=True)
    og_site_name = models.CharField(max_length=150,null=True,blank=True)
    og_locale = models.CharField(max_length=150,null=True,blank=True)
    twitter_card = models.CharField(max_length=150,null=True,blank=True)
    twitter_site = models.CharField(max_length=150,null=True,blank=True)
    twitter_title = models.CharField(max_length=150,null=True,blank=True)
    twitter_description = models.CharField(max_length=150,null=True,blank=True)
    twitter_image = models.ImageField(upload_to='meta_tags_location/', null=True, blank=True)
    twitter_image_alt = models.CharField(max_length=150,null=True,blank=True)


    def __str__(self):
        return self.title

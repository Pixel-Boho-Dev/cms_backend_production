from django.db import models


class SocialMedia(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(max_length=1000)
    icon = models.ImageField(upload_to='socialmedia_icons/')  # Assuming icons are represented as image
 # atlernative content for image -->krishna
    alt_img_text = models.TextField(max_length=300, null=True, blank=True)
    alt_img_title = models.TextField(max_length=300, null=True, blank=True)
    alt_img_Caption = models.TextField(max_length=300, null=True, blank=True)
    alt_img_description = models.TextField(max_length=300, null=True, blank=True)
 # atlernative content for image -->krishna

    def __str__(self):
        return self.name


# model for services
class Service(models.Model):
    icon = models.ImageField(upload_to='service_icons/')  # Assuming icons are represented as image
 # atlernative content for bg_image
    alt_img_text = models.TextField(max_length=300, null=True, blank=True)
    alt_img_title = models.TextField(max_length=300, null=True, blank=True)
    alt_img_Caption = models.TextField(max_length=300, null=True, blank=True)
    alt_img_description = models.TextField(max_length=300, null=True, blank=True)
 # atlernative content for bg_image
    title = models.CharField(max_length=100)
    subtitle = models.TextField()
    description = models.TextField(blank=True, null=True)
    link = models.URLField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


# model for locations

class Location(models.Model):
    location_url = models.URLField()
    place_name = models.CharField(max_length=100)
    phone_number1 = models.CharField(max_length=20)
    phone_number2 = models.CharField(max_length=20, blank=True, null=True)  # Optional field
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.place_name


# model for achievements

class Achievement(models.Model):
    achievements_icon = models.ImageField(upload_to='achievements_icons/')
 # atlernative content for image
    alt_img_text = models.TextField(max_length=300, null=True, blank=True)
    alt_img_title = models.TextField(max_length=300, null=True, blank=True)
    alt_img_Caption = models.TextField(max_length=300, null=True, blank=True)
    alt_img_description = models.TextField(max_length=300, null=True, blank=True)
 # atlernative content for image 
    achievements_title = models.CharField(max_length=100)
    achievements_description = models.TextField()

    def __str__(self):
        return self.achievements_title


# model for highlights

class HomeHighlights(models.Model):
    icon = models.ImageField(upload_to='HomeHighlights/')
    title = models.CharField(max_length=100)
   #  highlights_title = models.CharField(max_length=100)
   #  highlights_description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.highlights_title


# model for industries

class Industry(models.Model):
    industry_image = models.ImageField(upload_to='industry_images/')
 # atlernative content for image
    alt_img_text = models.TextField(max_length=300, null=True, blank=True)
    alt_img_title = models.TextField(max_length=300, null=True, blank=True)
    alt_img_Caption = models.TextField(max_length=300, null=True, blank=True)
    alt_img_description = models.TextField(max_length=300, null=True, blank=True)
 # atlernative content for image
    industry_title = models.CharField(max_length=100)
    industry_description = models.TextField()

    def __str__(self):
        return self.industry_title


# models for Market News
class Market(models.Model):
    market_image = models.ImageField(upload_to='market_images/')
 # atlernative content forimage -->krishna
    alt_img_text = models.TextField(max_length=300, null=True, blank=True)
    alt_img_title = models.TextField(max_length=300, null=True, blank=True)
    alt_img_Caption = models.TextField(max_length=300, null=True, blank=True)
    alt_img_description = models.TextField(max_length=300, null=True, blank=True)
 # atlernative content for image -->krishna
    market_title = models.CharField(max_length=100)
    market_description = models.TextField()

    def __str__(self):
        return self.market_title


# models for Home titles and descriptions
class Home(models.Model):
    service_main_title = models.CharField(max_length=100)
    service_main_description = models.TextField()
    features_main_title = models.CharField(max_length=100)
    features_main_description = models.TextField()
    highlights_main_title = models.CharField(max_length=100)
    highlights_main_description = models.TextField()
    industries_main_title = models.CharField(max_length=100)
    industries_main_description = models.TextField()
    markets_main_title = models.CharField(max_length=100)
    markets_main_description = models.TextField()

    def __str__(self):
        return "Home Data"

# Meta tags for homepage
class MetaTagsHome(models.Model):
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
    og_image = models.ImageField(upload_to='meta_tags_home/', null=True, blank=True)
    og_description = models.CharField(max_length=150,null=True,blank=True)
    og_site_name = models.CharField(max_length=150,null=True,blank=True)
    og_locale = models.CharField(max_length=150,null=True,blank=True)
    twitter_card = models.CharField(max_length=150,null=True,blank=True)
    twitter_site = models.CharField(max_length=150,null=True,blank=True)
    twitter_title = models.CharField(max_length=150,null=True,blank=True)
    twitter_description = models.CharField(max_length=150,null=True,blank=True)
    twitter_image = models.ImageField(upload_to='meta_tags_home/', null=True, blank=True)
    twitter_image_alt = models.CharField(max_length=150,null=True,blank=True)

    def __str__(self):
        return self.title
    

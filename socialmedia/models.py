from django.db import models
from django.utils.text import slugify

#model for socialmedia
class SocialMedia(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(max_length=1000)
    icon = models.ImageField(upload_to='socialmedia_icons/')  # Assuming icons are represented as image
 # atlernative content for image -->krishna
    alt_img_text = models.TextField(max_length=300, null=True, blank=True)
    alt_img_title = models.TextField(max_length=300, null=True, blank=True)
    alt_img_Caption = models.TextField(max_length=300, null=True, blank=True)
    alt_img_description = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name


# model for services
class Service(models.Model):
    image = models.ImageField(upload_to='service_images/')  # Assuming icons are represented as image
 # atlernative content for bg_image
    alt_img_text = models.TextField(max_length=300, null=True, blank=True)
    alt_img_title = models.TextField(max_length=300, null=True, blank=True)
    alt_img_Caption = models.TextField(max_length=300, null=True, blank=True)
    alt_img_description = models.TextField(max_length=300, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    slug = models.CharField(max_length=300, unique=True, blank=True, null=True)
    is_specialized = models.BooleanField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug or Service.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            self.slug = self._generate_unique_slug()
        super().save(*args, **kwargs)

    def _generate_unique_slug(self):
        base_slug = slugify(self.title) if self.title else "service"
        slug = base_slug
        counter = 1
        while Service.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        return slug

    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        return f"/service/{self.slug}/"

# model for locations
class Location(models.Model):
    
   #  location_url = models.URLField()
    place_name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    location_url = models.URLField() 
   #  description = models.TextField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.place_name

#models for ournetwork title
class OurNetworkTitle(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

# model for achievements
class Achievement(models.Model):
    achievements_icon = models.ImageField(upload_to='achievements_icons/')
    achievements_subtitle = models.TextField()
 # atlernative content for image
    alt_img_text = models.TextField(max_length=300, null=True, blank=True)
    alt_img_title = models.TextField(max_length=300, null=True, blank=True)
    alt_img_Caption = models.TextField(max_length=300, null=True, blank=True)
    alt_img_description = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.achievements_subtitle
    
#models for acheievement title
class AchievementSection(models.Model):
    title = models.TextField()
    def __str__(self):
        return self.title

# model for highlights
class HomeHighlights(models.Model):
   icon = models.ImageField(upload_to='homehighlights/')
   sub_title = models.CharField(max_length=200)

   def __str__(self):
        return self.sub_title

#models for highlightstitle
class HighlightsSection(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


# model for industries
class Industry(models.Model):
    industry_image = models.ImageField(upload_to='industry_images/')
 # atlernative content for image
    alt_img_text = models.TextField(max_length=300, null=True, blank=True)
    alt_img_title = models.TextField(max_length=300, null=True, blank=True)
    alt_img_Caption = models.TextField(max_length=300, null=True, blank=True)
    alt_img_description = models.TextField(max_length=300, null=True, blank=True)
    industry_title = models.CharField(max_length=100)
    industry_description = models.TextField()
    slug = models.CharField(max_length=300, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug or Industry.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            self.slug = self._generate_unique_slug()
        super().save(*args, **kwargs)

    def _generate_unique_slug(self):
        base_slug = slugify(self.industry_title ) if self.industry_title  else "industry header"
        slug = base_slug
        counter = 1
        while Industry.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        return slug

    def __str__(self):
        return self.industry_title 

    def get_absolute_url(self):
        return f"/about/{self.slug}/"
    
# models for Market header
class Market(models.Model):
    market_image = models.ImageField(upload_to='market_images/')
 # atlernative content forimage -->krishna
    alt_img_text = models.TextField(max_length=300, null=True, blank=True)
    alt_img_title = models.TextField(max_length=300, null=True, blank=True)
    alt_img_Caption = models.TextField(max_length=300, null=True, blank=True)
    alt_img_description = models.TextField(max_length=300, null=True, blank=True)
    market_title = models.CharField(max_length=100)
    slug = models.CharField(max_length=500, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug or Market.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            self.slug = self._generate_unique_slug()
        super().save(*args, **kwargs)

    def _generate_unique_slug(self):
        base_slug = slugify(self.market_title) if self.market_title else "market"
        slug = base_slug
        counter = 1
        while Market.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        return slug

    def __str__(self):
        return self.market_title 

    def get_absolute_url(self):
        return f"/market/{self.slug}/"

#models for market title
class MarketTitle(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title


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
    

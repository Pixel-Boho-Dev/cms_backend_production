# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator
from django.db.models.signals import pre_save
from django.utils.text import slugify
from urllib.parse import urlparse
import re

#models for about us page
class AboutPageSection(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    sub_title = models.CharField(max_length=200, null=True, blank=True)
    bg_image = models.ImageField(upload_to='about_page_images/', blank=True, null=True)
    slug = models.CharField(max_length=200, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug or AboutPageSection.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            self.slug = self._generate_unique_slug()
        super().save(*args, **kwargs)

    def _generate_unique_slug(self):
        base_slug = slugify(self.title) if self.title else "about-page-section"
        slug = base_slug
        counter = 1
        while AboutPageSection.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        return slug

    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        return f"/about/{self.slug}/"

#models for ourstory 
class OurStory(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='our_story_images/')
 # atlernative tags for image 
    alt_img_text = models.TextField(max_length=300, null=True, blank=True)
    alt_img_title = models.TextField(max_length=300, null=True, blank=True)
    alt_img_Caption = models.TextField(max_length=300, null=True, blank=True)
    alt_img_description = models.TextField(max_length=300, null=True, blank=True)
 
    def __str__(self):
        return self.title   
    
#model for ourstorytitle
class OurstoryTitle(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

# model for storing milestones 
class Milestone(models.Model):
    year = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    achievements= models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.year} - {self.title}"
    
#model for milestonetitle
class MilestoneTitle(models.Model):
    title = models.TextField()
    sub_title = models.TextField()

    def __str__(self):
        return self.title

# model for storing ourTeam
class OurTeam(models.Model):
    profile_pic = models.ImageField(upload_to='our_team/',null=True, blank=True)
    title_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    order_by = models.IntegerField(validators=[MinValueValidator(0)], unique=True)
 # atlernative tags for team profile_pic
    alt_img_text = models.TextField(max_length=300, null=True, blank=True)
    alt_img_title = models.TextField(max_length=300, null=True, blank=True)
    alt_img_Caption = models.TextField(max_length=300, null=True, blank=True)
    alt_img_description = models.TextField(max_length=300, null=True, blank=True) 

    def __str__(self):
        return self.title_name

#model for ourteamtitle    
class OurTeamTitle(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

# Model for mission, vision and purpose
class WhatWeAre(models.Model):
    icon = models.ImageField(upload_to='whatweare/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    # atlernative tags for icon
    alt_img_text = models.TextField(max_length=300, null=True, blank=True)
    alt_img_title = models.TextField(max_length=300, null=True, blank=True)
    alt_img_Caption = models.TextField(max_length=300, null=True, blank=True)
    alt_img_description = models.TextField(max_length=300, null=True, blank=True)    

    def __str__(self):
        return self.title
    
#models for whatweare
class WhatWeAreTitle(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

# models for saving certificates
class Certifications(models.Model):
    certificate_image = models.ImageField(upload_to='certifications/')
    # atlernative content for certificate_image
    alt_img_text = models.TextField(max_length=300, null=True, blank=True)
    alt_img_title = models.TextField(max_length=300, null=True, blank=True)
    alt_img_Caption = models.TextField(max_length=300, null=True, blank=True)
    alt_img_description = models.TextField(max_length=300, null=True, blank=True)

 #model for certificatetitle
class CertificateTitle(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

# Meta tags for about us page.
class MetaTagsAbout(models.Model):
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
    og_image = models.ImageField(upload_to='meta_tags_about/', null=True, blank=True)
    og_description = models.CharField(max_length=150,null=True,blank=True)
    og_site_name = models.CharField(max_length=150,null=True,blank=True)
    og_locale = models.CharField(max_length=150,null=True,blank=True)
    twitter_card = models.CharField(max_length=150,null=True,blank=True)
    twitter_site = models.CharField(max_length=150,null=True,blank=True)
    twitter_title = models.CharField(max_length=150,null=True,blank=True)
    twitter_description = models.CharField(max_length=150,null=True,blank=True)
    twitter_image = models.ImageField(upload_to='meta_tags_about/', null=True, blank=True)
    twitter_image_alt = models.CharField(max_length=150,null=True,blank=True)
    
    def __str__(self):
        return self.title
    
    


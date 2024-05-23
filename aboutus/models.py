# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator

# Model for about page header sections
class AboutPageSection(models.Model):
    title = models.CharField(max_length=255,null=True, blank=True)
    sub_title = models.CharField(max_length=200,null=True,blank=True)
    bg_image = models.ImageField(upload_to='about_page_images/',blank=True,null=True)

    def __str__(self):
        return self.title


# model to store OurStory
class OurStory(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='our_story_images/')
 # atlernative tags for image 
    alt_img_text = models.TextField(max_length=300, null=True, blank=True)
    alt_img_title = models.TextField(max_length=300, null=True, blank=True)
    alt_img_Caption = models.TextField(max_length=300, null=True, blank=True)
    alt_img_description = models.TextField(max_length=300, null=True, blank=True)
 # atlernative tags for image 
    def __str__(self):
        return self.title   

class OurstoryTitle(models.Model):
    # Fields specific to titles
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


# model for storing milestones 
class Milestone(models.Model):
    year = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    achievement1 = models.TextField(null=True, blank=True)
    achievement2 = models.TextField(null=True, blank=True)
    achievement3 = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.year} - {self.title}"

class MilestoneTitle(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

# model for storing ourTeam
class OurTeam(models.Model):
    # team_title = models.CharField(max_length=100)
    # team_description = models.CharField(max_length=1000)
    profile_pic = models.ImageField(upload_to='our_team/',)
    title_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    order_by = models.IntegerField(validators=[MinValueValidator(0)], unique=True)
 # atlernative tags for team profile_pic
    alt_img_text = models.TextField(max_length=300, null=True, blank=True)
    alt_img_title = models.TextField(max_length=300, null=True, blank=True)
    alt_img_Caption = models.TextField(max_length=300, null=True, blank=True)
    alt_img_description = models.TextField(max_length=300, null=True, blank=True)
 # atlernative tags for profile_pic 

    def __str__(self):
        return self.name
    

class OurTeamTitle(models.Model):
    # Fields specific to titles
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

# Model for storing mission, vision and purpose
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

    # def clean(self):
    #     # Check the number of existing instances
    #     existing_instances = WhatWeAre.objects.count()
    #     if existing_instances >= 3:
    #         raise ValidationError("You can't create more than 3 instances of WhatWeAre.")

# models for saving certificates
class Certifications(models.Model):
    certificate_image = models.ImageField(upload_to='certifications/')
    # description = models.TextField()
    # atlernative content for certificate_image
    alt_img_text = models.TextField(max_length=300, null=True, blank=True)
    alt_img_title = models.TextField(max_length=300, null=True, blank=True)
    alt_img_Caption = models.TextField(max_length=300, null=True, blank=True)
    alt_img_description = models.TextField(max_length=300, null=True, blank=True)
    # atlernative content for certificate_image

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
    
class WhatWeAreTitle(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    


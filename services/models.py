from django.db import models
from socialmedia.models import Service
from django.utils.text import slugify


#model for subheading
class Subheading(models.Model):
    subheading = models.CharField(max_length=200)
    related_service = models.ForeignKey(Service, on_delete=models.CASCADE)    

    def __str__(self):
        return self.subheading

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
    title = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='specializedservice_images/')
    alt_img_text = models.TextField(max_length=300, null=True,blank=True)
    alt_img_title = models.TextField(max_length=300, null=True,blank=True)
    alt_img_Caption = models.TextField(max_length=300,null=True,blank=True)
    alt_img_description = models.TextField(max_length=300,null=True,blank=True)
    link = models.URLField(max_length=1000)

    def __str__(self):
        return self.title

#models for spcializedsubservice
class SpecializedSubService(models.Model):
    header_title = models.TextField()
    header_image = models.ImageField(upload_to='specializedsubservice-header_images/')
    description = models.TextField()
    subheading = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='specializedsubservice_images/', null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    alt_img_text = models.TextField(max_length=300, null=True, blank=True)
    alt_img_title = models.TextField(max_length=300, null=True, blank=True)
    alt_img_Caption = models.TextField(max_length=300, null=True, blank=True)
    alt_img_description = models.TextField(max_length=300, null=True, blank=True)
    slug = models.CharField(max_length=200, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug or SpecializedSubService.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            self.slug = self._generate_unique_slug()
        super().save(*args, **kwargs)

    def _generate_unique_slug(self):
        base_slug = slugify(self.header_title.split(':')[0]) if self.header_title else "specialized-subservice-page"
        slug = base_slug
        counter = 1
        while SpecializedSubService.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        return slug

    def get_absolute_url(self):
        return f"/specialized_service/{self.slug}/"

    def __str__(self):
        return self.header_title

#models for categories
class Categories(models.Model):
    title = models.TextField()
    image = models.ImageField(upload_to='categories_images/')
    slug = models.CharField(max_length=200, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug or Categories.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            self.slug = self._generate_unique_slug()
        super().save(*args, **kwargs)

    def _generate_unique_slug(self):
        base_slug = slugify(self.title.split(':')[0]) if self.title else "categories"
        slug = base_slug
        counter = 1
        while Categories.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        return slug

    def get_absolute_url(self):
        return f"/categories/{self.slug}/"

    def __str__(self):
        return self.title

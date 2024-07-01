from django.db import models
from socialmedia.models import Location
from django.core.validators import RegexValidator
from django.utils.text import slugify


#models for office
class Office(models.Model): 
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    place_name = models.TextField()
    office_address = models.TextField()
    fax = models.CharField(max_length=30, blank=True, null=True)  # Changed null=False to null=True
    email = models.EmailField()
    country_manager_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    phone_regex = RegexValidator(
        regex=r'^\+?[1-9]\d{1,14}(?:[-\s]?\d{1,13})*$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed, spaces and hyphens are allowed."
    )
    country_manager_phone1 = models.CharField(validators=[phone_regex], max_length=50)
    country_manager_phone2 = models.CharField(validators=[phone_regex], max_length=50, blank=True, null=True)
    is_head_office = models.BooleanField(default=False)
    office_url = models.URLField()

    def __str__(self):
        return f"Office at {self.location.place_name}"

#models for location_page
class Location_page(models.Model):
    Location_header_image = models.ImageField(upload_to='Location_header_image/')
    location_title = models.CharField(max_length=100)
    location_subtitle = models.TextField()
    location_description = models.TextField()
  # atlernative content for Location_header_image 
    alt_img_text = models.TextField(max_length=300, null=True, blank=True)
    alt_img_title = models.TextField(max_length=300, null=True, blank=True)
    alt_img_Caption = models.TextField(max_length=300, null=True, blank=True)
    alt_img_description = models.TextField(max_length=300, null=True, blank=True)
    slug = models.CharField(max_length=200, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug or Location_page.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            self.slug = self._generate_unique_slug()
        super().save(*args, **kwargs)

    def _generate_unique_slug(self):
        base_slug = slugify(self.location_title) if self.location_title else "location-page"
        slug = base_slug
        counter = 1
        while Location_page.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        return slug

    def __str__(self):
        return self.location_title

    def get_absolute_url(self):
        return f"/location/{self.slug}/"


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

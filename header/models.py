import re
from django.db import models
from django.utils.text import slugify
from urllib.parse import urlparse

def generate_valid_slug(value):
    """
    Generate a valid slug from the given value.
    """
    # Remove any characters that are not letters, numbers, underscores, slashes, or hyphens
    value = re.sub(r'[^\w/-]', '-', value.lower())
    # Replace multiple hyphens or underscores with a single hyphen
    value = re.sub(r'[-\s]+', '-', value).strip('-')
    return value

class HomeHeader(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='header_images/')
    url = models.URLField()
    alt_img_text = models.TextField(max_length=300, null=True, blank=True)
    alt_img_title = models.TextField(max_length=300, null=True, blank=True)
    alt_img_Caption = models.TextField(max_length=300, null=True, blank=True)
    alt_img_description = models.TextField(max_length=300, null=True, blank=True)
    
    def __str__(self):
        return self.title



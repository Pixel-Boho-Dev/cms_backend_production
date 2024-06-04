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
    slug = models.CharField(max_length=200, unique=True, blank=True, null=True)  # This field stores only the slug

    def save(self, *args, **kwargs):
        # Use the provided slug, if available and valid
        if self.slug:
            # Extract the path component from the provided URL
            parsed_url = urlparse(self.slug)
            path = parsed_url.path
            # Modify the slug to include only the path component
            self.slug = path

        # If no slug is provided, generate slug based on the title
        if not self.slug:
            self.slug = generate_valid_slug(self.title)

        # Ensure the slug is unique
        self.slug = self._generate_unique_slug(self.slug)

        super().save(*args, **kwargs)

    def _generate_unique_slug(self, base_slug):
        slug = base_slug
        counter = 1
        while HomeHeader.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        return slug
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Return the complete URL including the base URL
        return f"https://example.com/home/{self.slug}/"

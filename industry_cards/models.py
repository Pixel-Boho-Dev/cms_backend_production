# models.py
from django.db import models



class IndustryCard(models.Model):
    title = models.CharField(max_length=100)
    description =models. TextField()
    image = models.ImageField(upload_to='industry_images/')
    alt_img_text = models.TextField(max_length=300, null=True, blank=True)
    alt_img_title = models.TextField(max_length=300, null=True, blank=True)
    alt_img_caption = models.TextField(max_length=300, null=True, blank=True)
    alt_img_description = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f"{self.title.title} - {self.subtitle}"
    



class IndustryTitles(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

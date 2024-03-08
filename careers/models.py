# models.py
from django.db import models


class CareerPage(models.Model):
    header_image = models.ImageField(upload_to='career_page')
    description = models.TextField()

class CareerSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    resume = models.FileField(upload_to='resumes')
    submitted_at = models.DateTimeField(auto_now_add=True)
class Meta:
    app_label = 'careers'


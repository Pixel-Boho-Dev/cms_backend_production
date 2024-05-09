from django.db import models

# Create your models here.

class ChoosesSection(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField()
    bg_image = models.ImageField(upload_to='Chooses_Section/')

    def __str__(self):
        return self.title

from django.db import models

#models for chooses
class ChoosesSection(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField()
    bg_image = models.ImageField(upload_to='Chooses_Section/')

    def __str__(self):
        return self.title

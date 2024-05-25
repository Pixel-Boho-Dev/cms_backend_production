from django.db import models

#models for servicecard
class ServicesCard(models.Model):
    title = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='Services_Card/')
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title

#models for servicetitle
class ServiceTitle(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

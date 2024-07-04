from django.db import models
from django.core.validators import MinValueValidator


#models for servicecard
class ServicesCard(models.Model):
    title = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='Services_Card/')
    description = models.CharField(max_length=500)
    link = models.URLField(max_length=1000)
    order_by = models.IntegerField(validators=[MinValueValidator(0)], unique=True)


    def __str__(self):
        return self.title

#models for servicetitle
class ServiceTitle(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

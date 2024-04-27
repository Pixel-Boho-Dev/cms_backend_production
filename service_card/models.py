from django.db import models

# Create your models here.
from django.db import models

class ServicesCard(models.Model):
    icon = models.ImageField(upload_to='Services_Card/')
    description = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Services_Card/')
    description = models.TextField()

    def __str__(self):
        return self.description
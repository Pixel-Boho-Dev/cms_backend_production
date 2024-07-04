from django.db import models
from django.core.validators import MinValueValidator


#models for key diffrentiates
class key_diffrentiates(models.Model):
    icon = models.ImageField(upload_to='key_diffrentiates/')
    tagline = models.TextField()
    order_by = models.IntegerField(validators=[MinValueValidator(0)], unique=True)


    def __str__(self):
        return str(self.id)  
    
#models for keydiffrentiates title
class key_diffrentiatesSection(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.TextField()

    def __str__(self):
        return self.title  
from django.db import models

class Footer(models.Model):
    icon = models.ImageField(upload_to='AppFooter/')
    location = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number1 = models.CharField(max_length=20)
    phone_number2 = models.CharField(max_length=20)


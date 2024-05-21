from django.db import models

class Footer(models.Model):
    title = models.CharField(max_length=300, blank=True, null=True)
    # location = models.CharField(max_length=300, blank=True, null=True)
    address = models.CharField(max_length=1000, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number1 = models.CharField(max_length=20, blank=True, null=True)
    phone_number2 = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.title
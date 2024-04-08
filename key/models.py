from django.db import models

class key_diffrentiates(models.Model):
    icon = models.ImageField(upload_to='key_diffrentiates/')
    tagline = models.TextField()

    def __str__(self):
        return str(self.id)  # Return an appropriate representation for the model

class key_diffrentiatesSection(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)

    def __str__(self):
        return self.title  # Return an appropriate representation for the model

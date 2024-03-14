from django.db import models

# from django.db import models

class key_diffrentiates(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='key_diffrentiates/')
    tagline = models.TextField()

    def __str__(self):
        return self.title



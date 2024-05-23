from django.db import models

class HomeHeaderCustom(models.Model):
    title = models.TextField()
    image = models.ImageField(upload_to="Customcss_home")
    sub_title = models.TextField()
    description = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.title

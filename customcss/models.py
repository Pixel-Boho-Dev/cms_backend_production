from django.db import models

class HomeHeaderCustom(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.title

class AboutPageSectionCustom(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.title

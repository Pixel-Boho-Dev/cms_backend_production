from django.db import models

# models for homeheader

class HomeHeaderCustom(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.title
    
#models fo aboutpagesection

class AboutPageSectionCustom(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.title

#models fo ourstorysection

class ourstoryCustom(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.title



class ServicecardsCustom(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


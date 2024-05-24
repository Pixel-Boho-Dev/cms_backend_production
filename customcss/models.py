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

#models for servicecard

class ServicecardsCustom(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text
    
#models for milestone
  
class milestoneCustom(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text

#models for ournetwork

class ournetworkCustom(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text


    


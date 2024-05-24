from django.db import models

# models for homeheader
class HomeHeaderCustom(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text
    
#models for servicecard
class ServicecardsCustom(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text
    
#models for chooseus
class ChooseusCustom(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text
    
#models fo aboutpagesection
class AboutPageSectionCustom(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

#models fo ourstorysection
class ourstoryCustom(models.Model):
    text = models.TextField()
    def __str__(self):
        return self.text

    def __str__(self):
        return self.text
    
#models for milestone
class milestoneCustom(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text

#models for ourteam
class ourteamCustom(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text

#models for whatweare
class whatweareCustom(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text


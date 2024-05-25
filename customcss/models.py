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

#models for ournetwork
class OurnetworkCustom(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text
    
#models for key diffrentiators
class KeydiffrentiatorsCustom(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text
    
#models for acheievements
class AcheievementCustom(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text
    
#models for highlights
class HighlightsCustom(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text
    
#models for industriescards
class IndustriesCardsCustom(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text
    
#models for marketupdates
class MarketUpdatesCustom(models.Model):
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

#models for certification
class certificationCustom(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text
    
#class for contactform
class contactformCustom(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text
    
#models for footer
class footerCustom(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text
    
#models for header ournetwork
class headerournetworkCustom(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text
    

#models for ournetwork description
class ournetworkdescriptionCustom(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text
    
#models for service
class ServiceCustom(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text

#models for ournetworklocation

class ournetworklocationCustom(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text
    
#models for ournetworkoffices

class ournetworkofficesCustom(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text
    
#models for careerspage

class careerspageCustom(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text
    

#models for heademarketupdate

# class headermarketupdatescustom(models.Model):
#     header_css = models.TextField()

#     def __str__(self):
#         return self.header_css
    
# #models for marketcustom
    
# class marketcustom(models.Model):
#     markets_css = models.TextField()
    
#     def __str__(self):
#         return self.markets_css
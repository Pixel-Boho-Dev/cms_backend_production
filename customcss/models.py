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
class OurstoryCustom(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text
    
#models for milestone
class MilestoneCustom(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text

#models for ourteam
class OurteamCustom(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text

#models for whatweare
class WhatweareCustom(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text

#models for certification
class CertificationCustom(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text
    
#class for contactform
class ContactformCustom(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text
    
#models for footer
class FooterCustom(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text
    
#models for header ournetwork
class HeaderournetworkCustom(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text
    

#models for ournetwork description
class OurnetworkdescriptionCustom(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text
    
#models for service
class ServiceCustom(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text

#models for ournetworklocation
class OurnetworklocationCustom(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text
    
#models for ournetworkoffices
class OurnetworkofficesCustom(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text
    

#models for careerspage
class CareerspageCustom(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text

#models for indutries header
class IndustriesHeaderCustom(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text
    
#models for industries blocks
class IndustriesBlocksCustom(models.Model):
    header = models.ForeignKey(IndustriesHeaderCustom, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content
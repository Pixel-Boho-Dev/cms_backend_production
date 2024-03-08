from django.db import models

# Header of the home page
class HomeHeader(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='header_images/')
    alt_img_text = models.TextField(max_length=300, null=True, blank=True)
    alt_img_title = models.TextField(max_length=300, null=True, blank=True)
    alt_img_Caption = models.TextField(max_length=300, null=True, blank=True)
    alt_img_description = models.TextField(max_length=300, null=True, blank=True)

    def save(self, *args, **kwargs):
        #to Ensure there is only one instance of the Header model
        if not self.pk and HomeHeader.objects.exists():
            existing_header = HomeHeader.objects.first()
            existing_header.title = self.title
            existing_header.subtitle = self.subtitle
            existing_header.description = self.description
            existing_header.image = self.image
        # atlernative save content for image 
            existing_header.alt_img_text = self.alt_img_text
            existing_header.alt_img_title = self.alt_img_title
            existing_header.alt_img_Caption = self.alt_img_Caption
            existing_header.alt_img_description = self.alt_img_description
         # atlernative save content for image 
            existing_header.save()
            return existing_header
        return super(HomeHeader, self).save(*args, **kwargs)


    def __str__(self):
        return self.title


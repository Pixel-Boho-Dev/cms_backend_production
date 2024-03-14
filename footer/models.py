from django.db import models

# from django.db import models

class Footer(models.Model):
    title = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    address = models.CharField(max_length=1000)
    email = models.EmailField()
    phone_number1 = models.CharField(max_length=20)
    phone_number2 = models.CharField(max_length=20)
    

    def __str__(self):
        return self.title
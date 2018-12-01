from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length =200)
    email = models.EmailField(max_length =200)
    phone = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name


    
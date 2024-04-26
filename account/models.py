from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone_number_field = models.PhoneNumberField(max_length=200, null=True)
    email_field = models.EmailField(max_length=200, null=True)
    date_created = models.DateTimeField(max_length=200, null=True)
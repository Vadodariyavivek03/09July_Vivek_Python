from django.db import models

# Create your models here.

class UserSignup(models.Model):
    fullname = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=15)
    mobile_number = models.BigIntegerField()
    created = models.DateTimeField(auto_now_add=True)
   
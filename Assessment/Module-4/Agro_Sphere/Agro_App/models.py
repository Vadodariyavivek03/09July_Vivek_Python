from django.db import models

# Create your models here.

class UserSignup(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.BigIntegerField()
    password = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
   
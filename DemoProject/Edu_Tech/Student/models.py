from django.db import models

# Create your models here.

class Student(models.Model):
    profile_pic = models.ImageField(upload_to="profiles/", blank=True, null=True)
    full_name = models.CharField(max_length=150) 
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    city = models.CharField(max_length=100)
    role = models.CharField(max_length=20, default="Student")  # for clarity
    created=models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField()
    sub = models.CharField(max_length=100)
    msg = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
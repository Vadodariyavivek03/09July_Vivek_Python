from django.db import models

# Create your models here.

class Student(models.Model):
    full_name = models.CharField(max_length=150) 
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    profile_pic = models.ImageField(upload_to="student_profiles/", default="default.png")
    created=models.DateTimeField(auto_now_add=True)

from django.db import models
from django.contrib.auth.models import User
import os
from django.utils.text import slugify

# function to rename land document files

def rename_document(instance, filename):
    base, ext = os.path.splitext(filename)
    clean_name = slugify(base)          # remove spaces and weird chars
    return f"documents/land/{clean_name}{ext}"

# ------------------------------------------------------------------------------------------- #

# function to rename id document files

def rename_id_document(instance, filename):
    base, ext = os.path.splitext(filename)
    clean_name = slugify(base)          # remove spaces and weird chars
    return f"documents/id/{clean_name}{ext}"

# Create your models here.

class UserSignup(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.BigIntegerField()
    password = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
   
class Profile(models.Model):
    user = models.ForeignKey(UserSignup, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    address = models.TextField()
    profile_image = models.FileField(upload_to="documents/profiles/")
    land_document = models.FileField(upload_to=rename_document)
    id_document = models.FileField(upload_to=rename_id_document)



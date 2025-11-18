from django.db import models

# Create your models here.

class UserSignup(models.Model):

    ROLE_CHOICES = (
        ("user", "User"),
        ("mechanic", "Mechanic"),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="user")
    fullname = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)

   
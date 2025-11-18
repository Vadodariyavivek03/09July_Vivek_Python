from django import forms
from .models import *

class SignupForm(forms.ModelForm):
    class Meta:                     
        model = UserSignup
        fields = "__all__"

        widgets = {
            "password": forms.PasswordInput(),
            "role": forms.Select(choices=[("user", "User"), ("mechanic", "Mechanic")]),
        }
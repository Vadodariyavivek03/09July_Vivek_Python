from django import forms
from .models import *

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["full_name", "mobile", "city", "profile_pic"]

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
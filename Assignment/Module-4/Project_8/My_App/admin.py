from django.contrib import admin
from .models import Doctor

# Register your models here.

class DoctorAdmin(admin.ModelAdmin):
    list_display = ("name", "specialization", "experience", "email", "phone", "available")
    search_fields = ("name", "specialization", "email")
    list_filter = ("specialization", "available")
    ordering = ("name",)

admin.site.register(Doctor, DoctorAdmin)
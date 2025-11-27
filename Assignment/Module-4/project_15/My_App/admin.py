from django.contrib import admin
from .models import Doctor, Availability

# Register your models here.

class AvailabilityInline(admin.TabularInline):
    model = Availability
    extra = 1  # number of empty rows


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("name", "specialty", "phone", "email", "available_days")
    search_fields = ("name", "specialty", "phone", "email")
    list_filter = ("specialty",)
    inlines = [AvailabilityInline]

    # Custom column showing availability days
    def available_days(self, obj):
        days = obj.availability.values_list("day", flat=True)
        return ", ".join(days)

    available_days.short_description = "Available Days"


@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ("doctor", "day", "start_time", "end_time")
    list_filter = ("day", "doctor")
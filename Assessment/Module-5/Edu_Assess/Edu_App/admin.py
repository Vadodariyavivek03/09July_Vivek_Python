from django.contrib import admin
from .models import DeliveryOrder, DeliveryAgent

# Register your models here.

admin.site.register(DeliveryOrder)
admin.site.register(DeliveryAgent)


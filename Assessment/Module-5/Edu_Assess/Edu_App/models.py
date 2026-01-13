import uuid
from django.db import models

# Create your models here

class DeliveryAgent(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    vehicle_details = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class DeliveryOrder(models.Model):
    DELIVERY_STATUS = [
        ('Pending', 'Pending'),
        ('Picked Up', 'Picked Up'),
        ('In Transit', 'In Transit'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]

    tracking_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    sender = models.CharField(max_length=100)
    recipient = models.CharField(max_length=100)
    pickup_address = models.TextField()
    delivery_address = models.TextField()
    weight = models.FloatField()
    delivery_type = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=DELIVERY_STATUS, default='Pending')
    agent = models.ForeignKey(DeliveryAgent, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.tracking_id)


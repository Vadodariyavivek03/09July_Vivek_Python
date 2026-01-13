from rest_framework import serializers
from .models import DeliveryOrder, DeliveryAgent

class DeliveryAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryAgent
        fields = '__all__'


class DeliveryOrderSerializer(serializers.ModelSerializer):
    agent_name = serializers.CharField(source='agent.name', read_only=True)
    class Meta:
        model = DeliveryOrder
        fields = '__all__'

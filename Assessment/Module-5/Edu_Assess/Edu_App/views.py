from rest_framework.viewsets import ModelViewSet
from .models import DeliveryOrder, DeliveryAgent
from .serializers import DeliveryOrderSerializer, DeliveryAgentSerializer

# Create your views here.

class DeliveryAgentViewSet(ModelViewSet):
    queryset = DeliveryAgent.objects.all()
    serializer_class = DeliveryAgentSerializer

class DeliveryOrderViewSet(ModelViewSet):
    queryset = DeliveryOrder.objects.all()
    serializer_class = DeliveryOrderSerializer



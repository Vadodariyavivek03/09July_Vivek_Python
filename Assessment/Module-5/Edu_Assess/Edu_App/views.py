from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import DeliveryOrder, DeliveryAgent
from .serializers import DeliveryOrderSerializer, DeliveryAgentSerializer

class DeliveryAgentViewSet(ModelViewSet):
    queryset = DeliveryAgent.objects.all()
    serializer_class = DeliveryAgentSerializer


class DeliveryOrderViewSet(ModelViewSet):
    queryset = DeliveryOrder.objects.all()
    serializer_class = DeliveryOrderSerializer

    @action(detail=False, methods=['get'], url_path='track/(?P<tracking_id>[^/.]+)')
    def track_order(self, request, tracking_id=None):
        order = DeliveryOrder.objects.filter(tracking_id=tracking_id).first()
        if not order:
            return Response({"error": "Order not found"}, status=404)
        return Response(DeliveryOrderSerializer(order).data)




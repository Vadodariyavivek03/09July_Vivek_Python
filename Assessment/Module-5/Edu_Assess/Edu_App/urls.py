from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DeliveryAgentViewSet, DeliveryOrderViewSet

router = DefaultRouter()
router.register('agents', DeliveryAgentViewSet)
router.register('orders', DeliveryOrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

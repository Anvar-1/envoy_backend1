from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='customers')
router.register(r'orders', OrderViewSet, basename='orders')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]

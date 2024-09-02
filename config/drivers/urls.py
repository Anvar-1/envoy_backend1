from django.urls import path
from config.drivers.views import DriverListCreateView, DriverDetailView


urlpatterns = [
    path('drivers/', DriverListCreateView.as_view(), name='driver-list-create'),
    path('drivers/<int:pk>/update/', DriverDetailView.as_view(), name='driver-detail'),
]
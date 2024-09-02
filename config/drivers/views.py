# from django.shortcuts import render
from rest_framework import generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Driver
from .serializers import DriverSerializer
from ..orders.models import Order

class DriverListCreateView(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class DriverDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class DriverCreateView(generics.CreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

    @action(detail=True, methods=['put'])
    def assign_order(self, request, pk=None):
        driver = self.get_object()
        order_id = request.data.get('order_id')
        if not order_id:
            return Response({'error': 'Buyurtma IDsi ko\'rsatilmagan'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            order = Order.objects.get(order_id=order_id)
        except Order.DoesNotExist:
            return Response({'error': 'Buyurtma topilmadi'}, status=status.HTTP_404_NOT_FOUND)
        if order.driver is not None:
            return Response({'error': 'Buyurtma allaqachon boshqa haydovchiga tayinlangan'},status=status.HTTP_400_BAD_REQUEST)
        driver.status = 'Tayinlangan'
        driver.save()
        order.driver = driver
        order.save()
        return Response({'msg': 'Buyurtma haydovchiga berildi'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['put'])
    def complete_order(self, request, pk=None):
        driver = self.get_object()
        try:
            order = Order.objects.get(driver=driver)
        except Order.DoesNotExist:
            return Response({'error': 'Haydovchiga tayinlangan buyurtma topilmadi'}, status=status.HTTP_404_NOT_FOUND)
        order.driver = None
        order.save()
        driver.status = 'Mavjud'
        driver.save()
        return Response({'msg': 'Buyurtma tugallandi'}, status=status.HTTP_200_OK)















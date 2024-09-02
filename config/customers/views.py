from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
from rest_framework import status

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=True, methods=['put'])
    def update_status(self, request, pk=None):
        customer = self.get_object()
        status = request.data.get('status')

        if status not in dict(Customer._meta.get_field('status').choices):
            return Response({'error': 'Invalid status value'}, status=status.HTTP_400_BAD_REQUEST)
        customer.status = status
        customer.save()
        return Response({'msg': 'Status updated successfully'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['put'])
    def assign_order(self, request, pk=None):
        customer = self.get_object()
        order_id = request.data.get('order_id')

        try:
            order = Order.objects.get(order_id=order_id)
        except Order.DoesNotExist:
            return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

        if customer.order:
            customer.order.delete()

        customer.order = order
        customer.save()
        return Response({'msg': 'Order assigned successfully'}, status=status.HTTP_200_OK)


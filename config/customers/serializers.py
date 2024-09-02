from rest_framework import serializers
from .models import Customer, Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order_id']

class CustomerSerializer(serializers.ModelSerializer):
    order = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = ['id', 'user', 'status', 'order']

    def get_order(self, obj):
        if obj.order:
            return OrderSerializer(obj.order).data
        return None


from rest_framework import serializers
from rest_framework.serializers import ChoiceField
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    pay_type = ChoiceField(choices=Order.pay_type.field.choices)

    class Meta:
        model = Order
        fields = '__all__'




# from django.contrib.auth import get_user_model
# from rest_framework import serializers
# from .models import CarInfo, Driver
#
#
# User = get_user_model()
#
# class CarInfoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CarInfo
#         fields = '__all__'
#
#
# class DriverSerializer(serializers.ModelSerializer):
#     car_info = CarInfoSerializer()
#
#     class Meta:
#         model = Driver
#         fields = '__all__'
#
#     def create(self, validated_data):
#         car_info_data = validated_data.pop('car_info')
#         car_info = CarInfo.objects.create(**car_info_data)
#         driver = Driver.objects.create(car_info=car_info, **validated_data)
#         return Driver


from rest_framework import serializers
from .models import Driver
from ..customers.models import Order


class DriverSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all(), required=False)
    class Meta:
        model = Driver
        fields = '__all__'







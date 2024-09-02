from django.contrib import admin
from .models import Order
from django.contrib.admin import ModelAdmin

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user_order_id', 'car_type', 'customer_name', 'deal']
    search_fields = ['car_type', 'customer_name']


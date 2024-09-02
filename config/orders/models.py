from django.db import models
from config.drivers.models import Driver
# from config.customers.models import Customer


class Order(models.Model):
    # Customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    order_id = models.AutoField(primary_key=True)
    car_type = models.CharField(max_length=100)
    car_case = models.CharField(max_length=100)
    load_weight = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=50)
    height = models.DecimalField(max_digits=10, decimal_places=2)
    length = models.DecimalField(max_digits=10, decimal_places=2)
    width = models.DecimalField(max_digits=10, decimal_places=2)
    start = models.CharField(max_length=200)
    finish = models.CharField(max_length=200)
    current_time = models.DateTimeField(auto_now=True)
    load_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    plastic_card = models.DecimalField(max_digits=20, decimal_places=2)
    price_amount = models.DecimalField(max_digits=10, decimal_places=2)
    pay_type = models.CharField(max_length=50, choices=[
        ('naqd pul', 'Naqd pul'),
        ('card', 'Card'),
        ('humo_card', 'Humo_Card'),
        ('uzcard', 'Uzcard'),
    ], default='cash')

    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Order {self.order_id} - {self.car_type}"



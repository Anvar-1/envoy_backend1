from django.db import models
from django.conf import settings

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)

class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[
        ('kutilmoqda', 'Kutilmoqda'),
        ('yakunlandi', 'Yakunlandi'),
        ('bekor qilingan', 'Bekor qilingan'),
    ], default='kutilmoqda')
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f"Customer {self.user.username} - Order {self.order.order_id}"





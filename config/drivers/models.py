# from django.db import models

# class CarInfo(models.Model):
#     car_name = models.CharField(max_length=100)
#     car_number = models.CharField(max_length=20)
#     text_pass = models.CharField(max_length=20)
#     driver_license = models.CharField(max_length=20)
#     car_type = models.CharField(max_length=50)
#     car_case = models.CharField(max_length=50)
#     load_weight = models.CharField(max_length=20)
#     size = models.CharField(max_length=20)
#     height = models.CharField(max_length=20)
#     length = models.CharField(max_length=20)
#     width = models.CharField(max_length=20)
#
# def __str__(self):
#         return self.car_name
#
# class Driver(models.Model):
#     driver_id = models.AutoField(primary_key = True)
#     order_id = models.ForeignKey(order_id, on_delete=models.RESTRICT)
#
#     def __str__(self):
#         return f"Driver {self.order_id}"

from django.db import models

class Driver(models.Model):
    driver_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=50, default='Available')
    # order_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.status






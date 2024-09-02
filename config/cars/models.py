from django.db import models
from django.utils.translation import gettext_lazy as _
from config.drivers.models import Driver


class Cars(models.Model):
    Driver = models.ForeignKey(Driver, on_delete=models.CASCADE, blank=True, null=True)
    car_name = models.CharField(_("car name"), max_length=50)
    car_number = models.CharField(_("car number"), max_length=20)
    car_type = models.CharField(_("car type"), max_length=50)
    car_case = models.CharField(_("car case"), max_length=50)
    load_weight = models.FloatField(_("load weight"), blank=True, null=True)
    size = models.CharField(_("size"), max_length=50)
    height = models.FloatField(_("height"), blank=True, null=True)
    length = models.FloatField(_("length"), blank=True, null=True)
    width = models.FloatField(_("width"), blank=True, null=True)

    class Meta:
        verbose_name = _("Car")
        verbose_name_plural = _("Cars")

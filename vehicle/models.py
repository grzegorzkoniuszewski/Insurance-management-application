# from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models

from accounts.models import CustomUser
from insurance.models import InsurancePolicy, PolicyStatus


class VehicleStatus(models.Model):
    vehicle_status = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.vehicle_status

    class Meta:
        verbose_name = "Vehicle status"
        verbose_name_plural = "Vehicle statuses"


class CustomVehicle(models.Model):
    registration_number = models.CharField(max_length=20)
    vin_number = models.CharField(max_length=17, validators=[MinLengthValidator(17), MaxLengthValidator(17)], unique=True)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    owner = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    purchase_date = models.DateField(null=False)
    sale_date = models.DateField(null=True, blank=True)
    policy = models.ForeignKey(InsurancePolicy, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(
        VehicleStatus,
        verbose_name="Vehicle Status",
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return f"{self.make} {self.model}"

    def save(self, *args, **kwargs):
        if not self.owner and hasattr(self, 'request') and self.request.user.is_authenticated:
            self.owner = self.request.user

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Vehicle"
        verbose_name_plural = "Vehicle"

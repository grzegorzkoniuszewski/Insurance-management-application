# from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from insurance.models import InsurancePolicy


class CustomVehicle(models.Model):
    registration_number = models.CharField(max_length=20)
    vin_number = models.CharField(max_length=17, validators=[MinLengthValidator(17), MaxLengthValidator(17)],unique=True)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    purchase_date = models.DateField(null=False)
    sale_date = models.DateField(null=True, blank=True)
    policy = models.ForeignKey(InsurancePolicy, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.make} {self.model}"

    class Meta:
        verbose_name = "Vehicle"
        verbose_name_plural = "Vehicle"


class VehicleStatus(models.Model):
    # Represents the status of an vehicle.
    vehicle_status_name = models.CharField(max_length=15, unique=True)

    def __str__(self):
        # Returns the name of the vehicle status as a string representation of the object.
        return self.vehicle_status_name

    class Meta:
        verbose_name = "Vehicle status"
        verbose_name_plural = "Vehicle statuses"

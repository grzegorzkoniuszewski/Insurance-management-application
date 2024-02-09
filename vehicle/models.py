# from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomVehicle(models.Vehcle):
    registration_number = models.CharField(max_length=20)
    vin_number = models.CharField(max_length=17, validators=[MinLengthValidator(17), MaxLengthValidator(17)],unique=True)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    purchase_date = models.DateField(null=False)
    sale_date = models.DateField(null=True, blank=True)
    policy = models.ForeignKey(InsurancePolicy)

    def __str__(self):
        return f"{self.make} {self.model}"

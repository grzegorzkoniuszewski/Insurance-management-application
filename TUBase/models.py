from django.db import models


class CustomTUBase(models.Model):
    short_name = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=255)
    address_street = models.CharField(max_length=255)
    address_building_number = models.CharField(max_length=20)
    address_postal_code = models.CharField(max_length=10)
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    id_name = models.CharField(max_length=3, unique=True)

    # this is for create id_name used for policy number that contains id_name of insurance company and exact number
    def save(self, *args, **kwargs):
        self.id_name = self.short_name[:3]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.short_name

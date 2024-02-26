from django.contrib import admin
from .models import CustomVehicle, VehicleStatus
# Register your models here.


@admin.register(CustomVehicle)
class VehicleAdmin(admin.ModelAdmin):
    # Display the 'vehicle' field in the admin list view.
    list_display = ('registration_number', 'vin_number', 'make', 'model')


@admin.register(VehicleStatus)
class VehicleStatus(admin.ModelAdmin):
    # Display the 'vehicle_status_name' field in the admin list view.
    list_display = ('vehicle_status',)


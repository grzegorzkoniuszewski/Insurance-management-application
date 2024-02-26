from django.shortcuts import render
from django.http import HttpResponse

import vehicle
from .models import CustomVehicle, VehicleStatus


# View for displaying a list of vehicles.
def vehicle_list(request):
    vehicle = CustomVehicle.objects.all()
    return render(request, 'vehicle_list.html')


# View for displaying details of a single vehicle.
def vehicle_detail(request, id):
    vehicle = CustomVehicle.objects.get(pk=id)
    return render(request, 'vehicle_detail.html', {'vehicle': vehicle})


# View for adding a vehicle.
def vehicle_add(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'vehicle_add.html')


# View for editing an existing vehicle details.
def vehicle_details_edit(request, id):
    vehicle = CustomVehicle.objects.get(pk=id)
    if request.method == 'POST':
        pass
    else:
        return render(request, 'vehicle_details_edit.html', {'vehicle': vehicle})


def vehicle_status_add(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'vehicle_status_add.html')


def vehicle_status_delete(request, vehicle_status_id):
    vehicle_status = VehicleStatus.objects.get(pk=id)
    pass


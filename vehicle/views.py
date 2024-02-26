from django.shortcuts import render
from django.http import HttpResponse
from .models import CustomVehicle


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

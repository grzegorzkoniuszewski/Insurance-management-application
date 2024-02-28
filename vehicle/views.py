from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import VehicleForm
import vehicle
from .models import CustomVehicle, VehicleStatus


def vehicle_list(request):
    queryDataAll = CustomVehicle.objects.all()

    context = {'AllVehicles': queryDataAll}

    return render(request, 'vehicle_list.html', context)


def vehicle_detail(request, id):
    vehicle = CustomVehicle.objects.get(pk=id)
    return render(request, 'vehicle_detail.html', {'vehicle': vehicle})


def vehicle_add(request):
    form = VehicleForm()

    if request.method == 'POST':

        form = VehicleForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('vehicle_list')

    context = {"VehicleForm": form}

    return render(request, 'vehicle_add.html', context)


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

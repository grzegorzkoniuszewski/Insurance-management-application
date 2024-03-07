from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import VehicleForm
from .models import CustomVehicle, VehicleStatus


@login_required
def vehicle_list(request):
    query_data = CustomVehicle.objects.filter(owner=request.user)
    context = {'AllVehicles': query_data}
    return render(request, 'vehicle_list.html', context)


@login_required
def vehicle_detail(request, id):
    vehicle = CustomVehicle.objects.get(pk=id)
    policy = vehicle.policy
    policy_start_date = policy.validity_start_date if policy else None
    policy_end_date = policy.validity_end_date if policy else None
    return render(request, 'vehicle_detail.html', {'vehicle': vehicle, 'start': policy_start_date, 'end':policy_end_date})


@login_required
def vehicle_add(request):
    form = VehicleForm()

    if request.method == 'POST':

        form = VehicleForm(request.POST)

        if form.is_valid():
            custom_vehicle = form.save(commit=False)
            custom_vehicle.request = request
            custom_vehicle.save()
            return redirect('vehicle_list')

    context = {"VehicleForm": form}

    return render(request, 'vehicle_add.html', context)


@login_required
def vehicle_remove(request, id):
    vehicle = get_object_or_404(CustomVehicle, pk=id)
    context = {
        'id': id,
        'message': ''
    }
    if request.user == vehicle.owner:
        vehicle.delete()
        context['message'] = "Requested vehicle removal was successful!"
    else:
        context['message'] = "You do not have permission to remove the vehicle"
    return render(request, 'vehicle_delete.html', context)


@login_required
def vehicle_details_edit(request, id):
    vehicle = get_object_or_404(CustomVehicle, pk=id)

    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm(instance=vehicle)

    return render(request, 'vehicle_details_edit.html', {'form': form, 'vehicle': vehicle})


@login_required
def vehicle_status_add(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'vehicle_status_add.html')


@login_required
def vehicle_status_delete(request, vehicle_status_id):
    vehicle_status = VehicleStatus.objects.get(pk=id)
    pass

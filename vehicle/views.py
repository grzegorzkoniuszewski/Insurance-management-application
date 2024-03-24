# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from .forms import VehicleForm
# from .models import CustomVehicle, VehicleStatus
#
#
# @login_required
# def vehicle_list(request):
#     query_data = CustomVehicle.objects.filter(owner=request.user)
#     context = {'AllVehicles': query_data}
#     return render(request, 'vehicle_list.html', context)
#
#
# @login_required
# def vehicle_detail(request, id):
#     vehicle = CustomVehicle.objects.get(pk=id)
#     policy = vehicle.policy
#     policy_start_date = policy.validity_start_date if policy else None
#     policy_end_date = policy.validity_end_date if policy else None
#     return render(request, 'vehicle_detail.html', {'vehicle': vehicle, 'start': policy_start_date, 'end':policy_end_date})
#
#
# @login_required
# def vehicle_add(request):
#     form = VehicleForm()
#
#     if request.method == 'POST':
#
#         form = VehicleForm(request.POST)
#
#         if form.is_valid():
#             custom_vehicle = form.save(commit=False)
#             custom_vehicle.request = request
#             custom_vehicle.save()
#             return redirect('vehicle_list')
#
#     context = {"VehicleForm": form}
#
#     return render(request, 'vehicle_add.html', context)
#
#
# @login_required
# def vehicle_remove(request, id):
#     vehicle = get_object_or_404(CustomVehicle, pk=id)
#     context = {
#         'id': id,
#         'message': ''
#     }
#     if request.user == vehicle.owner:
#         vehicle.delete()
#         context['message'] = "Requested vehicle removal was successful!"
#     else:
#         context['message'] = "You do not have permission to remove the vehicle"
#     return render(request, 'vehicle_delete.html', context)
#
#
# @login_required
# def vehicle_details_edit(request, id):
#     vehicle = get_object_or_404(CustomVehicle, pk=id)
#
#     if request.method == 'POST':
#         form = VehicleForm(request.POST, instance=vehicle)
#         if form.is_valid():
#             form.save()
#             return redirect('vehicle_list')
#     else:
#         form = VehicleForm(instance=vehicle)
#
#     return render(request, 'vehicle_details_edit.html', {'form': form, 'vehicle': vehicle})
#
#
# @login_required
# def vehicle_status_add(request):
#     if request.method == 'POST':
#         pass
#     else:
#         return render(request, 'vehicle_status_add.html')
#
#
# @login_required
# def vehicle_status_delete(request, vehicle_status_id):
#     vehicle_status = VehicleStatus.objects.get(pk=id)
#     pass
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from .forms import VehicleForm
from .models import CustomVehicle, VehicleStatus


class VehicleListView(LoginRequiredMixin, ListView):
    model = CustomVehicle
    template_name = 'vehicle_list.html'
    login_url = '/login/'

    def get_queryset(self):
        return CustomVehicle.objects.filter(owner=self.request.user)


class VehicleDetailView(LoginRequiredMixin, DetailView):
    model = CustomVehicle
    template_name = 'vehicle_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vehicle = self.object
        policy_start_date = vehicle.policy.validity_start_date if vehicle.policy else None
        policy_end_date = vehicle.policy.validity_end_date if vehicle.policy else None
        context['start'] = policy_start_date
        context['end'] = policy_end_date
        return context


class VehicleAddView(LoginRequiredMixin, CreateView):
    model = CustomVehicle
    form_class = VehicleForm
    template_name = 'vehicle_add.html'
    success_url = reverse_lazy('vehicle_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class VehicleRemoveView(LoginRequiredMixin, DeleteView):
    model = CustomVehicle
    template_name = 'vehicle_delete.html'
    success_url = reverse_lazy('vehicle_list')

    def get(self, request, *args, **kwargs):
        vehicle = self.get_object()
        if request.user == vehicle.owner:
            return super().get(request, *args, **kwargs)
        else:
            return redirect('vehicle_list')


class VehicleDetailsEditView(LoginRequiredMixin, UpdateView):
    model = CustomVehicle
    form_class = VehicleForm
    template_name = 'vehicle_details_edit.html'
    success_url = reverse_lazy('vehicle_list')

    def get(self, request, *args, **kwargs):
        vehicle = self.get_object()
        if request.user == vehicle.owner:
            return super().get(request, *args, **kwargs)
        else:
            return redirect('vehicle_list')


class VehicleStatusAddView(LoginRequiredMixin, CreateView):
    model = VehicleStatus
    fields = ['vehicle_status']
    template_name = 'vehicle_status_add.html'
    success_url = reverse_lazy('vehicle_list')


class VehicleStatusDeleteView(LoginRequiredMixin, DeleteView):
    model = VehicleStatus
    template_name = 'vehicle_status_delete.html'
    success_url = reverse_lazy('vehicle_list')

    def get_object(self, queryset=None):
        status_id = self.kwargs.get('vehicle_status_id')
        return get_object_or_404(VehicleStatus, pk=status_id)

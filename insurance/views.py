# from django.core.exceptions import PermissionDenied
# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.template.context_processors import request
# from django.views.generic import CreateView
#
# from .models import InsurancePolicy
# from .forms import InsuranceForm
# from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# from django.shortcuts import render
# from django.views import View
# from django.contrib.messages import error
#
#
# def insurance_list(request):
#     queryDataAll = InsurancePolicy.objects.all()
#
#     context = {'AllInsurances': queryDataAll}
#
#     return render(request, 'insurance_list.html', context)
#
#
# # View for displaying details of a single insurance policy.
# def policy_detail(request, policy_id):
#     policy = InsurancePolicy.objects.get(pk=policy_id)
#     return render(request, 'policy_detail.html', {'policy': policy})
#
#
# def insurance_add(request):
#     form = InsuranceForm()
#
#     if request.method == 'POST':
#
#         form = InsuranceForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return redirect('insurance_list')
#         # else
#     context = {"InsuranceForm": form}
#
#     return render(request, 'insurance_add.html', context)
#
#
# def policy_edit(request, policy_id):
#     policy = InsurancePolicy.objects.get(pk=policy_id)
#     if request.method == 'POST':
#         # Process form data and update the policy.
#         # Redirect to the policy detail page.
#         pass
#     else:
#         return render(request, 'policy_edit.html', {'policy': policy})
#
#
# def policy_delete(request, policy_id):
#     policy = InsurancePolicy.objects.get(pk=policy_id)
#     # Delete the policy and redirect to the policy list page.
#     pass
#
#
# def policy_list(request):
#     policies = InsurancePolicy.objects.all()
#     return render(request, 'policy_list.html', {'policies': policies})
#
#
# # def policy_add(request, LoginRequiredMixin, PermissionRequiredMixin):
# #     if request.method == 'POST':
# #         # Process form data and save the new policy.
# #         # Redirect to the policy detail page.
# #         pass
# #     else:
# #         # Display the form for adding a new policy.
# #         return render(request, 'policy_add.html')
#
# class PolicyAddView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
#     # Set the required permissions
#     permission_required = 'insurance_insurancepolicy.add_insurancepolicy'
#
#     def post(self, request):
#         # Process form data and save the new policy.
#         # Redirect to the policy detail page.
#         pass
#
#     def get(self, request):
#         # Display the form for adding a new policy.
#         return render(request, 'insurance_add.html')
#
# def home(request):
#     return render(request, 'base.html')


from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy

from .models import InsurancePolicy
from .forms import InsuranceForm


class InsuranceListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = InsurancePolicy
    template_name = 'insurance_list.html'
    login_url = '/login/'
    permission_required = 'insurance_insurancepolicy.view_insurancepolicy'


class InsuranceAddView(LoginRequiredMixin, CreateView):
    model = InsurancePolicy
    form_class = InsuranceForm
    template_name = 'insurance_add.html'
    # login_url = '/login/'
    success_url = reverse_lazy('insurance_list')
    # permission_required = 'insurance_insurancepolicy.add_insurancepolicy'


class InsuranceEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = InsurancePolicy
    form_class = InsuranceForm
    template_name = 'insurance_edit.html'
    # login_url = '/login/'
    success_url = reverse_lazy('insurance_list')
    permission_required = 'insurance_insurancepolicy.change_insurancepolicy'


class InsuranceDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = InsurancePolicy
    success_url = reverse_lazy('insurance_list')
    # login_url = '/login/'
    permission_required = 'insurance_insurancepolicy.delete_insurancepolicy'


def home(request):
    return render(request, 'base.html')
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


class InsuranceListView(LoginRequiredMixin, ListView):
    model = InsurancePolicy
    template_name = 'insurance_list.html'
    login_url = '/login/'

    def get_queryset(self):
        return InsurancePolicy.objects.filter(policy_creator=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['policies'] = self.get_queryset()
        return context


class InsuranceAddView(LoginRequiredMixin, CreateView):
    model = InsurancePolicy
    form_class = InsuranceForm
    template_name = 'insurance_add.html'
    success_url = reverse_lazy('insurance_list')

    def form_valid(self, form):
        form.instance.policy_creator = self.request.user
        return super().form_valid(form)


class InsuranceEditView(LoginRequiredMixin, UpdateView):
    model = InsurancePolicy
    form_class = InsuranceForm
    template_name = 'insurance_edit.html'
    success_url = reverse_lazy('insurance_list')



class InsuranceDeleteView(LoginRequiredMixin, DeleteView):
    model = InsurancePolicy
    template_name = 'insurance_delete.html'
    success_url = reverse_lazy('insurance_list')


def home(request):
    return render(request, 'base.html')

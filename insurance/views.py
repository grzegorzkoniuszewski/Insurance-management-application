from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
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


class InsuranceDetailView(LoginRequiredMixin, DetailView):
    model = InsurancePolicy
    template_name = 'insurance_detail.html'


def home(request):
    return render(request, 'base.html')

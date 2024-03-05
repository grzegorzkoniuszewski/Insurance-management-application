from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import InsurancePolicy
from .forms import InsuranceForm


def insurance_list(request):

    queryDataAll = InsurancePolicy.objects.all()

    context = {'AllInsurances': queryDataAll}

    return render(request, 'insurance_list.html', context)


# View for displaying details of a single insurance policy.
def insurance_detail(request, policy_id):
    policy = InsurancePolicy.objects.get(pk=policy_id)
    return render(request, 'insurance_detail.html', {'policy': policy})


def insurance_add(request):
    form = InsuranceForm()

    if request.method == 'POST':

        form = InsuranceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('insurance_list')
        # else
    context = {"InsuranceForm": form}

    return render(request, 'insurance_add.html', context)


def insurance_edit(request, policy_id):
    policy = InsurancePolicy.objects.get(pk=policy_id)
    if request.method == 'POST':
        # Process form data and update the policy.
        # Redirect to the policy detail page.
        pass
    else:
        return render(request, 'insurance_edit.html', {'policy': policy})


def insurance_delete(request, policy_id):
    policy = InsurancePolicy.objects.get(pk=policy_id)
    # Delete the policy and redirect to the policy list page.
    pass


def home(request):
    return render(request, 'base.html')
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import InsurancePolicy
from .forms import InsuranceForm



# View for displaying a list of insurance policies.
def policy_list(request):
    policies = InsurancePolicy.objects.all()
    return render(request, 'policy_list.html', {'policies': policies})


# View for displaying details of a single insurance policy.
def policy_detail(request, policy_id):
    policy = InsurancePolicy.objects.get(pk=policy_id)
    return render(request, 'policy_detail.html', {'policy': policy})


# View for adding a new insurance policy.
def policy_add(request):
    form = InsuranceForm()

    if request.method == 'POST':

        form = InsuranceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('insurance_add')

    context = {"InsuranceForm": form}

    return render(request, 'insurance_add.html', context)






# View for editing an existing insurance policy.
def policy_edit(request, policy_id):
    policy = InsurancePolicy.objects.get(pk=policy_id)
    if request.method == 'POST':
        # Process form data and update the policy.
        # Redirect to the policy detail page.
        pass
    else:
        # Display the form for editing the policy.
        return render(request, 'policy_edit.html', {'policy': policy})


# View for deleting an existing insurance policy.
def policy_delete(request, policy_id):
    policy = InsurancePolicy.objects.get(pk=policy_id)
    # Delete the policy and redirect to the policy list page.
    pass


def home(request):
    return render(request, 'base.html')


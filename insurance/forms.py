from django.forms import ModelForm
from .models import InsurancePolicy


class InsuranceForm(ModelForm):

    class Meta:
        model = InsurancePolicy
        fields = '__all__'
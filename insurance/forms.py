from django import forms
from .models import InsurancePolicy
from django.core.validators import MinLengthValidator, MaxLengthValidator


class InsuranceForm(forms.ModelForm):
    class Meta:
        model = InsurancePolicy
        fields = '__all__'
        # fields = ['policy_number', 'validity_start_date', 'validity_end_date', 'status', 'policy_type']
        exclude = ['policy_creator']
        widgets = {
            'validity_start_date': forms.DateInput(attrs={'type': 'date'}),
            'validity_end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['policy_number'].validators.extend([MinLengthValidator(11), MaxLengthValidator(11)])

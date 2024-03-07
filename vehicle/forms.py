from django import forms
from .models import CustomVehicle


class VehicleForm(forms.ModelForm):

    class Meta:
        model = CustomVehicle
        fields = '__all__'
        exclude = ['owner']
        widgets = {
            'purchase_date': forms.DateInput(attrs={'type': 'date'}),
            'sale_date': forms.DateInput(attrs={'type': 'date'}),
        }

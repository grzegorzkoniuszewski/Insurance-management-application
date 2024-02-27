from django.forms import ModelForm
from .models import CustomVehicle

class VehicleForm(ModelForm):

    class Meta:
        model = CustomVehicle
        fields = '__all__'
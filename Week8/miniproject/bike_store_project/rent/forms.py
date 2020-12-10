from django.forms import ModelForm
from .models import *

class AddCustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class AddVehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'

class AddRentalForm(ModelForm):
    class Meta:
        model = Rental
        exclude = ['return_date']

    def __init__(self, *args, **kwargs):
        super(AddRentalForm, self).__init__(*args, **kwargs)
        rented_vehicles_ids = Rental.objects.filter(return_date = None).values_list("vehicle", flat = True)
        self.fields['vehicle'].queryset = Vehicle.objects.exclude(id__in = rented_vehicles_ids)



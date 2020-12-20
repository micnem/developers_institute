from django.forms import ModelForm
from hotel import models

class RegisterForm(ModelForm):
    class Meta:
        model = models.Customer
        exclude = ['account']

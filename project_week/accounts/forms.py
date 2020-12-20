from django.forms import ModelForm
from .models import Player

class RegisterForm(ModelForm):
    class Meta:
        model = Player
        exclude = ['account']

from django.forms import ModelForm
from . import models

class MakeOffer(ModelForm):
    class Meta:
        model = models.Offer
        exclude = ['card1','date']
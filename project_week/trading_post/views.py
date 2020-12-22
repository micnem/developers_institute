from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *
from django.contrib.auth.models import User
from accounts.models import Player
# Create your views here.
def ViewCards(request):
    cards = Card.objects.filter(owner=request.user.id)

    return render(request, 'mycards.html', {'cards':cards})

def AllDrivers(request):
    drivers = Driver.objects.all()
    paginator = Paginator(drivers, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'drivers.html', {'page_obj':page_obj})



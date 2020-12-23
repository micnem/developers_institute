from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import *
from django.contrib.auth.models import User
from accounts.models import Player
from termcolor import cprint
import json
from .forms import MakeOffer
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



def trade(request):
    
    body = json.loads(request.body)
    card_id = body['card_id']
    card = Card.objects.get(pk=card_id)
    cprint(card, 'green')
    try:
        card.trade_status = not card.trade_status
        card.save()
        return JsonResponse({"status": 'success'})
    except Exception:
        return JsonResponse({"status": 'error'})
    


def marketplace(request):
    cards = Card.objects.filter(trade_status = True)

    return render(request, 'market.html', {'cards':cards})


def offer(request, card_id):
    card1 = Card.objects.get(id=card_id)

    form = MakeOffer()
    form.fields['card2'].queryset = request.user.deck.all()
    if request.method == "POST":
        form = MakeOffer(request.POST)
        if form.is_valid():
            form.save()
            return redirect('marketplace')
    return render(request, 'offer.html', {'form':form, 'card1':card1})


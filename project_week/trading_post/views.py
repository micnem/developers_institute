from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import *
from django.contrib.auth.models import User
from accounts.models import Player
from termcolor import cprint
import json
from .forms import MakeOffer


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
    cards = Card.objects.filter(trade_status = True).exclude(owner=request.user.id)
    user_deck = request.user.deck.all()
    return render(request, 'market.html', {'cards':cards, 'user_deck':user_deck})


def offer(request, card_id):
    if not request.user.is_authenticated:
        return redirect('login')
    card1 = Card.objects.get(id=card_id)
    form = MakeOffer()
    form.fields['card2'].queryset = request.user.deck.all()
    if request.method == "POST":
        form = MakeOffer(request.POST)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.card1 = card1 
            offer.save()
            return redirect('marketplace')
    return render(request, 'offer.html', {'form':form, 'card1':card1})



def ViewOffers(request):
    offers = Offer.objects.filter(card1__owner = request.user).exclude(card2__owner = request.user).exclude(active=False)
    
    return render(request, 'viewoffers.html', {'offers':offers})


def AcceptOffer(request, offer_id, accepted):
    offer = Offer.objects.get(id=offer_id)
    card1 = Card.objects.get(pk=offer.card1_id)
    card2 = Card.objects.get(pk=offer.card2_id)
    owner1 = card1.owner
    owner2 = card2.owner
    if accepted == 'true':
        card1.owner = owner2
        card1.trade_status = False
        card2.owner = owner1
        card1.save()
        card2.save()   
    else:
        offer.active = False
        offer.save()
        print('offer rejected')
        return redirect('viewoffers')

    
    return redirect('home')


def leaderboard(request):
    players = Player.objects.all()
    
    return render(request, 'leaderboard.html', {'players':players})
from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from pprint import pprint
from . import models

# Create your views here.
def family(request, id):
    family = models.Family.objects.get(id=id)
    return render(request, 'family.html', {'family': family})

def animal(request, id):
    animal = models.Animal.objects.get(id=id)
                
    return render(request, 'animal.html', {'animal': animal})

def all_animals(request):
    all_animals = models.Animal.objects.all()

    return render(request, 'animals.html', {'all_animals': all_animals})

def on_click(request):
    return redirect('/animals')
from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from pprint import pprint

# Create your views here.
def family(request, id):
    animal_list = []
    with open('animals.json', 'r') as f:
        data = json.load(f)['animals']
        for animal in data:
            if animal['family'] == id:
                animal_list.append(animal)
                
    return render(request, 'family.html', {'animals': animal_list})

def animal(request, id):
    animal_list = []
    with open('animals.json', 'r') as f:
        data = json.load(f)['animals']
        for animal in data:
            if animal['id'] == id:
                animal_list.append(animal)
                
    return render(request, 'animal.html', {'animals': animal_list})

def all_animals(request):
    all_animals = []
    with open('animals.json', 'r') as f:
        data = json.load(f)['animals']
        for animal in data:
            all_animals.append(animal)
    return render(request, 'animals.html', {'all_animals': all_animals})

 
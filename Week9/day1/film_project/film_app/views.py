from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def homepage(request):
    films = Film.objects.all()
    return render(request, 'homepage.html', {'films':films})

def add_film(request):
    if request.method == "GET":
            form = AddFilmForm()
            return render(request, 'add_film.html', {'form':form})
        
    if request.method == "POST":
        form = AddFilmForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('homepage')

def add_director(request):
    if request.method == "GET":
            form = AddDirectorForm()
            return render(request, 'add_director.html', {'form':form})
        
    if request.method == "POST":
        form = AddDirectorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('homepage')

def film(request, id):
    film = Film.objects.get(id=id)

    return render(request, 'film.html', {'film':film})

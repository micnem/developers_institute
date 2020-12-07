from django.shortcuts import render
from . import models


# Create your views here.
def persons(request):
    all_persons = models.Person.objects.all()
    return render(request, 'persons.html', {'all_persons': all_persons})

def number(request, phone_number):
    print(phone_number)
    print(type(phone_number))
    person = models.Person.objects.get(phone_number = phone_number)
    return render(request, 'person.html', {'person': person})

def name(request, name):
    person = models.Person.objects.get(name = name.title())
    return render(request, 'name.html', {'person': person})
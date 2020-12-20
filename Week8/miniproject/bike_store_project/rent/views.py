from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

@login_required
def customers(request):
    customers = Customer.objects.all().order_by('first_name')
    return render(request, 'customers.html', {'customers' : customers})

def customer(request, id):
    customer = Customer.objects.get(id=id)
    return render(request, 'customer.html', {'customer' : customer})

def vehicles(request):
    vehicles = Vehicle.objects.all().order_by('vehicle_type')
    return render(request, 'vehicles.html', {'vehicles' : vehicles})

def vehicle(request, id):
    vehicle = Vehicle.objects.get(id=id)
    return render(request, 'vehicle.html', {'vehicle' : vehicle})

def add_customer(request):
    form = AddCustomerForm()
    if request.method == "POST":
        form = AddCustomerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('customers')
    return render(request, 'add_customer.html', {'form':form})

def add_vehicle(request):
    if request.method == "GET":
            form = AddVehicleForm()
            return render(request, 'add_vehicle.html', {'form':form})
        
    if request.method == "POST":
        form = AddVehicleForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('vehicles')

def add_rental(request):
    form = AddRentalForm()
    if request.method == "POST":
        form = AddRentalForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('rentals')
    return render(request, 'add_rental.html', {'form':form})

def rentals(request):
    rentals = Rental.objects.all()
    return render(request, 'rentals.html', {'rentals' : rentals})

def rental(request, id):
    rental = Rental.objects.get(id=id)
    return render(request, 'rental.html', {'rental' : rental})

def customer_rental(request, customer_id):
    customer_rental = Rental.objects.all().filter(customer = customer_id)
    return render(request, 'customer_rental.html', {'customer_rental' : customer_rental})

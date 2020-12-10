from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homepage, name = 'homepage'),
    path('rent/customer/', views.customers, name='customers'),
    path('rent/customer/<int:id>', views.customer, name='customer'),
    path('rent/vehicle/', views.vehicles, name='vehicles'),
    path('rent/vehicle/<int:id>', views.vehicle, name='vehicle'),
    path('rent/customer/add', views.add_customer, name='add_customer'),
    path('rent/vehicle/add', views.add_vehicle, name='add_vehicle'),
    path('rent/rental/add', views.add_rental, name='add_rental'),
    path('rent/rental/', views.rentals, name='rentals'),
    path('rent/rental/<int:id>', views.rental, name='rental')

]

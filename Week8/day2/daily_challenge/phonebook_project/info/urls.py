from django.urls import path
from . import views

urlpatterns = [
    path('persons/', views.persons),
    path('persons/phonenumber/<str:phone_number>', views.number),
    path('persons/name/<str:name>', views.name)
]
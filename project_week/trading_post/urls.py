from django.urls import path
from .views import ViewCards, AllDrivers

urlpatterns = [
    path('view/', ViewCards, name='view_cards'),
    path('all/', AllDrivers, name='all_drivers')

]
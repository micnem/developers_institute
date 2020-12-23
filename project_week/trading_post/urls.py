from django.urls import path
from .views import ViewCards, AllDrivers, trade, marketplace, offer

urlpatterns = [
    path('view/', ViewCards, name='view_cards'),
    path('all/', AllDrivers, name='all_drivers'),
    path('trade/', trade, name='trade'),
    path('marketplace/', marketplace, name='marketplace'),
    path('offer/<int:card_id>', offer, name='offer')
]
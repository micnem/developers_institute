from django.urls import path
from . import views

urlpatterns = [
    path('animal/<int:id>', views.animal, name="animal"),
    path('family/<int:id>', views.family, name="family"),
    path('animals/', views.all_animals, name="all_animals"),
    
]
from django.urls import path
from . import views


urlpatterns = [
    path('home/',  views.homepage, name='homepage'),
    path('addfilm/', views.add_film, name='add_film'),
    path('adddirector/', views.add_director, name='add_director'),
    path('film/<int:id>', views.film, name='film')

]
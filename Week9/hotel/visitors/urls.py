from django.urls import path
from . import views
from .views import ReviewList
urlpatterns = [
    path('home/', views.home, name='home'),
    path('booking/', views.book, name='book'),
    path('reviews/', ReviewList.as_view(), name='reviews'),
    path('addreview/', views.add_review, name='add_review'),
    path('review/<int:id>', views.review, name='review')
]
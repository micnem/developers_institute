from django.urls import path, include
from .views import SignUpView, homepage, profile

urlpatterns = [
    path('home/', homepage, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('profile/', profile, name='profile')
]
from django.urls import path, include
from .views import SignUpView, Register, homepage

urlpatterns = [
    path('home/', homepage, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('register/', Register.as_view(), name='register'),
    path('account/', include('django.contrib.auth.urls'))
]
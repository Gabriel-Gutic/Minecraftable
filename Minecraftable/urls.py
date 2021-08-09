from django.urls import path
from django.contrib.auth import views as authtentication_views

from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('register/<data>', views.register_confirmed, name='register_confirmed'),
    path('register/confirmation/', views.register_confirmation, name='register-confirmation'),
    path('logout/', authtentication_views.LogoutView.as_view(template_name='Minecraftable/User/logout.html'), name='logout')
]
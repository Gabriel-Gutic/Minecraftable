from django.urls import path, include
from django.contrib.auth import views as authtentication_views

from Minecraftable.views import views, datapack_views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('register/confirmation/', views.register_confirmation, name='register-confirmation'),
    path('email_confirmed/<data>/', views.register_confirmed, name='register_confirmed'),
    path('logout/', authtentication_views.LogoutView.as_view(template_name='Minecraftable/User/logout.html'), name='logout'),
    path('forgot-password/', views.forgot_password, name='forgot-password'),
    path('reset-password/<data>/', views.reset_password, name='reset-password'),
    path('reset-email/<data>/', views.reset_email, name='reset-email'),
    path('email-reset-confirmation/', views.email_reset_confirmation, name='email-reset-confirmation'),
    path('recovery-email-send/', views.recovery_email_send, name='recovery-email-send'),
    path('not-permission/', views.not_permission, name='not-permission'),
    path('datapack/create/', datapack_views.create, name='datapack-create'),
    path('datapack/not-exist/', datapack_views.not_exist, name='not-exist'),
    path('datapack/<int:datapack_id>/', include('Minecraftable.urls.datapack_urls')),
]
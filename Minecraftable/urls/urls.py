from django.urls import path, include
from django.contrib.auth import views as authtentication_views

from Minecraftable.views import views, datapack_views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('register/<data>', views.register_confirmed, name='register_confirmed'),
    path('register/confirmation/', views.register_confirmation, name='register-confirmation'),
    path('logout/', authtentication_views.LogoutView.as_view(template_name='Minecraftable/User/logout.html'), name='logout'),
    path('not-permission/', views.not_permission, name='not-permission'),
    path('datapack/create/', datapack_views.create, name='datapack-create'),
    path('datapack/not-exist/', datapack_views.not_exist, name='not-exist'),
    path('datapack/<int:datapack_id>/', include('Minecraftable.urls.datapack_urls')),
]
from django.urls import path

from Minecraftable.views import datapack_views

urlpatterns = [
    path('settings/', datapack_views.settings, name='datapack-create'),
]
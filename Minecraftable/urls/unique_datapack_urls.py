from django.urls import path

from Minecraftable.views import datapack_views

urlpatterns = [
    path('', datapack_views.datapack, name='datapack'),
    path('settings/', datapack_views.settings, name='datapack-create'),
]
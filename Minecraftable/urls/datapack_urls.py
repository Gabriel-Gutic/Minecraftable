from django.urls import path, include

from Minecraftable.views import datapack_views

urlpatterns = [
    path('create/', datapack_views.create, name='datapack-create'),
    path('<int:id>/', include('Minecraftable.urls.unique_datapack_urls')),
]
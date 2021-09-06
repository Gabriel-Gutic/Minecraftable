from django.urls import path, include

from Minecraftable.views import datapack_views, recipe_views

urlpatterns = [
    path('', datapack_views.datapack, name='datapack'),
    path('download/', datapack_views.download, name='datapack-download'),
    path('settings/', datapack_views.settings, name='datapack-create'),
    path('recipe/<int:recipe_id>/', include('Minecraftable.urls.recipe_urls')),
    path('recipe/create/', recipe_views.create, name='recipe-create'),
]
from django.urls import path

from Minecraftable.views import recipe_views


urlpatterns = [
    path('', recipe_views.recipe, name='recipe'),
]
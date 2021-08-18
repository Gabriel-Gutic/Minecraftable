from django.template import loader
from django.http import HttpResponse, JsonResponse

from Minecraftable.models import Item


def recipe(request, datapack_id, recipe_id):
    pass


def create(request, datapack_id):
    template = loader.get_template('Minecraftable/Datapack/Recipe.html')

    items = Item.objects.all()

    if request.method == 'GET' and request.is_ajax():
            if 'prepare-items' in request.GET:
                items_dict =  []
                for item in items:
                    items_dict.append({
                        'id': item.id,
                        'id_name': item.id_name,
                        'name': item.name,
                        'image': item.image.url if item.image else None,
                    })
                return JsonResponse({'items': items_dict}, status=200)

    context = {}

    return HttpResponse(template.render(context, request))
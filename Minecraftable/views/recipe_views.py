from django.template import loader
from django.http import HttpResponse, JsonResponse

from Minecraftable.models import Item, Tag
from Minecraftable.utils import get_matrix_from_request_post


def recipe(request, datapack_id, recipe_id):
    pass


def create(request, datapack_id):
    template = loader.get_template('Minecraftable/Datapack/Recipe.html')

    if request.method == 'POST':
        is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
        if is_ajax:
            if 'new-recipe' in request.POST:
                name = request.POST.get('name')
                type_ = request.POST.get('type')
                recipe = get_matrix_from_request_post(request.POST, 'recipe')
                result = request.POST.get('result')
    
                print(name)
                print(type_)
                print(recipe)
                print(result)

                return JsonResponse({'datapack_id': datapack_id}, status=200)

    if request.method == 'GET' and request.is_ajax():
            if 'prepare-items' in request.GET:
                items = Item.objects.all()
                items_dict =  []
                for item in items:
                    items_dict.append({
                        'id': item.id,
                        'id_name': item.id_name,
                        'name': item.name,
                        'image': item.image.url if item.image else None,
                    })
                return JsonResponse({'items': items_dict}, status=200)
            elif 'prepare-tags' in request.GET:
                tags_dict = []
                tags = Tag.objects.all()
                for tag in tags:
                    items = []
                    for item in tag.item_set.all():
                        items.append({
                            'id': item.id,
                            'name': item.name,
                            'image': item.image.url if item.image else None,
                        })
                    tags_dict.append({
                        'id': tag.id,
                        'name': tag.name,
                        'image': tag.image.url if tag.image else None,
                        'items': items,
                    })
                return JsonResponse({'tags': tags_dict}, status=200)
    
    context = {
        'datapack_id': datapack_id,
    }

    return HttpResponse(template.render(context, request))
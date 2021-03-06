from django.template import loader
from django.http import HttpResponse, JsonResponse

from Minecraftable.utils import first_from_dict
from Minecraftable.models import Item, Tag, Recipe, GetElementTypeAndId
from Minecraftable.recipes.creator_from_data import create_from_data
from Minecraftable.recipes.recipe_types import RECIPE_TYPES
from Minecraftable.printer import print_error, print_info
from Minecraftable.decorators import datapack_owned


@datapack_owned()
def recipe(request, datapack_id, recipe_id):
    template = loader.get_template('Minecraftable/Datapack/Recipe.html')

    if request.method == 'POST':
        is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
        if is_ajax:
            if 'recipe_id' in request.POST:
                print(request.POST)
                id = request.POST.get('recipe_id')
                name = request.POST.get('name')
                type_ = request.POST.get('type')
                recipe_list = request.POST.getlist('recipe[]')
                result = request.POST.get('result')
                
                if id == "None":
                    id = -1
                else:
                    id = int(id)
                create_from_data(
                    recipe_id=id,
                    name=name, 
                    recipe_type=type_, 
                    recipe_list=recipe_list,
                    result=result,
                    datapack_id=datapack_id,
                    )

                return JsonResponse({'datapack_id': datapack_id}, status=200)

    if request.method == 'GET' and request.is_ajax():
        if 'fill-recipe-data' in request.GET:
            recipe_ = Recipe.objects.get(id=recipe_id)

            recipe = recipe_.get_recipe()

            data = {
                'name': recipe_.name,
                'type': recipe.type(),
                'result': Item.objects.get(id_name=recipe.result).id,
                'count': recipe.result_count,
            }

            if data['type'] == 'crafting_shapeless':
                ingredients = recipe.get_ingredients()

                ingredients_list = []

                for ingredient in ingredients:
                    if 'item' in ingredient:
                        item = Item.objects.get(id_name=ingredient['item'])
                        ingredients_list.append("item~" + str(item.id))
                    elif 'tag' in ingredient:
                        tags = Tag.objects.filter(user=None).filter(name=ingredient['tag'])
                        if len(tags) == 0:
                            tags = Tag.objects.filter(user=request.user).filter(name=ingredient['tag'])
                        tag = tags[0]
                        ingredients_list.append("tag~" + str(tag.id))
                    else:
                        print_error("Unknown ingredient!")
                data['ingredients'] = ingredients_list
            elif data['type'] == 'crafting_shaped':
                crafting = [['', '', ''], ['', '', ''], ['', '', '']]
                rp = recipe.get_pattern()
                keys = recipe.get_keys()
                for i in range(3):
                    for j in range(3):
                        if rp[i][j] in keys:
                            key = keys[rp[i][j]]
                            type_ = list(key.keys())[0]
                            if type_ == 'item':
                                obj = Item.objects.get(id_name=key[type_])
                            else:
                                obj = Tag.objects.filter(name=key[type_])[0] #TODO: 
                            element = type_ + '~'  + str(obj.id)
                            crafting[i][j] = element
                data['crafting'] = crafting
            elif data['type'] == 'smithing':
                base = first_from_dict(recipe.get_base())
                type_, id = GetElementTypeAndId(type_=base[0], name=base[1], user=request.user)
                base = type_ + "~" + str(id)

                addition = first_from_dict(recipe.get_addition())
                type_, id = GetElementTypeAndId(data=addition[0] + "~" + addition[1], user=request.user)
                addition = type_ + "~" + str(id)

                data['base'] = base
                data['addition'] = addition 
            elif data['type'] in {'smelting', 'smoking', 'blasting'}:
                data['xp'] = recipe.get_experience()
                data['cooking_time'] = recipe.get_cooking_time_in_seconds()
                ingredients = recipe.get_ingredients()
                data['ingredients'] = []
                for ingredient in ingredients:
                    for key, value in ingredient.items():
                        type_, id = GetElementTypeAndId(type_=key, name=value, user=request.user)

                        data['ingredients'].append((type_, id))
            elif data['type'] == 'stonecutting':
                ingredients = recipe.get_ingredients()
                data['ingredients'] = []
                for ingredient in ingredients:
                    for key, value in ingredient.items():
                        type_, id = GetElementTypeAndId(type_=key, name=value, user=request.user)

                        data['ingredients'].append((type_, id))
            elif data['type'] == 'campfire_cooking':
                ingredients = recipe.get_ingredients()
                data['ingredients'] = []
                for ingredient in ingredients:
                    for key, value in ingredient.items():
                        type_, id = GetElementTypeAndId(type_=key, name=value, user=request.user)

                        data['ingredients'].append((type_, id))
                data['cooking_time'] = recipe.get_cooking_time_in_seconds()

            print_info("Load recipe %s with data: %s" % (recipe_.name, data))
            return JsonResponse(data, status=200)
        elif 'prepare-items' in request.GET:
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
            from itertools import chain
            tags_dict = []
            tags = sorted(list(chain(Tag.objects.filter(user=None), Tag.objects.filter(user=request.user))),
                    key=lambda instance: instance.id)
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
        'recipe_id': recipe_id,
        'recipe_types': RECIPE_TYPES,
    }

    return HttpResponse(template.render(context, request))


@datapack_owned()
def create(request, datapack_id):
    return recipe(request=request, datapack_id=datapack_id, recipe_id=None)
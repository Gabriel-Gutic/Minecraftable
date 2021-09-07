from django.template import loader
from django.http import HttpResponse, JsonResponse, response
from django.shortcuts import redirect

from Minecraftable.printer import print_error, print_info
from Minecraftable.forms import NewDatapackForm
from Minecraftable.models import Datapack, Recipe, Tag, Item
from Minecraftable.decorators import datapack_owned
from Minecraftable.decorators import login_required


@login_required()
def create(request):
    template = loader.get_template('Minecraftable/Datapack/Create.html')

    form = NewDatapackForm()
    if request.method == 'POST':
        form = NewDatapackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            version = form.cleaned_data['version']
            datapack = Datapack.objects.create(name=name, description=description, version=version, user=request.user)
            datapack.save()
            print_info("Datapack %s successfully created!")
            return redirect('/Minecraftable/home/')

    context = {
        'form': form,
    }

    return HttpResponse(template.render(context, request))


def not_exist(request):
    print_error("Datapack does not exist!")

    template = loader.get_template('Minecraftable/Datapack/not-exist.html')
    return HttpResponse(template.render({}, request))


@datapack_owned()
def settings(request, datapack_id):
    template = loader.get_template('Minecraftable/Datapack/Settings.html')

    datapack = Datapack.objects.get(id=datapack_id)

    if request.method == 'GET':
        is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
        if is_ajax:
            if 'changed-settings' in request.GET:
                name = request.GET.get('name')
                description = request.GET.get('description')
                version = request.GET.get('version')

                datapack.name = name
                datapack.description = description
                datapack.version = version
                datapack.save(force_update=True)

                print_info("Datapack %s successfully updated!" % datapack)

    context = {
        'datapack': datapack,
        'versions': Datapack.VERSIONS,
    }

    return HttpResponse(template.render(context, request))


@datapack_owned()
def datapack(request, datapack_id):
    
    if request.method == 'POST' and request.is_ajax():
        if "recipe-delete" in request.POST:
            recipe_id = int(request.POST.get('recipe-id'))
            recipe = Recipe.objects.get(id=recipe_id)
            recipe_name = recipe.name
            recipe.delete()

            print_info("Recipe '" + recipe_name + "' deleted")
            return JsonResponse({"recipe_id": recipe_id}, status=200)

    template = loader.get_template('Minecraftable/Datapack/Datapack.html')

    datapack = Datapack.objects.get(id=datapack_id)
    recipes_ = Recipe.objects.filter(datapack=datapack)
    recipes = []
    for recipe_ in recipes_:
        recipe = recipe_.get_recipe()
        id_name = recipe.get_result()

        recipes.append({ 
            'id': recipe_.id,
            'name': recipe_.name,
            "image": Item.objects.get(id_name=id_name).image.url,
        })

    context = {
        'datapack': datapack,
        'recipes': recipes,
    }

    return HttpResponse(template.render(context, request))


import os, shutil
from os.path import basename
from django.conf import settings as django_settings


@datapack_owned()
def download(request, datapack_id):
    static_root = os.path.join(django_settings.STATIC_PATH, "datapacks")
    datapack = Datapack.objects.get(id=datapack_id)

    name = ''.join(char for char in datapack.name if char not in '\/:*?"<>|')
    main_folder = os.path.join(static_root, name)
    i = 0

    while os.path.exists(main_folder):
        i += 1
        main_folder = os.path.join(static_root, name + "_" + str(i))
    
    os.mkdir(main_folder)

    with open(os.path.join(main_folder, 'pack.mcmeta'), 'w') as pack_file:
        pack_data = {
            "pack": {
            "pack_format": datapack.version,
            "description": datapack.description,
            }
        }

        import json

        pack_content = json.dumps(pack_data, indent=4)
        pack_file.write(pack_content) 
        pack_file.close()

    data_folder = os.path.join(main_folder, 'data')
    os.mkdir(data_folder)

    os.mkdir(os.path.join(data_folder, "minecraft"))
    own_path = os.path.join(data_folder, "own")
    os.mkdir(own_path)

    recipe_path = os.path.join(own_path, "recipes")
    os.mkdir(recipe_path)

    recipes = Recipe.objects.filter(datapack=datapack)
    for recipe in recipes:
        jp = os.path.join(recipe_path, recipe.name)
        json_path = jp + ".json"
        i = 0
        while os.path.exists(json_path):
            i += 1
            json_path = jp + "_" + str(i) + ".json"
        json_file = open(json_path, "w")

        json_file.write(recipe.json_data)
        json_file.close()

    tags_path = os.path.join(own_path, "tags")
    os.mkdir(tags_path)

    items_path = os.path.join(tags_path, "items")
    os.mkdir(items_path)

    tags = Tag.objects.filter(user=request.user)
    for tag in tags:
        json_file = open(os.path.join(items_path, tag.name.replace("own:", "", 1) + ".json"), "w")
        json_data = {
            "values": [item.id_name for item in tag.item_set.all()],
        }

        json_file.write(json.dumps(json_data, indent=4))
        json_file.close()

    from Minecraftable.utils import zip_from_directory
    zip_path = zip_from_directory(main_folder)
    zip_name = basename(zip_path)

    shutil.rmtree(main_folder)
    zip = open(zip_path, "rb")

    from django.core.files.storage import FileSystemStorage
    fs = FileSystemStorage()
    fs.delete(zip_name)
    zip_file = fs.save(zip_name, zip)
    zip_url = fs.url(zip_file)
    zip.close()
    os.remove(zip_path)

    return JsonResponse({"zip_url": zip_url, "zip_name": zip_name}, status=200)


def download_complete(request, zip_name):
    from django.core.files.storage import FileSystemStorage
    fs = FileSystemStorage()

    fs.delete(zip_name)
    return JsonResponse({}, status=200)

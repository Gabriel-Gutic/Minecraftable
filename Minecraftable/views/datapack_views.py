from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect

from Minecraftable.printer import print_error, print_info
from Minecraftable.forms import NewDatapackForm
from Minecraftable.models import Datapack, Recipe
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
    recipes = Recipe.objects.filter(datapack=datapack)

    context = {
        'datapack': datapack,
        'recipes': recipes,
    }

    return HttpResponse(template.render(context, request))
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect

from Minecraftable.forms import NewDatapackForm
from Minecraftable.models import Datapack, Client, Item
from Minecraftable.scripts.minecraft_data_filler import Filler


def create(request):
    template = loader.get_template('Minecraftable/Datapack/Create.html')

    form = NewDatapackForm()
    if request.method == 'POST':
        form = NewDatapackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            version = form.cleaned_data['version']
            datapack = Datapack.objects.create(name=name, description=description, version=version, client=Client.objects.get(user=request.user))
            datapack.save()
            return redirect('/Minecraftable/home/')

    context = {
        'form': form,
    }

    return HttpResponse(template.render(context, request))


def settings(request, id):
    template = loader.get_template('Minecraftable/Datapack/Settings.html')

    datapack = Datapack.objects.get(id=id)

    if request.method == 'GET':
        if request.is_ajax():
            if 'changed-settings' in request.GET:
                name = request.GET.get('name')
                description = request.GET.get('description')
                version = request.GET.get('version')

                datapack.name = name
                datapack.description = description
                datapack.version = version
                datapack.save(force_update=True)

    context = {
        'datapack': datapack,
        'versions': Datapack.VERSIONS,
    }

    return HttpResponse(template.render(context, request))


# TODO: items filler
def datapack(request, id):
    template = loader.get_template('Minecraftable/Datapack/Datapack.html')

    context = {}

    return HttpResponse(template.render(context, request))
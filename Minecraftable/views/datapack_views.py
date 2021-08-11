from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect

from Minecraftable.forms import NewDatapackForm
from Minecraftable.models import Datapack, Client


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

    context = {
        'datapack': datapack,
        'versions': Datapack.VERSIONS,
    }

    return HttpResponse(template.render(context, request))
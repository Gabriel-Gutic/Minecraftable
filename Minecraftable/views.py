from django.http import HttpResponse
from django.template import loader

from .forms import NewDatapackForm


def home(request):
    
    template =  loader.get_template('Minecraftable/Home-Page.html')

    form = NewDatapackForm()
    context = {
        'form': form,
    }

    return HttpResponse(template.render(context, request))
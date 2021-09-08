from django.template import loader
from django.http import HttpResponse


def error_404(request, exception):
    template = loader.get_template('Minecraftable/Error-404.html')

    return HttpResponse(template.render({}, request))


def error_400(request, exception):
    template = loader.get_template('Minecraftable/Error-400.html')

    return HttpResponse(template.render({}, request))


def error_403(request, exception):
    template = loader.get_template('Minecraftable/User/not-permission.html')

    return HttpResponse(template.render({}, request))


def error_500(request):
    template = loader.get_template('Minecraftable/Error-500.html')

    return HttpResponse(template.render({}, request))

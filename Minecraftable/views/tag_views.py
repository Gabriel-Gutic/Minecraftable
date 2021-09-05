from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.contrib import messages

from Minecraftable.models import Item, Tag
from Minecraftable.decorators import tag_owned
from Minecraftable.printer import print_error


def tag_update(request):
    if request.method == 'POST' and request.is_ajax():
        name = request.POST.get('name')
        items = request.POST.getlist('items')
        items = items[0].split(',')
        image = request.FILES.get('image')

        tags_base = Tag.objects.filter(name=name, user=None)
        tags_user = Tag.objects.filter(name=name, user=request.user)

        if tags_user.count() > 0 or tags_base.count() > 0:
            return JsonResponse({'error': "This name is already taken!"}, status=200)

        if 'create' in request.POST:
            tag = Tag.objects.create(name=name, image=image, user=request.user)
            tag.save()

            for id in items:
                item = Item.objects.get(id=int(id))
                item.tags.add(tag)
                item.save()
        elif 'update' in request.POST:
            tag_id = request.POST.get('tag-id')
            tag = Tag.objects.get(id=tag_id)

            tag.name = name
            tag.image = image
            tag.item_set.clear()
            tag.save()
            for id in items:
                item = Item.objects.get(id=int(id))
                item.tags.add(tag)
                item.save()

    return JsonResponse({}, status=200)


def create(request):
    template = loader.get_template('Minecraftable/Tag/Tag.html')

    items = Item.objects.all()

    context = {
        'items': items,
    }

    return HttpResponse(template.render(context, request))

@tag_owned()
def tag(request, tag_id):
    template = loader.get_template('Minecraftable/Tag/Tag.html')

    tag = Tag.objects.get(id=tag_id)
    items = Item.objects.all()
    context = {
        'items': items,
        'tag': tag,
    }

    return HttpResponse(template.render(context, request))


def not_exist(request):
    print_error("Tag does not exist!")

    template = loader.get_template('Minecraftable/Tag/not-exist.html')
    return HttpResponse(template.render({}, request))
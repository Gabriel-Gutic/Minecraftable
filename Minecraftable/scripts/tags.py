from Minecraftable.models import Tag

for tag in Tag.objects.all():
    print(tag.name)
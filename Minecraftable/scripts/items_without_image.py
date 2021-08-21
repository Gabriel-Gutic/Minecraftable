from Minecraftable.models import Item

for item in Item.objects.all():
    if not item.image:
        print(item.id_name)
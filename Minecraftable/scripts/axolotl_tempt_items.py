from Minecraftable.models import Tag, Item

tag = Tag.objects.filter(name='axolotl_tempt_items')[0]

items = Item.objects.filter(tags=tag)
for item in items:
    print(item.id_name)
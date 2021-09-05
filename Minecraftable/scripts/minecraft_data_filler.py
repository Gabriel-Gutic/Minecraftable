from bs4 import BeautifulSoup
import urllib.request
import json
import shutil
import os

from Minecraftable.models import Item, Tag
from Minecraftable.printer import print_info, print_error


class Filler():

    def __init__(self):
        self.url = 'https://minecraftitemids.com'

        json_file = open('D:/VS CODE/PYTHON/DJANGO/Minecraftable/config.json')
        config = json.loads(json_file.read())

        static_url = config.get('static')
        self.static = static_url

    def remove_all_items(self):
        items_path = self.static + '/images/items'
        if os.path.isdir(items_path):
            shutil.rmtree(items_path)
        os.mkdir(items_path)
        Item.objects.all().delete()
    
    def remove_all_tags(self):
        file = open('MineSite/Minecraftable/scripts/default_tags.txt', 'r')
        for line in file.readlines():
            line = line[:-1]
            Tag.objects.filter(name=line).delete()
        

    def fill_items(self):
        #Iterate through all 9 pages that contain ids
        for index in range(1, 10):
            page_url = self.url + '/' + str(index)
            page=urllib.request.urlopen(page_url)

            print_info("Page %s opened!" % page_url)

            soup = BeautifulSoup(page, 'html.parser')
            page_data = soup.find_all('tr', {'class': 'tsr'})
            #Go through all lines of the table from the curent page
            for item in page_data:
                parts = item.findAll('td')

                #Get the item's name and id
                name = parts[1].string
                if name == 'Air':
                    continue
                id = parts[2].string

                image_path = None
                image = item.find('img')

                #If the item has an image, copy the image in the static folder
                if image is not None:
                    image_url = image['src']
                    image_url = image_url.replace("32", "128", 1) #Get images in higher resolution

                    list_ = image_url.split('/')
                    filename = list_[len(list_) - 1]

                    image_path = 'items/' + filename
                    result = urllib.request.urlretrieve(self.url + image_url, self.static + '/images/' + image_path)
                else:
                    extra_items_path = self.static + '/images/extra-items/'

                    if os.path.exists(extra_items_path + id[10:] + '.png'):
                        image_path = 'extra-items/' + id[10:] + '.png'
                        print_error("Image path: " + image_path)
                #If the item is not already existing, create it
                items = Item.objects.filter(id_name=id)
                if len(items) == 0 and (image_path is not None):
                    try:
                        item = Item.objects.create(
                            id_name=id,
                            name=name,
                            image=image_path,
                        )
                        item.save()

                        print_info("Item %s successfully created!" % item)
                    except Item.DoesNotExist:
                        item = Item.objects.get(id_name=id)
                        print_error("Id name: '" + id + "' is  already taken  by item: " + item.id + " --- " + item.name)
                        return
    
    def fill_tags(self):
        #Open the page with tags
        url = 'https://minecraft.fandom.com/wiki/Tag'
        page=urllib.request.urlopen(url)

        soup = BeautifulSoup(page, 'html.parser')
        page_find=soup.select('tr[id*="items"]')
        #Some tags are using other tags
        #Go through all of them, create the ones that are possible to be created
        #Then go back and reiterate them
        #finished is True when all are created
        finished = False
        while not finished:
            finished = True
            #Go through all tags
            for item in page_find:
                parts = item.findAll('td')

                #The tag names have a '\n' character at the end
                image_name = parts[0].string[:-1]
                tag_name = 'minecraft:' + image_name

                tags = Tag.objects.filter(name=tag_name)
                if len(tags) == 0:
                    tag_finished = True

                    #Get the items that are containing the curent tag
                    ids = parts[1].text.split(', ')
                    ids[-1] = str(ids[-1])[:-1]
                    for i in range(len(ids)):
                        ids[i] = 'minecraft:' + ids[i]
                    #Get the tags that are specified for the curent tag
                    other_tags = parts[1].findAll('a')
                    for other_tag in other_tags:
                        other_tag_name = 'minecraft:' + other_tag.string.replace('#','')

                        #Check if this tag already exists:
                        t = Tag.objects.filter(name=other_tag_name)
                        if len(t) > 0:
                            other_tag_items = Item.objects.filter(tags=t[0])
                            for item in other_tag_items:
                                ids.append(item.id_name)
                        else:
                            finished = False
                            tag_finished = False
                    
                    if tag_finished:
                        image_path = 'default_tags/' + image_name + '.png'
                        if os.path.exists(self.static + '\\images\\' + image_path):
                            new_tag = Tag.objects.create(
                                name=tag_name,
                                image=image_path,
                                )
                            new_tag.save()
                            for id in ids:
                                try:
                                    item = Item.objects.get(id_name=id)
                                    item.tags.add(new_tag)
                                except Item.DoesNotExist:
                                    print("Item '" + id + "' does not exist!" )
                            print_info("Tag " + tag_name + " finished!")
                        else:
                            print_error("Image '" + image_path + "' not found!")
                            return

filler = Filler()
filler.remove_all_items()
filler.remove_all_tags()
filler.fill_items()
filler.fill_tags()
        






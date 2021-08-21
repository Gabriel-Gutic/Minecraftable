from bs4 import BeautifulSoup
import urllib.request
import json
import shutil
import os

from Minecraftable.models import Item, Tag

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
        Tag.objects.all().delete()

    def fill_items(self):
        #Iterate through all 9 pages that contain ids
        for index in range(1, 10):
            print(index)
            page=urllib.request.urlopen(self.url + '/' + str(index))

            soup = BeautifulSoup(page, 'html.parser')
            page_data = soup.find_all('tr', {'class': 'tsr'})
            #Go through all lines of the table from the curent page
            for item in page_data:
                parts = item.findAll('td')

                #Get the item's name and id
                name = parts[1].string
                if name == 'Air':
                    continue
                id = parts[2].string[10:]

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

                    if os.path.exists(extra_items_path + id + '.png'):
                        image_path = 'extra-items/' + id + '.png'
                #If the item is not already existing, create it
                items = Item.objects.filter(id_name=id)
                if len(items) == 0 and (image_path is not None):
                    Item.objects.create(
                        id_name=id,
                        name=name,
                        image=image_path,
                    )
        
    
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
                tag_name = parts[0].string[:-1]

                tags = Tag.objects.filter(name=tag_name)
                if len(tags) == 0:
                    tag_finished = True

                    #Get the items that are containing the curent tag
                    ids = parts[1].text.split(', ')
                    ids[-1] = str(ids[-1])[:-1]
                    #Get the tags that are specified for the curent tag
                    other_tags = parts[1].findAll('a')
                    for other_tag in other_tags:
                        other_tag_name = other_tag.string.replace('#','')

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
                        image_path = 'tags/' + tag_name + '.png'
                        if os.path.exists(self.static + '\\images\\tags\\' + tag_name + '.png'):
    
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
                            print("Tag " + tag_name + " finished!")
                        else:
                            print("Image '" + image_path + "' not found!")
                            return

filler = Filler()
filler.remove_all_items()
filler.remove_all_tags()
filler.fill_items()
filler.fill_tags()

        
        






from bs4 import BeautifulSoup
import urllib.request
import json
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.files.storage import FileSystemStorage

from Minecraftable.models import Item, Tag

class Filler():

    def __init__(self):
        self.url = 'https://minecraftitemids.com'

    def remove_all_items(self):
        Item.objects.all().delete()
    
    def remove_all_tags(self):
        Tag.objects.all().delete()

    def fill(self):
        json_file = open('D:/VS CODE/PYTHON/DJANGO/Minecraftable/config.json')
        config = json.loads(json_file.read())

        static_url = config.get('static')

        file_system_storage = FileSystemStorage()

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
                    result = urllib.request.urlretrieve(self.url + image_url, static_url + '/images/' + image_path)
                    


                #If the item is not already existing, create it
                items = Item.objects.filter(id_name=id)
                if len(items) == 0:
                    Item.objects.create(
                        id_name=id,
                        name=name,
                        image=image_path,
                    )
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

                #The tag names have a '\n' character at the end, except the last one
                #So if it's not the last one, erase the last character
                if item != page_find[-1]:
                    tag_name = parts[0].string[:-1]
                else:
                    tag_name = parts[0].string

                tags = Tag.objects.filter(name=tag_name)
                if len(tags) == 0:
                    tag_finished = True

                    #Get the items that are containing the curent tag
                    ids = parts[1].text.split(', ')
                    ids[-1] = str(ids[-1])[:-1]
                    #Get the tags that are specified for the curent tag
                    other_tags = parts[1].findAll('a')

                    if len(tags) > 0:
                        for other_tag in other_tags:
                            other_tag_name = other_tag.string.replace('#','')

                            #Check if this tag already exists:
                            t = Tag.objects.filter(name=other_tag_name)
                            if len(t) > 0:
                                other_tag_items = Item.objects.filter(tags=t[0])
                                ids.extend(other_tag_items.values_list('id_name'))

                                print("Tag:" + tag_name)
                                print(ids)
                                print("------")
                            else:
                                finished = False
                                tag_finished = False
                    
                    if tag_finished:
                        new_tag = Tag.objects.create(name=tag_name)
                        new_tag.save()
                        for id in ids:
                            try:
                                item = Item.objects.get(id_name=id)
                                item.tags.add(new_tag)


                            except Item.DoesNotExist:
                                print("Item '" + id + "' does not exist!" )



        
        






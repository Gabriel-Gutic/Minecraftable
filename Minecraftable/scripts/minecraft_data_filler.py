from bs4 import BeautifulSoup
import requests
import urllib.request
import json
from django.core.files import File

from Minecraftable.models import Item

class Filler():

    def __init__(self):
        self.url = 'https://minecraftitemids.com'

    def remove_all_items(self):
        Item.objects.all().delete()

    def fill(self):
        

        json_file = open('D:/VS CODE/PYTHON/DJANGO/Minecraftable/config.json')
        config = json.loads(json_file.read())

        static_url = config['static']

        for index in range(1, 10):
            page=urllib.request.urlopen(self.url + '/' + str(index))

            soup = BeautifulSoup(page, 'html.parser')
            page_data = soup.find_all('tr', {'class': 'tsr'})
            i = 0
            for item in page_data:
                parts = item.findAll('td')

                name = parts[1].string
                id = parts[2].string

                image_path = None
                image = item.find('img')

                if image is not None:
                    image_url = image['src']

                    list_ = image_url.split('/')
                    filename = list_[len(list_) - 1]
                    image_path = static_url + '/images/items/' + filename

                    result = urllib.request.urlretrieve(self.url + image_url, image_path)

                items = Item.objects.filter(id=id)
                if len(items) == 0:
                    Item.objects.create(
                        id=id,
                        name=name,
                        image=image_path,
                    )
                i += 1
        
        






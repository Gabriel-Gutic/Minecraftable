import os
from os import path
import json

from Minecraftable.printer.error import print_error


class Datapack():

    def __init__(self, location=None, name=None, format=7):
        self.location = location
        self.name = name
        self.format = format

    def create(self):
        if path.exists(self.location + '/' + self.name):
            print_error('Directory ' + self.name + ' already exists!')
        else:
            dir_path = self.location + '/' + self.name
            os.mkdir(dir_path)
            pack_file = open(dir_path + '/pack.mcmeta', 'w')
            json.dump({ "pack": {
                "pack_format": self.format,
                "description": "Data Pack Test"}
            }, pack_file, indent=4)

            dir_path = dir_path + '/' + 'data'
            os.mkdir(dir_path)
            os.mkdir(dir_path + '/minecraft')

            dir_path = dir_path + '/namespace_test'
            os.mkdir(dir_path)
            os.mkdir(dir_path + '/recipes')



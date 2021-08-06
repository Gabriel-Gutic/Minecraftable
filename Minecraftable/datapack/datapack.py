import os
from os import path
import json

from Minecraftable.printer.error import print_error


class DatapackCreator():

    def __init__(self, location=None, name=None, format=7, description=None):
        self.location = location
        self.name = name
        self.format = format
        self.description = description

        self.recipe_path = None

        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def create_datapack(self):
        if path.exists(self.location + '/' + self.name):
            print_error('Directory ' + self.name + ' already exists!')
            return False
        else:
            dir_path = self.location + '/' + self.name
            os.mkdir(dir_path)
            pack_file = open(dir_path + '/pack.mcmeta', 'w')
            json.dump({ "pack": {
                "pack_format": self.format,
                "description": self.description}
            }, pack_file, indent=4)

            dir_path = dir_path + '/' + 'data'
            os.mkdir(dir_path)
            os.mkdir(dir_path + '/minecraft')

            dir_path = dir_path + '/namespace_test'
            os.mkdir(dir_path)
            os.mkdir(dir_path + '/recipes')

            self.recipe_path = dir_path + '/recipes'
            return True

    def create_recipes(self):
        for file in os.listdir(self.recipe_path):
            os.remove(self.recipe_path + '/' + file)

        for recipe in self.recipes:
            name = self.recipe_path + '/' + recipe.type() + '.json'
            i = 1
            while path.exists(name):
                name = self.recipe_path + '/' + recipe.type() + '_' + str(i) + '.json'

            recipe.write(name)



import json

from .recipe import Recipe
from Minecraftable.printer.error import print_error

class CraftingRecipeShapeless(Recipe):

    def __init__(self):
        super().__init__()
        self.ingredients = []
    
    def type(self):
        return 'crafting_shapeless'

    def  add_ingredient(self, item):
        if self.ingredients_number() >= 9:
            print_error('The max of 9 ingradients exceeded!')
        else:
            self.ingredients.append({'item': item})

    def remove_ingredient(self, item):
        for i in range(len(self.ingredients)):
            if self.ingredients[i]['item'] == item:
                del self.ingredients[i]
                break

    def ingredients_number(self):
        return len(self.ingredients)

    def write(self, path):
        dictionary = {
            "type": self.type(),
            "ingredients": self.ingredients,
            "result": {
                "item": self.result, 
                "count": self.result_count
            }
        }

        with open(path, 'w') as json_file:
            json.dump(dictionary, json_file, indent=4)


class CraftingRecipeShaped(Recipe):

    def __init__(self):
        super().__init__()

        self.pattern = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.key = {}

    def type(self):
        return 'crafting_shaped'

    def set_pattern(self, key, i, j):
        self.pattern[i][j] = key

    def add_key(self, key, value):
        if key in self.key:
            if type(self.key[key]) == list:
                self.key[key].append({ "item": value })
            else:
                old_key = self.key[key]
                self.key[key] = [old_key]
                self.key[key].append({ "item": value })
        else: 
            self.key[key] = { "item": value }

    def remove_key(self, key):
        del self.key[key]

    def remove_value_from_key(self, key, value):
        if key in self.key:
            if type(self.key[key]) == list:
                for element in self.key[key]:
                    if element['item'] == value:
                        self.key[key].remove(element)
                        break
            else:
                self.remove_key(key)
        else:
            print_error('Key not found!')

    def write(self, path):

        sp = self.pattern

        pattern = [
            sp[0][0] + sp[0][1] + sp[0][2],
            sp[1][0] + sp[1][1] + sp[1][2],
            sp[2][0] + sp[2][1] + sp[2][2],
        ]

        dictionary = {
            "type": self.type(),
            "pattern": pattern,
            "key": self.key,
            "result": {
                "item": self.result, 
                "count": self.result_count
            }
        }

        with open(path, 'w') as json_file:
            json.dump(dictionary, json_file, indent=4)




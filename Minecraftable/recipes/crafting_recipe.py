from .recipe import RawRecipe
from Minecraftable.printer import print_error, print_info
from Minecraftable.utils import next_alpha


class CraftingRecipeShapeless(RawRecipe):

    def __init__(self):
        super().__init__()
        self.ingredients = []
    
    def type(self):
        return 'crafting_shapeless'

    def get_ingredients(self):
        return self.ingredients

    def  add_ingredient(self, type_, name):
        if self.ingredients_number() >= 9:
            print_error('The max of 9 ingradients exceeded!')
            return

        if type_ == 'item':
            self.ingredients.append({'item': name})
        elif type_ == 'tag':
            self.ingredients.append({'tag': name})
    
    def remove_item_from_ingredients(self, item):
        for ingredient in self.ingredients:
            if 'item' in ingredient:
                if ingredient['item'] == item:
                    self.ingredients.remove(ingredient)
                    break
    
    def remove_tag_from_ingredients(self, tag):
        for ingredient in self.ingredients:
            if 'tag' in ingredient:
                if ingredient['tag'] == tag:
                    self.ingredients.remove(ingredient)
                    break

    def ingredients_number(self):
        return len(self.ingredients)

    def _fill_dictionary_(self):
        if self.ingredients_number() < 1:
            return 'No ingredients in ' + self.type() + ' recipe'
        self.dictionary["ingredients"] = self.ingredients
        self.dictionary["result"] = {
                "item": self.result, 
                "count": self.result_count
            }
        return None

    def fill_data_from_dictionary(self, dictionary):
        d = dictionary
        if 'ingredients' in d:
            self.ingredients = d['ingredients']
        if 'result' in d:
            result = d['result']
            if 'item' in result:
                self.result = result['item']
            if 'count' in result:
                self.result_count = result['count']


class CraftingRecipeShaped(RawRecipe):

    def __init__(self):
        super().__init__()

        self.pattern = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.keys = {} #Example: {"D": {"item": "minecraft:diamond"}}

    def type(self):
        return 'crafting_shaped'

    def get_pattern(self):
        return self.pattern

    def get_keys(self):
        return self.keys

    def add_value(self, type_, name, i, j):
        for key, value in self.keys.items():
            if type_ in value:
                if value[type_] == name:
                    self.pattern[i][j] = key
                    return

        key = 'A'
        while key in self.keys.keys():
            key = next_alpha(key) #Go to the next letter
        self.pattern[i][j] = key
        self.keys[key] = {type_: name}

    def remove_value(self, type_, name):
        for key, value in self.keys.items():
            if type_ in value:
                if value[type_] == name:
                    for line in self.pattern:
                        for x in line:
                            if x == key:
                                x = ' '
                    print(self.pattern)
                    self.keys.pop(key, None)
                    return

    def _fill_dictionary_(self):
        sp = self.pattern

        pattern = [
            sp[0][0] + sp[0][1] + sp[0][2],
            sp[1][0] + sp[1][1] + sp[1][2],
            sp[2][0] + sp[2][1] + sp[2][2],
        ]

        self.dictionary["pattern"] = pattern
        if len(self.keys) < 1:
            return 'No keys in ' + self.type() + ' recipe'
        self.dictionary["key"] = self.keys
        self.dictionary["result"] = {
                "item": self.result, 
                "count": self.result_count,
            }
        return None

    def fill_data_from_dictionary(self, dictionary):
        d = dictionary
        if 'key' in d:
            self.keys = d['key']
        if 'pattern' in d:
            pattern = d['pattern']
            print_info(pattern)
            for i in range(len(pattern)):
                row = pattern[i]
                for j in range(len(row)):
                    self.pattern[i][j] = row[j]
        if 'result' in d:
            result = d['result']
            if 'item' in result:
                self.result = result['item']
            if 'count' in result:
                self.result_count = result['count']


        




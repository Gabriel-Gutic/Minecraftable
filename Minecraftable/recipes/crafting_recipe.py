from .recipe import RawRecipe
from Minecraftable.printer import print_error, print_info


class CraftingRecipeShapeless(RawRecipe):

    def __init__(self):
        super().__init__()
        self.ingredients = []
    
    def type(self):
        return 'crafting_shapeless'

    def get_ingredients(self):
        return self.ingredients

    def  add_item_as_ingredient(self, item):
        if self.ingredients_number() >= 9:
            print_error('The max of 9 ingradients exceeded!')
        else:
            self.ingredients.append({'item': item})

    def remove_item_from_ingredients(self, item):
        for ingredient in self.ingredients:
            if 'item' in ingredient:
                if ingredient['item'] == item:
                    self.ingredients.remove(ingredient)
                    break
    
    def add_tag_as_ingredient(self, tag):
        if self.ingredients_number() >= 9:
            print_error('The max of 9 ingradients exceeded!')
        else:
            self.ingredients.append({'tag': tag})
    
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

    def _fill_dictionary_(self):

        sp = self.pattern

        pattern = [
            sp[0][0] + sp[0][1] + sp[0][2],
            sp[1][0] + sp[1][1] + sp[1][2],
            sp[2][0] + sp[2][1] + sp[2][2],
        ]

        self.dictionary["pattern"] = pattern
        if len(self.key) < 1:
            return 'No keys in ' + self.type() + ' recipe'
        self.dictionary["key"] = self.key
        self.dictionary["result"] = {
                "item": self.result, 
                "count": self.result_count
            }
        return None

    def fill_data_from_dictionary(self, dictionary):
        d = dictionary
        if 'key' in d:
            self.key = d['key']
        if 'pattern' in d:
            pattern = d['pattern']
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


        




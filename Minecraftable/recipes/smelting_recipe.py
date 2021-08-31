from .recipe import RawRecipe
from Minecraftable.printer import print_error


class SmeltingRecipe(RawRecipe):

    def __init__(self):
        super().__init__()

        self.ingredients = []

        self.experience = 0
        self.cooking_time = 200

    def type(self):
        return 'smelting'

    def add_ingredient(self, type_, name): #ingredient format: type~name
        for ingredient in self.ingredients:
            if name in ingredient.values():
                return
        self.ingredients.append({ type_: name })

    def remove_ingredient(self, data): #ingredient format: type~name
        
        type_, name = data.split('~')

        i = 0
        for ingredient in self.ingredients:
            if type_ in ingredient:
                if ingredient[type_] == name:
                    self.ingredients.pop(i)
                    return
            i += 1
    
    def get_ingredients(self):
        return self.ingredients

    def set_experience(self, experience):
        self.experience = experience

    def get_experience(self):
        return self.experience

    def set_cooking_time_in_ticks(self, ticks):
        self.cooking_time = ticks

    def set_cooking_time_in_seconds(self, seconds):
        self.cooking_time = seconds * 20

    def get_cooking_time(self):
        return self.cooking_time

    def get_cooking_time_in_seconds(self):
        return int(self.cooking_time / 20)

    def _fill_dictionary_(self):
        if len(self.ingredients) == 1:
            self.dictionary['ingredient'] = self.ingredients[0]
        elif len(self.ingredients) > 1:
            self.dictionary['ingredient'] = self.ingredients
        else:
            return 'No ingredients in ' + self.type() + ' recipe'

        self.dictionary['result'] = self.result
        self.dictionary['experience'] = self.experience
        self.dictionary['cookingtime'] = self.cooking_time 
        return None
    
    def fill_data_from_dictionary(self, dictionary):
        d = dictionary
        if 'ingredient' in d:
            self.ingredients = d['ingredient']
        if 'cookingtime' in d:
            self.cooking_time = d['cookingtime']
        if 'experience' in d:
            self.experience = d['experience']
        if 'result' in d:
            self.result = d['result']


class BlastingRecipe(SmeltingRecipe):
    def __init__(self):
        super().__init__()

        self.cooking_time = 100

    def type(self):
        return 'blasting'


class SmokingRecipe(SmeltingRecipe):
    def __init__(self):
        super().__init__()

        self.cooking_time = 100

    def type(self):
        return 'smoking'


class CampfireRecipe(SmeltingRecipe):
    def __init__(self):
        super().__init__()

        self.cooking_time = 600

    def type(self):
        return 'campfire_cooking'

    
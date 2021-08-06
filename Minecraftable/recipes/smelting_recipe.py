from .recipe import Recipe


class SmeltingRecipe(Recipe):

    def __init__(self):
        super().__init__()

        self.ingredients = []

        self.experience = 0
        self.cooking_time = 200

    def type(self):
        return 'smelting'

    def add_ingredient_by_item(self, item):
        self.ingredients.append({ 'item': item })

    def add_ingredient_by_tag(self, tag):
        self.ingredients.append({ 'tag': tag })
    
    def remove_ingredient_by_item(self, item):
        i = 0
        for ingredient in self.ingredients:
            if 'item' in ingredient:
                if ingredient['item'] == item:
                    self.ingredients.pop(i)
                    break
            i += 1
    
    def remove_ingredient_by_tag(self, tag):
        i = 0
        for ingredient in self.ingredients:
            if 'tag' in ingredient:
                if ingredient['tag'] == tag:
                    self.ingredients.pop(i)
                    break
            i += 1

    def set_experience(self, experience):
        self.experience = experience

    def set_cooking_time_in_ticks(self, ticks):
        self.cooking_time = ticks

    def set_cooking_time_in_seconds(self, seconds):
        self.cooking_time = seconds * 20

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
        with dictionary as d:
            if 'ingredients' in d:
                self.ingredients = d['ingredients']
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

    
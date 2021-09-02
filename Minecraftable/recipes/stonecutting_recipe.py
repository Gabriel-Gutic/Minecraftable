from .recipe import RawRecipe


class StonecuttingRecipe(RawRecipe):

    def __init__(self):
        super().__init__()

        self.ingredients = []

    def type(self):
        return 'stonecutting'

    def get_ingredients(self):
        return self.ingredients

    def add_ingredient(self, type_, name): #ingredient format: type~name
        for ingredient in self.ingredients:
            if name in ingredient.values():
                return
        self.ingredients.append({ type_: name })
    
    def remove_ingredient(self, type_, name): #ingredient format: type~name
        i = 0
        for ingredient in self.ingredients:
            if type_ in ingredient:
                if ingredient[type_] == name:
                    self.ingredients.pop(i)
                    return
            i += 1

    def _fill_dictionary_(self):
        if len(self.ingredients) == 1:
            self.dictionary['ingredient'] = self.ingredients[0]
        elif len(self.ingredients) > 1:
            self.dictionary['ingredient'] = self.ingredients
        else:
            return 'No ingredients in ' + self.type() + ' recipe'

        self.dictionary['result'] = self.result
        self.dictionary['count'] = self.result_count
        return None

    def fill_data_from_dictionary(self, dictionary):
        d = dictionary
        if 'ingredient' in d:
            if len(d['ingredient']) == 1:
                self.ingredients = [d['ingredient']]
            else:
                self.ingredients = d['ingredient']
        if 'result' in d:
            self.result = d['result']
        if 'count' in d:
            self.result_count = d['count']
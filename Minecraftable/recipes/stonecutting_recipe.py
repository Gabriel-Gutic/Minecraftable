from .recipe import Recipe


class StonecuttingRecipe(Recipe):

    def __init__(self):
        super().__init__()

        self.ingredients = []

    def type(self):
        return 'stonecutting'

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
        with dictionary as d:
            if 'ingredients' in d:
                self.ingredients = d['ingredients']
            if 'result' in d:
                self.result = d['result']
            if 'count' in d:
                self.result_count = d['count']
from .recipe import RawRecipe


class SmithingRecipe(RawRecipe):

    def __init__(self):
        super().__init__()

        self.base = {}
        self.addition = {}

    def type(self):
        return 'smithing'

    def get_base(self):
        return self.base

    def get_addition(self):
        return self.addition

    def set_base(self, type_, name):
        self.base.clear()
        self.base[type_] = name

    def set_addition(self, type_, name):
        self.addition.clear()
        self.addition[type_] = name

    def _fill_dictionary_(self):
        if 'item' in self.base:
            self.dictionary['base'] = { 'item': self.base['item'] }
        elif 'tag' in self.base:
            self.dictionary['base'] = { 'tag': self.base['tag'] }
        else:
            return "No item or tag in " + self.type() + " recipe's base"
        
        if 'item' in self.addition:
            self.dictionary['addition'] = { 'item': self.addition['item'] }
        elif 'tag' in self.addition:
            self.dictionary['addition'] = { 'tag': self.addition['tag'] }
        else:
            return "No item or tag in " + self.type() + " recipe's addition"

        self.dictionary['result'] = { 'item': self.result }
        return None

    def fill_data_from_dictionary(self, dictionary):
        d = dictionary
        if 'base' in d:
            base = d['base']
            if 'tag' in base:
                self.base['tag'] = base['tag']
            elif 'item' in base:
                self.base['item'] = base['item']
        if 'addition' in d:
            addition = d['addition']
            if 'tag' in addition:
                self.addition['tag'] = addition['tag']
            elif 'item' in addition:
                self.addition['item'] = addition['item']
        if 'result' in d:
            if 'item' in d['result']:
                self.result = d['result']['item']
            



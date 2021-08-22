from .recipe import RawRecipe


class SmithingRecipe(RawRecipe):

    def __init__(self):
        super().__init__()

        self.base = {"item": None, "tag": None}
        self.addition = {"item": None, "tag": None}

    def type(self):
        return 'smithing'

    def set_base_by_item(self, item):
        self.base['item'] = item

    def set_base_by_tag(self, tag):
        self.base['tag'] = tag

    def set_addition_by_item(self, item):
        self.addition['item'] = item

    def set_addition_by_tag(self, tag):
        self.addition['tag'] = tag

    def _fill_dictionary_(self):
        if self.base['item'] is not None:
            self.dictionary['base'] = { 'item': self.base['item'] }
        elif self.base['tag'] is not None:
            self.dictionary['base'] = { 'tag': self.base['tag'] }
        else:
            return "No item or tag in " + self.type() + " recipe's base"
        
        if self.addition['item'] is not None:
            self.dictionary['addition'] = { 'item': self.addition['item'] }
        elif self.addition['tag'] is not None:
            self.dictionary['addition'] = { 'tag': self.addition['tag'] }
        else:
            return "No item or tag in " + self.type() + " recipe's addition"

        self.dictionary['result'] = { 'item': self.result }
        return None

    def fill_data_from_dictionary(self, dictionary):
        d = dictionary
        if 'addition' in d:
            addition = d['addition']
            if 'tag' in addition:
                self.addition['tag'] = addition['tag']
            elif 'item' in addition:
                self.addition['item'] = addition['item']
        if 'addition' in d:
            addition = d['addition']
            if 'tag' in addition:
                self.addition['tag'] = addition['tag']
            elif 'item' in addition:
                self.addition['item'] = addition['item']
        if 'result' in d:
            if 'item' in d['result']:
                self.result = d['result']['item']
            



import json

from Minecraftable.printer.error import print_error


class RawRecipe():

    def __init__(self):
        self.dictionary = {}
        self.group = None
        self.result = None
        self.result_count = 1

    def type(self):
        return None

    def set_group(self, group):
        self.group = group

    def set_result(self, result):
        self.result = result

    def set_result_count(self, result_count):
        self.result_count = result_count

    def _fill_dictionary_(self):
        pass
    
    def get_json_data(self):
        self.dictionary['type'] = self.type()
        if self.group is not None:
            self.dictionary['group'] = self.group

        if self.result is None:
            error = 'No result set for ' + self.type() + ' recipe'
        else:
            error = self._fill_dictionary_()

        if error is not None:
            print_error(error)
            return
        
        json_data = json.dumps(self.dictionary, indent=4)
        return str(json_data)

    def fill_data_from_dictionary(self, dictionary):
        pass

    def write(self, path):
        json_data = self.get_json_data()

        with open(path, 'w') as json_file:
            json_file.write(json_data)

        

    
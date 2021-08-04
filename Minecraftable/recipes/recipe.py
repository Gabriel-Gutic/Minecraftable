
from Minecraftable.printer.error import print_error


class Recipe():

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

    def write(self, path):
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

        import json
        with open(path, 'w') as json_file:
            json.dump(self.dictionary, json_file, indent=4)

    
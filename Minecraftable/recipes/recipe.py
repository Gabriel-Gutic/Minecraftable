
class Recipe():

    def __init__(self):
        self.result = None
        self.result_count = 1

    def type(self):
        return None

    def set_result(self, result):
        self.result = result

    def set_result_count(self, result_count):
        self.result_count = result_count

    def write(self, path):
        pass

    
from .bcolors import bcolors


class Error():
    def __init__(self, message):
        self.message = message
    
    def get_error_message(self):
        return self.message

    def print(self):
        print_error(self.get_error_message())

    def __str__(self):
        return self.get_error_message()

def print_error(message : str):
    print(bcolors.FAIL + "ERROR: " + message + bcolors.ENDC)
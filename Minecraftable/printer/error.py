from .bcolors import bcolors


class Error():
    def __init__(self, message):
        self.message = message
    
    def get_error_message(self):
        return self.message

    def get_error(self):
        return bcolors.FAIL + "ERROR: " + self.message + bcolors.ENDC

    def __str__(self):
        return self.get_error()

def print_error(message):
    print(bcolors.FAIL + "ERROR: " + message + bcolors.ENDC)
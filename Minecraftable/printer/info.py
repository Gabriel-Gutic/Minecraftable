from .bcolors import bcolors


class Info():
    def __init__(self, message):
        self.message = message
    
    def get_info_message(self):
        return self.message

    def print(self):
        print_info(self.get_info_message())

    def __str__(self):
        return self.get_info_message()

def print_info(message : str):
    print(bcolors.OKGREEN + "INFO: " + message + bcolors.ENDC)
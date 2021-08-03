from .bcolors import bcolors

def print_error(message):
    print(bcolors.FAIL + "ERROR: " + message + bcolors.ENDC)
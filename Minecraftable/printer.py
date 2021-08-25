class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Error():
    def __init__(self, message):
        self.message = message
    
    def get_error_message(self):
        return self.message

    def print(self):
        print_error(self.get_error_message())

    def __str__(self):
        return self.get_error_message()

def print_error(message):
    print(bcolors.FAIL + "ERROR: " + str(message) + bcolors.ENDC)


class Info():
    def __init__(self, message):
        self.message = message
    
    def get_info_message(self):
        return self.message

    def print(self):
        print_info(self.get_info_message())

    def __str__(self):
        return self.get_info_message()

def print_info(message):
    print(bcolors.OKGREEN + "INFO: " + str(message) + bcolors.ENDC)
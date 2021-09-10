
from django.conf import settings as django_settings
import os
import shutil

from Minecraftable.printer import print_info

def RemoveFinishedDatapacks():
    print_info("Removing start!")
    folder = os.path.join(django_settings.STATIC_PATH, 'datapacks/finished')
    shutil.rmtree(folder)
    os.mkdir(folder)


RemoveFinishedDatapacks()
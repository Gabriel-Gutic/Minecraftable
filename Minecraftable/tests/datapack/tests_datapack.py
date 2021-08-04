from django.test import TestCase
import shutil

from Minecraftable.datapack.datapack  import Datapack


class DatapackTest(TestCase):

    def test_create_datapack(self):
        shutil.rmtree('test files/DATAPACK TEST')

        dp = Datapack(location='test files', name='DATAPACK TEST')

        dp.create()
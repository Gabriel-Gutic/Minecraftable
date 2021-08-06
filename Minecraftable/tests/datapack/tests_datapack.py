from django.test import TestCase
import shutil
from os import path

from Minecraftable.datapack.datapack  import DatapackCreator
from Minecraftable.recipes.crafting_recipe import CraftingRecipeShapeless, CraftingRecipeShaped


class DatapackTest(TestCase):

    def test_create_datapack(self):
        if path.exists('test files/DATAPACK TEST'):
            shutil.rmtree('test files/DATAPACK TEST')

        dp = DatapackCreator(location='test files', name='DATAPACK TEST')

        dp.create_datapack()

        #Add recipes
        cr1_shapeless = CraftingRecipeShapeless()

        cr1_shapeless.add_ingredient('bone')
        cr1_shapeless.add_ingredient('steak')

        cr1_shapeless.set_result('diamond')

        dp.add_recipe(cr1_shapeless)
        
        cr2_shapeless = CraftingRecipeShapeless()

        cr2_shapeless.add_ingredient('bone')
        cr2_shapeless.add_ingredient('steak')

        cr2_shapeless.set_result('diamond')

        dp.add_recipe(cr2_shapeless)

        crs = CraftingRecipeShaped()
        crs.set_pattern('D', 0, 2)
        crs.set_pattern('D', 1, 0)
        crs.set_pattern('D', 1, 2)
        crs.set_pattern('D', 2, 0)
        crs.set_pattern('D', 2, 1)
        crs.set_pattern('D', 2, 2)

        crs.set_pattern('L', 1, 1)

        crs.add_key('D', 'diamond')
        crs.add_key('L', 'white_wool')
        crs.add_key('L', 'green_wool')
        crs.add_key('L', 'blue_wool')

        crs.set_result('diamond_horse_armor')

        dp.add_recipe(crs)

        dp.create_recipes()
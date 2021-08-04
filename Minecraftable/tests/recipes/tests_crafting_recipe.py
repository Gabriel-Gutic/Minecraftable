from django.test import TestCase

from Minecraftable.recipes.crafting_recipe import CraftingRecipeShapeless, CraftingRecipeShaped


class  CraftingRecipeTest(TestCase):

    def test_crafting_shapeless(self):
        crs = CraftingRecipeShapeless()

        crs.add_ingredient('bone')
        crs.add_ingredient('gunpowder')
        crs.add_ingredient('steak')

        crs.set_result('diamond')

        crs.remove_ingredient('gunpowder')

        crs.write('test files/crafting_recipe_shapeless.json')


    def test_crafting_shaped(self):
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
        crs.add_key('L', 'black_wool')
        crs.add_key('L', 'green_wool')
        crs.add_key('L', 'blue_wool')

        crs.remove_value_from_key('L', 'black_wool')

        crs.add_key('A', 'white_wool')
        crs.remove_value_from_key('A', 'white_wool')

        crs.set_result('diamond_horse_armor')

        crs.write('test files/crafting_recipe_shaped.json')


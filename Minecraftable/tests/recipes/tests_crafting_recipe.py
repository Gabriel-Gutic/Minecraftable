from django.test import TestCase

from Minecraftable.recipes.crafting_recipe import CraftingRecipeShapeless, CraftingRecipeShaped
from Minecraftable.printer import print_error, print_info


class  CraftingRecipeTest(TestCase):

    def test_crafting_shapeless(self):
        crs = CraftingRecipeShapeless()

        crs.add_item_as_ingredient('bone')
        crs.add_item_as_ingredient('gunpowder')
        crs.add_item_as_ingredient('steak')

        crs.remove_item_from_ingredients('gunpowder')

        crs.add_tag_as_ingredient('wool')
        crs.add_tag_as_ingredient('slabs')

        crs.remove_tag_from_ingredients('slabs')
        
        crs.set_result('diamond')

        crs.write('test files/crafting_recipe_shapeless.json')


    def test_crafting_shaped(self):
        crs = CraftingRecipeShaped()
        crs.add_value("item~diamond", 0, 2)
        crs.add_value("item~diamond", 1, 2)
        crs.add_value("item~diamond", 2, 2)
        crs.add_value("item~diamond", 2, 1)
        crs.add_value("item~diamond", 1, 0)
        crs.add_value("item~diamond", 2, 0)

        crs.add_value('tag~wool', 1, 1)
        print_info(crs.get_pattern())
        crs.set_result('diamond_horse_armor')

        crs.write('test files/crafting_recipe_shaped.json')


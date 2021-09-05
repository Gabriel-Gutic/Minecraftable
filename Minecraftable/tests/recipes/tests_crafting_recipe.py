from django.test import TestCase

from Minecraftable.recipes.crafting_recipe import CraftingRecipeShapeless, CraftingRecipeShaped
from Minecraftable.printer import print_error, print_info


class  CraftingRecipeTest(TestCase):

    def test_crafting_shapeless(self):
        crs = CraftingRecipeShapeless()

        crs.add_ingredient('item', 'minecraft:bone')
        crs.add_ingredient('item', 'minecraft:gunpowder')
        crs.add_ingredient('item', 'minecraft:steak')

        crs.remove_item_from_ingredients('minecraft:gunpowder')

        crs.add_ingredient('tag', 'minecraft:wool')
        crs.add_ingredient('tag', 'minecraft:slabs')

        crs.remove_tag_from_ingredients('minecraft:slabs')
        
        self.assertEqual(crs.get_ingredients(), [{'item': 'minecraft:bone'}, {'item': 'minecraft:steak'}, {'tag': 'minecraft:wool'}])

        crs.set_result('minecraft:diamond')
        self.assertEqual(crs.get_result(), 'minecraft:diamond')

        crs.set_result_count(10)
        self.assertEqual(crs.get_count(), 10)

        crs.write('test files/crafting_recipe_shapeless.json')


    def test_crafting_shaped(self):
        crs = CraftingRecipeShaped()
        crs.add_value("item", "minecraft:diamond", 0, 2)
        crs.add_value("item", "minecraft:diamond", 1, 2)
        crs.add_value("item", "minecraft:diamond", 2, 2)
        crs.add_value("item", "minecraft:diamond", 2, 1)
        crs.add_value("item", "minecraft:diamond", 1, 0)
        crs.add_value("item", "minecraft:diamond", 2, 0)

        crs.add_value("tag", "minecraft:wool", 1, 1)
        print_info(crs.get_pattern())
        self.assertEqual(crs.get_pattern(), [[' ', ' ', 'A'], ['A', 'B', 'A'], ['A', 'A', 'A']])
        
        crs.set_result('minecraft:diamond_horse_armor')
        self.assertEqual(crs.get_result(), 'minecraft:diamond_horse_armor')

        crs.set_result_count(10)
        self.assertEqual(crs.get_count(), 10)

        crs.write('test files/crafting_recipe_shaped.json')


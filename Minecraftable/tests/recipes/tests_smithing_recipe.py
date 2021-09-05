from django.test import TestCase

from Minecraftable.recipes.smithing_recipe import SmithingRecipe


class SmithingRecipeTest(TestCase):

    def test_smithing_recipe_with_item(self):
        sr = SmithingRecipe()

        sr.set_base('item', 'minecraft:iron_pickaxe')
        self.assertEqual(sr.get_base(), {'item': 'minecraft:iron_pickaxe'})

        sr.set_addition('item', 'minecraft:diamond')
        self.assertEqual(sr.get_addition(), {'item': 'minecraft:diamond'})

        sr.set_result('minecraft:diamond_pickaxe')
        self.assertEqual(sr.get_result(), 'minecraft:diamond_pickaxe')

        sr.write('test files/smithing_recipe_with_item.json')

    def test_smithing_recipe_with_tag(self):
        sr = SmithingRecipe()

        sr.set_base('tag', 'minecraft:leaves')
        self.assertEqual(sr.get_base(), {'tag': 'minecraft:leaves'})

        sr.set_addition('tag', 'minecraft:anvil')
        self.assertEqual(sr.get_addition(), {'tag': 'minecraft:anvil'})

        sr.set_result('minecraft:diamond_pickaxe')
        self.assertEqual(sr.get_result(), 'minecraft:diamond_pickaxe')

        sr.write('test files/smithing_recipe_with_tag.json')
from django.test import TestCase

from Minecraftable.recipes.stonecutting_recipe import StonecuttingRecipe


class StonecuttingRecipeTest(TestCase):

    def test_stonecutting_recipe(self):
        sr = StonecuttingRecipe()

        sr.add_ingredient('item', 'minecraft:granite')
        sr.add_ingredient('item', 'minecraft:granite')
        sr.add_ingredient('tag',  'minecraft:leaves')
        self.assertEqual(sr.get_ingredients(), [{'item': 'minecraft:granite'}, {'tag': 'minecraft:leaves'}])

        sr.add_ingredient('item', 'minecraft:stone')
        sr.remove_ingredient('item', 'minecraft:stone')
        self.assertEqual(sr.get_ingredients(), [{'item': 'minecraft:granite'}, {'tag': 'minecraft:leaves'}])

        sr.add_ingredient('tag', 'minecraft:stone')
        sr.remove_ingredient('tag', 'minecraft:stone')
        self.assertEqual(sr.get_ingredients(), [{'item': 'minecraft:granite'}, {'tag': 'minecraft:leaves'}])

        sr.set_result('minecraft:grass_block')
        self.assertEqual(sr.get_result(), 'minecraft:grass_block')
        
        sr.set_result_count(3)
        self.assertEqual(sr.get_count(), 3)

        sr.write('test files/stonecutting_recipe.json')
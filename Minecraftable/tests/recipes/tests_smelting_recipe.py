from django.test import TestCase

from Minecraftable.recipes.smelting_recipe import SmeltingRecipe, BlastingRecipe, SmokingRecipe, CampfireRecipe


class SmeltingRecipeTest(TestCase):

    def __test_smelting_recipe__(self, recipe):
        recipe.add_ingredient('item', 'minecraft:granite')
        recipe.add_ingredient('item', 'minecraft:granite')
        recipe.add_ingredient('tag',  'minecraft:leaves')
        self.assertEqual(recipe.get_ingredients(), [{'item': 'minecraft:granite'}, {'tag': 'minecraft:leaves'}])

        recipe.add_ingredient('item', 'minecraft:stone')
        recipe.remove_ingredient('item', 'minecraft:stone')
        self.assertEqual(recipe.get_ingredients(), [{'item': 'minecraft:granite'}, {'tag': 'minecraft:leaves'}])

        recipe.add_ingredient('tag', 'minecraft:stone')
        recipe.remove_ingredient('tag', 'minecraft:stone')
        self.assertEqual(recipe.get_ingredients(), [{'item': 'minecraft:granite'}, {'tag': 'minecraft:leaves'}])

        recipe.set_result('minecraft:grass_block')
        self.assertEqual(recipe.get_result(), 'minecraft:grass_block')

        recipe.set_cooking_time_in_seconds(2)
        self.assertEqual(recipe.get_cooking_time_in_seconds(), 2)

        recipe.set_experience(100)
        self.assertEqual(recipe.get_experience(), 100)

    def test_smelting_recipe(self):
        sr = SmeltingRecipe()

        self.__test_smelting_recipe__(sr)

        sr.write('test files/smelting_recipe.json')


    def test_blasting_recipe(self):
        br = BlastingRecipe()

        self.__test_smelting_recipe__(br)

        br.write('test files/blasting_recipe.json')


    def test_smoking_recipe(self):
        sr = SmokingRecipe()

        self.__test_smelting_recipe__(sr)

        sr.write('test files/smoking_recipe.json')


    def test_campfire_recipe(self):
        cr = CampfireRecipe()

        self.__test_smelting_recipe__(cr)

        cr.write('test files/campfire_recipe.json')


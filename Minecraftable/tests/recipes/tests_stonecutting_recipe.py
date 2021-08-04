from django.test import TestCase

from Minecraftable.recipes.stonecutting_recipe import StonecuttingRecipe


class SmeltingRecipeTest(TestCase):

    def test_stonecutting_recipe(self):
        sr = StonecuttingRecipe()

        sr.add_ingredient_by_item('granite')
        sr.add_ingredient_by_tag('leaves')

        sr.add_ingredient_by_item('stone')
        sr.remove_ingredient_by_item('stone')

        sr.add_ingredient_by_tag('stone')
        sr.remove_ingredient_by_tag('stone')

        sr.set_result('grass_block')
        sr.set_result_count(3)

        sr.write('test files/stonecutting_recipe.json')
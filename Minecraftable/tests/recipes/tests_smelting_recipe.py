from django.test import TestCase

from Minecraftable.recipes.smelting_recipe import SmeltingRecipe, BlastingRecipe, SmokingRecipe, CampfireRecipe


class SmeltingRecipeTest(TestCase):

    def test_smelting_recipe(self):
        sr = SmeltingRecipe()

        sr.add_ingredient_by_item('granite')
        sr.add_ingredient_by_tag('leaves')

        sr.add_ingredient_by_item('stone')
        sr.remove_ingredient_by_item('stone')

        sr.add_ingredient_by_tag('stone')
        sr.remove_ingredient_by_tag('stone')

        sr.set_result('grass_block')
        sr.set_cooking_time_in_seconds(2)
        sr.set_experience(100)

        sr.write('test files/smelting_recipe.json')

    def test_blasting_recipe(self):
        br = BlastingRecipe()

        br.add_ingredient_by_item('granite')
        br.add_ingredient_by_tag('leaves')

        br.add_ingredient_by_item('stone')
        br.remove_ingredient_by_item('stone')

        br.add_ingredient_by_tag('stone')
        br.remove_ingredient_by_tag('stone')

        br.set_result('grass_block')
        br.set_experience(100)

        br.write('test files/blasting_recipe.json')

    def test_smoking_recipe(self):
        sr = SmokingRecipe()

        sr.add_ingredient_by_item('granite')
        sr.add_ingredient_by_tag('leaves')

        sr.add_ingredient_by_item('stone')
        sr.remove_ingredient_by_item('stone')

        sr.add_ingredient_by_tag('stone')
        sr.remove_ingredient_by_tag('stone')

        sr.set_result('grass_block')
        sr.set_experience(100)

        sr.write('test files/smoking_recipe.json')

    def test_campfire_recipe(self):
        cr = CampfireRecipe()

        cr.add_ingredient_by_item('granite')
        cr.add_ingredient_by_tag('leaves')

        cr.add_ingredient_by_item('stone')
        cr.remove_ingredient_by_item('stone')

        cr.add_ingredient_by_tag('stone')
        cr.remove_ingredient_by_tag('stone')

        cr.set_result('grass_block')
        cr.set_experience(100)

        cr.write('test files/campfire_recipe.json')


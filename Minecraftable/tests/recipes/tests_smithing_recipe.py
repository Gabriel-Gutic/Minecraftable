from django.test import TestCase

from Minecraftable.recipes.smithing_recipe import SmithingRecipe


class SmithingRecipeTest(TestCase):

    def test_smithing_recipe_with_item(self):
        sr = SmithingRecipe()

        sr.set_base_by_item('iron_pickaxe')
        sr.set_addition_by_item('diamond')

        sr.set_result('diamond_pickaxe')

        sr.write('test files/smithing_recipe_with_item.json')

    def test_smithing_recipe_with_tag(self):
        sr = SmithingRecipe()

        sr.set_base_by_tag('leaves')
        sr.set_addition_by_tag('anvil')

        sr.set_result('diamond_pickaxe')

        sr.write('test files/smithing_recipe_with_tag.json')
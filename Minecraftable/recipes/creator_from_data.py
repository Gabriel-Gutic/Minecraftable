import json

from Minecraftable.printer.error import print_error

from .crafting_recipe import CraftingRecipeShapeless, CraftingRecipeShaped
from .smelting_recipe import SmeltingRecipe, BlastingRecipe, SmokingRecipe, CampfireRecipe
from .smithing_recipe import SmithingRecipe
from .stonecutting_recipe import StonecuttingRecipe

from Minecraftable.models import Recipe, Datapack, Item, Tag


def create_from_data(name : str, recipe_type, recipe_list, result : str, datapack_id : int):
    if recipe_type == "crafting_shapeless":
        recipe = CraftingRecipeShapeless()

        for element in recipe_list:
            if element is not None and element != '':
                element_type, element_id = element.split('~')

                if element_type == 'item':
                    recipe.add_item_as_ingredient(Item.objects.get(id=element_id).id_name)
                elif element_type == 'tag':
                     recipe.add_tag_as_ingredient(Tag.objects.get(id=element_id).name)
                else:
                    print_error("Unknown element type: " + element_type)
                    return None
        
        result_type, result_id = result.split('~')
        if result_type != 'item':
            print_error("Result must be item!")
            return None
        recipe.set_result(Item.objects.get(id=result_id).id_name)
        #TODO: deal with result count
        recipe_instance = Recipe.objects.create(
            name=name,
            json_data=recipe.get_json_data(),
            datapack= Datapack.objects.get(id=datapack_id)
        )
        recipe_instance.save()


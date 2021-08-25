import json

from Minecraftable.printer import print_error, print_info

from .crafting_recipe import CraftingRecipeShapeless, CraftingRecipeShaped
from .smelting_recipe import SmeltingRecipe, BlastingRecipe, SmokingRecipe, CampfireRecipe
from .smithing_recipe import SmithingRecipe
from .stonecutting_recipe import StonecuttingRecipe

from Minecraftable.models import Recipe, Datapack, Item, Tag


#Create a recipe from the data got from the webapp
def create_from_data(recipe_id : int, name : str, recipe_type, recipe_list, result : str, result_count : str, datapack_id : int):
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
    elif recipe_type == "crafting_shaped":
        recipe = CraftingRecipeShaped()

        i = 0
        for element in recipe_list:
            if element is not None and element != '':
                element_type, element_id = element.split('~')

                if element_type == 'item':
                    id_name = Item.objects.get(id=element_id).id_name
                else:
                    id_name = Tag.objects.get(id=element_id).name
                
                recipe.add_value(element_type + '~' + id_name, int(i / 3), i % 3)
            i += 1
    result_type, result_id = result.split('~')
    if result_type != 'item':
        print_error("Result must be item!")
        return None
    recipe.set_result(Item.objects.get(id=result_id).id_name)
    recipe.set_result_count(result_count)

    if recipe_id == -1: #Create new recipe_instance
        message = 'created'
        recipe_instance = Recipe.objects.create(
            name=name,
            json_data=recipe.get_json_data(),
            datapack=Datapack.objects.get(id=datapack_id)
        )
    else: #Modify existing recipe_instance
        message = 'updated'
        recipe_instance = Recipe.objects.get(id=recipe_id)
        recipe_instance.name = name
        recipe_instance.json_data = recipe.get_json_data()
    recipe_instance.save()
    print_info("Recipe %s from the datapack %s successfully %s!" % (recipe_instance, recipe_instance.datapack, message) )


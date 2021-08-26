import json

from Minecraftable.printer import print_error, print_info

from .crafting_recipe import CraftingRecipeShapeless, CraftingRecipeShaped
from .smelting_recipe import SmeltingRecipe, BlastingRecipe, SmokingRecipe, CampfireRecipe
from .smithing_recipe import SmithingRecipe
from .stonecutting_recipe import StonecuttingRecipe

from Minecraftable.models import Recipe, Datapack, Item, Tag, GetElementTypeAndName


#Create a recipe from the data got from the webapp
def create_from_data(recipe_id : int, name : str, recipe_type, recipe_list, result : str, datapack_id : int):
    result_count = None
    if recipe_type == "crafting_shapeless" or recipe_type == "crafting_shaped" or recipe_type == "campfire_cooking":
        result, result_count = result.split('!')
    
    if recipe_type == "crafting_shapeless":
        recipe = CraftingRecipeShapeless()

        for element in recipe_list:
            if element is not None and element != '':
                recipe.add_ingredient(GetElementTypeAndName(element))
    elif recipe_type == "crafting_shaped":
        recipe = CraftingRecipeShaped()

        i = 0
        for element in recipe_list:
            if element is not None and element != '':

                recipe.add_value(GetElementTypeAndName(element), int(i / 3), i % 3)
            i += 1
    elif recipe_type == "smithing":
        recipe = SmithingRecipe()
        type_name = GetElementTypeAndName(recipe_list[0])
        recipe.set_base(type_name)

        type_name = GetElementTypeAndName(recipe_list[1])
        recipe.set_addition(type_name)

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


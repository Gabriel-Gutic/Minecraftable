import json

from Minecraftable.printer import print_error, print_info

from .crafting_recipe import CraftingRecipeShapeless, CraftingRecipeShaped
from .smelting_recipe import SmeltingRecipe, BlastingRecipe, SmokingRecipe, CampfireRecipe
from .smithing_recipe import SmithingRecipe
from .stonecutting_recipe import StonecuttingRecipe

from Minecraftable.models import Recipe, Datapack, Item, GetElementTypeAndName


#Create a recipe from the data got from the webapp
#result format: type~id!other_attrs
def create_from_data(recipe_id : int, name : str, recipe_type, recipe_list, result : str, datapack_id : int):
    result_count = None
    if recipe_type in {"crafting_shapeless", "crafting_shaped", "stonecutting"}:
        result, result_count = result.split('!')
    elif recipe_type in {"smelting", "blasting", "smoking"}:
        result, timer, xp = result.split('!')
    
    if recipe_type == "crafting_shapeless":
        recipe = CraftingRecipeShapeless()

        for element in recipe_list:
            if element is not None and element != '':
                recipe.add_ingredient(GetElementTypeAndName(data=element))
    elif recipe_type == "crafting_shaped":
        recipe = CraftingRecipeShaped()

        i = 0
        for element in recipe_list:
            if element is not None and element != '':
                type_, name_ = GetElementTypeAndName(data=element)
                recipe.add_value(type_, name_, int(i / 3), i % 3)
            i += 1
    elif recipe_type == "smithing":
        recipe = SmithingRecipe()
        type_, name_ = GetElementTypeAndName(data=recipe_list[0])
        recipe.set_base(type_, name_)

        type_, name_ = GetElementTypeAndName(data=ecipe_list[1])
        recipe.set_addition(type_, name_)
    elif recipe_type == "smelting":
        recipe = SmeltingRecipe()
    elif recipe_type == "smoking":
        recipe = SmokingRecipe()
    elif recipe_type == "blasting":
        recipe = BlastingRecipe()
    elif recipe_type == "stonecutting":
        recipe = StonecuttingRecipe()
        for type_id in recipe_list:
            type_, name_ = GetElementTypeAndName(data=type_id)
            recipe.add_ingredient(type_, name_)
    elif recipe_type == "campfire_cooking":
        recipe = CampfireRecipe()
        result, timer = result.split('!')

        for type_id in recipe_list:
            type_, name_ = GetElementTypeAndName(data=type_id)
            recipe.add_ingredient(type_, name_)

        recipe.set_cooking_time_in_seconds(int(timer))
    
    if recipe_type in {"smelting", "smoking", "blasting"}:
        for type_id in recipe_list:
            type_, name_ = GetElementTypeAndName(data=type_id)
            recipe.add_ingredient(type_, name_)
        recipe.set_cooking_time_in_seconds(int(timer))
        recipe.set_experience(int(xp))

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


import json

from .crafting_recipe import CraftingRecipeShapeless, CraftingRecipeShaped
from .smelting_recipe import SmeltingRecipe, BlastingRecipe, SmokingRecipe, CampfireRecipe
from .smithing_recipe import SmithingRecipe
from .stonecutting_recipe import StonecuttingRecipe

def create_recipe_from_json(self, json_data):
    dictionary = json.loads(json_data)

    if 'type' not in dictionary:
        return None
    else:
        type = dictionary['type']
        if type == 'crafting_shapeless':
            recipe = CraftingRecipeShapeless()
        elif type == 'crafting_shaped':
            recipe = CraftingRecipeShaped()
        elif type == 'smelting':
            recipe = SmeltingRecipe()
        elif type == 'blasting':
            recipe = BlastingRecipe()
        elif type == 'smoking':
            recipe = SmokingRecipe()
        elif type == 'campfire_cooking':
            recipe = CampfireRecipe()
        elif type == 'smithing':
            recipe = SmithingRecipe()
        elif type == 'stonecutting':
            recipe = StonecuttingRecipe()
        else:
            return None
    
    if 'group' in dictionary:
        recipe.set_group(dictionary['group'])
    
    recipe.fill_data_from_dictionary(dictionary)
    return recipe
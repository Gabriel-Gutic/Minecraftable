
def get_matrix_from_request_post(request_post, matrix_name : str):
    recipe = []
    i = 0
    key = matrix_name + "[" + str(i) + "][]"
    while key in request_post:
        recipe.append(request_post.getlist(key))
        i += 1
        key = matrix_name + "[" + str(i) + "][]"
    
    return recipe

def next_alpha(s):
    return chr((ord(s.upper()) + 1 - 65) % 26 + 65)

def first_from_dict(dict):
    items_view = dict.items()
    value_iterator = iter(items_view)
    return next(value_iterator)  
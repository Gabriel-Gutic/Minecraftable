
def get_matrix_from_request_post(request_post, matrix_name : str):
    recipe = []
    i = 0
    key = matrix_name + "[" + str(i) + "][]"
    while key in request_post:
        recipe.append(request_post.getlist(key))
        i += 1
        key = matrix_name + "[" + str(i) + "][]"
    
    return recipe

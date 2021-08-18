from django import template

register = template.Library()

@register.filter()
def to_int(value):
    if type(value) is list:
        new_list = []
        for i in range(len(value)):
            new_list.append(int(value[i]))
        return new_list
    return int(value)


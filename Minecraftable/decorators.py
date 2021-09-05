from django.shortcuts import redirect

from .models import Datapack, Tag


def datapack_owned():
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            user = request.user

            datapack_id = kwargs.get('datapack_id')
            try:
                datapack = Datapack.objects.get(id=datapack_id)
            except Datapack.DoesNotExist:
                return redirect('/Minecraftable/datapack/not-exist/') 

            if datapack.user == user or user.is_staff:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('/Minecraftable/not-permission/')
            
        return wrapper_func
    return decorator


def tag_owned():
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            user = request.user

            tag_id = kwargs.get('tag_id')
            try:
                tag = Tag.objects.get(id=tag_id)
            except Tag.DoesNotExist:
                return redirect('/Minecraftable/tag/not-exist/') 

            if tag.user == user or user.is_staff:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('/Minecraftable/not-permission/')
            
        return wrapper_func
    return decorator


def login_required():
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            user = request.user

            if not user.is_authenticated:
                return redirect('/Minecraftable/login/') 
            return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator

def login_not_required():
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            user = request.user

            if user.is_authenticated:
                return redirect('/Minecraftable/home/') 
            return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator
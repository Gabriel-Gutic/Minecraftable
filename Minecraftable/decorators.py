from django.shortcuts import redirect

from .models import Datapack


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
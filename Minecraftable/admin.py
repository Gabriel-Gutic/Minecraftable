from django.contrib import admin

from . import models

admin.site.register(models.User)
admin.site.register(models.Client)

admin.site.register(models.Datapack)
admin.site.register(models.Recipe)
admin.site.register(models.Tag)
admin.site.register(models.Item)

EMAIL_ADMIN = 'minecraftable-admin@gmail.com'
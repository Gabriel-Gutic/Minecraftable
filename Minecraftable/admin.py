from django.contrib import admin

from . import models

admin.site.register(models.User)

admin.site.register(models.Datapack)
admin.site.register(models.Recipe)
admin.site.register(models.Tag)
admin.site.register(models.Item)
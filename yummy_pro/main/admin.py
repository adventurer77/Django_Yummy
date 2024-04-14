from django.contrib import admin
from .models import DishCategory,Events,Personnel


# Register your models here.

admin.site.register(DishCategory)

admin.site.register(Events)
admin.site.register(Personnel)

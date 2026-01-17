from django.contrib import admin

from .models import Category, Thing, MetroStation

admin.site.register(Category)
admin.site.register(Thing)
admin.site.register(MetroStation)

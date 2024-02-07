from django.contrib import admin
from .models import Plan, Attribute, User, Screen, Menu
from _panel.models import Category, CategoryAdmin
# Register your models here.
admin.site.register([User, Screen, Plan, Attribute])

admin.site.register(Category, CategoryAdmin)


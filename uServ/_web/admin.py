from django.contrib import admin
from .models.common import menu_model, screen_model 
from .models.user import User

# Register your models here.
admin.site.register([User.User, menu_model.Menu, screen_model.Screen])
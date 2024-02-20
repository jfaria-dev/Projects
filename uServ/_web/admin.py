from django.contrib import admin
from .models import Plan, Attribute, User, Screen, Menu, SupplierDetails
from _panel.models import Category, CategoryAdmin, UnitForService
# Register your models here.
admin.site.register([User, Screen, Plan, Attribute, SupplierDetails, UnitForService])

admin.site.register(Category, CategoryAdmin, )


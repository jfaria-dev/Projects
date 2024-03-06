from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from _auth.models import UserAuth
from _web.models import Plan, Attribute, User, Screen, Menu, SupplierDetails
from _panel.models import Category, CategoryAdmin, UnitForService


class UserAdmin(UserAdmin):
    list_display = ('email', 'is_staff', 'is_active')
    ordering = ['email']
admin.site.register(UserAuth, UserAdmin)

admin.site.register([User, Screen, Plan, Attribute, SupplierDetails, UnitForService])
admin.site.register(Category, CategoryAdmin, )


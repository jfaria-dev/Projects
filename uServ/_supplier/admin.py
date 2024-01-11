from django.contrib import admin


from _supplier.models import Supplier, SupplierUser, Plan
from _dashboard.models import Category, Unity
# Register your models here.
admin.site.register([Supplier, SupplierUser, Plan, Category, Unity])
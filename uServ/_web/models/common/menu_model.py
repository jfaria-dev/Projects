# create a model for all menus that will be access for each screen

from django.db import models
from _web.models import SupplierUser
from .screen_model import Screen

class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    screen = models.ForeignKey(Screen, related_name='menu_screen', on_delete=models.SET_NULL, null=True, blank=True)
    action = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    created_by = models.ForeignKey(SupplierUser, related_name='menu_created_by', on_delete=models.SET_NULL, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(SupplierUser, related_name='menu_modified_by', on_delete=models.SET_NULL, null=True, blank=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = '_web'
        db_table = 'web_menu'
        verbose_name_plural = 'menus'
        ordering = ('name',)

    def __unicode__(self):
        return self.name


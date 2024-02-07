# create a model for all screens in the system for access control

from django.db import models
from datetime import datetime

class Screen(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    namespace = models.CharField(max_length=100, default='user')
    url = models.CharField(max_length=100)
    
    title = models.CharField(max_length=200, null=True, blank=True)
    paragraph = models.CharField(max_length=400, null=True, blank=True)
    
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(default= datetime.now())
    modified_on = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} - "{self.url}"'
    
    def content(request):
        print('request.path: ', request.path)
        path = str(request.path)
        if path.startswith('/'):
            path = path[1:]
        aux = Screen.objects.get(url=path)
        return {
                'title': aux.title,
                'paragraph': aux.paragraph
            }

    class Meta:
        app_label = '_web'
        db_table = 'web_screen'
        verbose_name_plural = 'screens'
        ordering = ('name',)

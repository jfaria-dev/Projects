from django.db import models

class State(models.Model):
    state = models.CharField(max_length=2)
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
    class Meta:
        app_label = '_web'
        db_table = 'state'
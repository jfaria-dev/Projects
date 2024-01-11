from django.utils.translation import gettext_lazy as _
from ..models import Unity
from django import forms

class UnityForm(forms.ModelForm):  
    class Meta:
        model = Unity
        fields=[
            'unit'
        ]
        labels = {
            'unit': _('Unidade:')
        }
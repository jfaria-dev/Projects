from django import forms
from django.utils.translation import gettext_lazy as _
from ..models import Team

class TeamForm(forms.ModelForm):  
    class Meta:
        model = Team
        fields = [
            'name',
            'description',
            'active',
            'photo'
        ]
        widgets = {
          'description': forms.Textarea(attrs={'rows':3,}),
        }
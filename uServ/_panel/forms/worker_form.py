from django import forms
from _panel.models import Worker

class WorkerForm(forms.ModelForm):
    employment_date = forms.DateField(input_formats=['%d/%m/%Y'], widget=forms.DateInput(format='%d/%m/%Y', attrs={'placeholder': 'dd/MM/aaaa'}))
    class Meta:
        model = Worker
        fields = [
            'name',
            'document',
            'position',
            'employment_date',
            'photo',
            'active'
        ]
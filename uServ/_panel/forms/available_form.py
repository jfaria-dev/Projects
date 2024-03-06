from django import forms
from _panel.models import AvailableTime

class AvailableForm(forms.ModelForm):
    # day_of_week = forms.ChoiceField( label=None)    
    class Meta:
        model = AvailableTime
        fields = [
            'day_of_week',
            'open_time',
            'close_time'
        ]
    
    def __init__(self, *args, supplier=None, **kwargs):
        super().__init__(*args, **kwargs)
        # Obtém todos os dias da semana
        all_days_of_week = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
        # Obtém os dias já cadastrados no modelo AvailableTime
        used_days_of_week = supplier.available_times.values_list('day_of_week', flat=True)
        # Remove os dias já cadastrados da lista de dias da semana
        available_days_of_week = [day for day in all_days_of_week if day not in used_days_of_week]
        # Atualiza as escolhas do campo day_of_week
        self.fields['day_of_week'].choices = [(day, day) for day in available_days_of_week]

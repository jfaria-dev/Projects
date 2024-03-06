from django import forms
from _web.models import UserCart
from _panel.models import Worker, AvailableTime

class UserCartForm(forms.ModelForm):
    class Meta:
        model = UserCart
        fields = [
            'quantity',
            'service',
            'worker',
            'date',
            'time',
            'value',
        ]
    
    def __init__(self,  *args, service=None, **kwargs):
        # Preenche o campo 'service' com o serviço padrão
        kwargs.setdefault('initial', {})
        kwargs['initial']['service'] = service
        super().__init__(*args, **kwargs)
        self.fields['worker'].queryset = service.workers.filter(active=True)     
        
    def clean(self):
        cleaned_data = super(UserCartForm, self).clean()
        # print(cleaned_data)
        # Verifica se o campo 'time' está vazio ou '---------'
        if cleaned_data.get('time') in ('', None):
            # Define o campo 'time' como None para indicar que está vazio
            self.cleaned_data['time'] = None

        return cleaned_data
        
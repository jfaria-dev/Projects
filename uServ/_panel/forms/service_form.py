from django import forms
from django.utils.translation import gettext_lazy as _
from _panel.models import Service, UnitForService, GeneralService, Team, Worker

GEEKS_CHOICES =( 
    ("Minutos", "Minutos"), 
    ("Horas", "Horas") ,
    ("Dias", "Dias") ,
    ("Meses", "Meses") 
) 

class ServiceForm(forms.ModelForm):     
    unit_of_execution = forms.ChoiceField(choices=GEEKS_CHOICES, widget=forms.Select, label="---------")
    price = forms.DecimalField(max_digits=10, decimal_places=2, localize=True, widget=forms.NumberInput(attrs={'type': 'currency'}))
    class Meta:
        model = Service
        fields = [
            'general_service', 
            'price', 
            'unit_for_service',
            'execution_time',
            'unit_of_execution', 
            'service_image', 
            'requirements',
            'active',
            'team',
            'workers'
            ]
        exclude = ['warranty', 'delivery_time']
        labels = {
            'general_service': _('Serviço:'),
            'price': _('Valor:'),			
            'service_image': _('Imagem:'),	
            'requirements': _('Exigências para Execução:'),	
            'active': _('Ativo:')
        }
        widgets = {
          'requirements': forms.Textarea(attrs={'rows':2,}),
          'execution_time': forms.NumberInput(attrs={'placeholder': 'Ex: 99', 'step': 0.50}),
        #   'workers': forms.CheckboxSelectMultiple(),
          'unit_of_execution': forms.NumberInput(attrs={'placeholder': 'Ex: horas, dias...'}),
        }
    
    def __init__(self, *args, supplier=None, **kwargs, ):
        super().__init__(*args, **kwargs)
        self.fields['price'].decimal_places = 2
        self.fields['unit_for_service'].queryset = UnitForService.objects.none()
        self.fields['general_service'].queryset = GeneralService.objects.none()
        self.fields['workers'].queryset = Worker.objects.none()   
        if supplier:
            self.fields['team'].queryset = supplier.teams.filter(active=True)                
        else:
            self.fields['team'].queryset = Team.objects.none()
        
        
        print(self.data.get('general_service'))
        print(self.data.get('unit_for_service'))
        print(self.instance)
        try:
            if 'general_service' in self.data:
                gs_id = int(self.data.get('general_service'))
                self.fields['general_service'].queryset = GeneralService.objects.filter(id=gs_id)
            if 'unit_for_service' in self.data:
                unit_id = int(self.data.get('unit_for_service'))
                self.fields['unit_for_service'].queryset = UnitForService.objects.filter(id=unit_id)   
            if 'team' in self.data:
                team_id = int(self.data.get('team'))
                self.fields['workers'].queryset = Worker.objects.filter(team_id=team_id, active=True).order_by('name')            
                
            if self.instance.pk:
                category_id = self.instance.general_service.category.id
                gs_id = self.instance.general_service.id                
                self.fields['general_service'].queryset = GeneralService.objects.filter(category_id=category_id).order_by('description')
                self.fields['unit_for_service'].queryset = UnitForService.objects.filter(general_service_id=gs_id).order_by('name')
                if self.instance.team:
                    team_id = self.instance.team.id
                    self.fields['workers'].queryset = Worker.objects.filter(team_id=team_id, active=True).order_by('name')  
            
        except (ValueError, TypeError):
            pass  # invalid input from the client; ignore and fallback to empty City queryset
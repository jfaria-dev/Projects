from django.utils.translation import gettext_lazy as _
from _web.models import SupplierDetails
from _panel.models import Category
from django import forms

GEEKS_CHOICES =( 
    ("CNPJ", "CNPJ"), 
    ("CPF", "CPF") 
) 

# register a new supplier
class SupplierDetailsForm(forms.ModelForm): 
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['segment'] = forms.ModelChoiceField(queryset=Category.objects.filter(parent__isnull=True, active=True))
           
    document_type = forms.ChoiceField(choices=GEEKS_CHOICES, widget=forms.Select, label="Tipo de Documento")
    birthdate = forms.DateField(input_formats=['%d/%m/%Y'], widget=forms.DateInput(format='%d/%m/%Y', attrs={'placeholder': 'dd/mm/aaaa'}))
    
    class Meta:
        model = SupplierDetails
        fields = [
            'document_type', 
            'company_document_number', 
            'birthdate',
            'company_name', 
            'company_name_show', 
            'owner_document_number',
            'segment',
            'term',
            'photo',
            'cnd'
            ]        
        labels = {  
            'document_type': _('Tipo de Documento'),                             
            'company_document_number': _('CNPJ'),
            'company_name': _('Nome da Empresa'),
            'company_name_show': _(''),
            'owner_name': _('Nome Completo'),
            'owner_document_number': _('Documento do Representante (CPF)'),
            'segment': _('Segmento de Atuação'), # 'Segmento de Atuação
            'term': _('Termo de Uso e Política de Privacidade'),
            'photo': _('Logo ou Foto da Empresa'),
            'cnd': _('Certidão Negativa de Débitos (CND)'),
        } 
        widgets = {
            'company_document_number': forms.TextInput(attrs={'placeholder': '00.000.000/0000-00'}),
            'company_name': forms.TextInput(attrs={
                'placeholder': 'Informe o número do documento primeiro', 
                'disabled': 'disabled', 
                }),
            'birthdate': forms.DateInput(attrs={'placeholder': 'dd/mm/aaaa'}),
            'owner_document_number': forms.TextInput(attrs={'placeholder': '000.000.000-00'}),            
            'company_name_show': forms.TextInput(attrs={'placeholder': 'ex: Mercado do João ou Nome Fantasia'}),            
            'term': forms.CheckboxInput(attrs={'required': 'required'}),   
                 
        }
       
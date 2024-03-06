from datetime import datetime
from itertools import cycle
import re
from django.db import models
from django.forms import ValidationError

class Worker(models.Model):
    
    def get_ById(id):
        return Worker.objects.filter(id=id).first()
    
    def get_available_dates(self):
        return self.orders.filter(date__month=datetime.now().month)
    
    def worker_image_path(instance, filename):
    # Cria um caminho baseado no ID do fornecedor e no nome do arquivo
        url = f"supplier/{instance.team.supplier.id}/team/{instance.team.id}/workers/{filename}"
        print(url)
        return url
    
    def company_document_is_valid(value :str):  
        """Verify if numbers of document is valid. CPF or CNPJ

        Args:
            document (document): value of company_document_number

        Raises:
            ValidationError: if not inform all numbers
            ValidationError: if not inform only numbers
            ValidationError: if number is invalid
        """
        if value is None:
            return
        value = re.sub(r'\D', '', value)
        if len(value) not in [11, 14]:
            raise ValidationError("Documento inválido, informe todos os números.")        
        if value in (c * len(value) for c in "1234567890"):
            raise ValidationError("Documento inválido, informe apenas números") 
        value_reverse = value[::-1]        
        for i in range(2, 0, -1):            
            if len(value) == 14:
                document_enum = zip(cycle(range(2, 10)), value_reverse[i:])
            else:
                document_enum = enumerate(value_reverse[i:], start=2)            
            dv = sum(map(lambda x: int(x[1]) * x[0], document_enum)) * 10 % 11
            if value_reverse[i - 1:i] != str(dv % 10):
                raise ValidationError("Documento inválido.")
    
    def date_is_valid(data_str):
    # Expressão regular para verificar o formato da data
        pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
        
        # Verificar se a string corresponde ao padrão de data esperado
        date = str(data_str)
        print(date)
        if not pattern.match(date):
            print('data fora do formato aaaa-mm-dd')
            raise ValidationError('Data inválida.')
        
        # Tentar converter a string para um objeto datetime
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            print('data nao converteu no formato aaaa-mm-dd')            
            raise ValidationError('Data inválida.')
        
    team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='workers')
    name = models.CharField(max_length=100)
    document = models.CharField(max_length=20, validators=[company_document_is_valid])
    position = models.CharField(max_length=100)
    employment_date = models.DateField(validators=[date_is_valid])
    photo = models.ImageField(upload_to=worker_image_path, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 
    
    class Meta:
        app_label = '_panel'
        db_table = 'worker'
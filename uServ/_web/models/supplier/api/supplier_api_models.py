import re
from datetime import datetime
import requests

def api_get_supplier_information(document_number:str, birthdate=None):
        document_number = re.sub(r'\D', '', document_number)
        print('API CNPJ - document_number: (regex-replace) ', document_number)
        
        if birthdate:           
            date_format = "%Y-%m-%d"
            birthdate = datetime.strptime(birthdate, date_format).strftime('%Y-%m-%d')
            token = 'EIj4Ujz-6aFwxzxwvQWBnidjwTrr_YNaP2DmgdBI'
            url = 'https://api.infosimples.com/api/v2/consultas/receita-federal/cpf'
            args = {
                "cpf":       str(document_number),
                "birthdate": str(birthdate),
                "origem":    "web",
                "token":     token,
                "timeout":   300
            }                    
            response = requests.post(url, args)
            response.close()
        else:
            url = f'https://www.receitaws.com.br/v1/cnpj/{document_number}'  
            response = requests.get(url)   
            response.close()
        data = response.json()
        print('data: ', data)
        return data
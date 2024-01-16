from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

import requests
from ...models import Supplier, SupplierUser, SupplierAddress
from ...models.common.screen_model import Screen
from ...forms.supplier import SupplierForm, AddressForm

# ==================== FUNCTIONS ====================
def _set_screen_content(request):
    """SET SCREEN CONTENT

    Args:
        request (REQUEST): REQUEST FROM BROWSER

    Returns:
        JSON: 
        {
            partial_title: 'title',
            partial_paragraph: 'paragraph'
        }
    """
    content_screen = Screen.content(request=request)
    return {
                'partial_title': content_screen['title'],
                'partial_paragraph': content_screen['paragraph']
            }

def verify_address_exists(company_data, supplier_id):
    address = SupplierAddress.get_bySupplierId(supplier_id)
    if address:
        return AddressForm(company_data, instance=address)
    else:
        return AddressForm(company_data)

def create_user_and_login(request, supplier, password):
    user = SupplierUser.create_user(email=supplier.email, password=password, supplier=supplier)                
    # LOGIN USER                 
    return auth.authenticate(request=request, username=supplier.email, password=password)

# ==================== VIEWS =======================

def home(request):
    context = {
        'content_page': _set_screen_content(request)
    }    
    return render(request, 'supplier/index.html', context= context)

def login(request):
    return render(request, 'supplier/login/login.html')

def register(request):
    """Register a new supplier (owner_name, email, phone)

    Args:
        request (request.POST): (owner_name, email, phone)

    Returns:
        Redirect: Document Choice (CPF or CNPJ)
    """
    form = SupplierForm()
    if request.method == 'POST':
        supplier_data = request.POST.copy()  # Create a copy to avoid modifying the original request.POST
        form = SupplierForm(supplier_data)               
        supplier = Supplier.objects.filter(email=supplier_data['email']).first()  # Verify if already exists supplier with this email
        if not supplier:
            if form.is_valid():
                supplier = form.save()
            return redirect('supplier:document_choice', supplier.id)        
        else:
            return redirect('supplier:document_choice', supplier.id)    
    context = {
        'form': form,
        'content_page': _set_screen_content(request)
    }
    return render(request, 'supplier/register/register.html', context=context)

def get_company_from_document(request):
    """Get the information about the company from the document number

    Args:
        request (string): number of document from the company

    Returns:
        Json: 
        {
            "abertura": "11/11/2019",
            "situacao": "ATIVA",
            "tipo": "MATRIZ",
            "nome": "JFARIA ASSESSORIA E CONSULTORIA LTDA",
            "fantasia": "JFARIA CONSULTORIA",
            "porte": "MICRO EMPRESA",
            "natureza_juridica": "206-2 - Sociedade Empresária Limitada",
            "atividade_principal": [
                {
                    "code": "70.20-4-00",
                    "text": "Atividades de consultoria em gestão empresarial"
                }
            ],
            "logradouro": "RUA SERGIPE",
            "numero": "661",
            "complemento": "LOTE 6 QUADRA241",
            "municipio": "FRANCISCO BELTRAO",
            "bairro": "ALVORADA",
            "uf": "PR",
            "cep": "85.601-040",
            "telefone": "(46) 3538-1270",
            "data_situacao": "21/11/2016",
            "cnpj": "26.576.146/0001-73",
            "ultima_atualizacao": "2023-12-09T23:59:59.000Z",
            "status": "OK",
            "email": "",
            "efr": "",
            "motivo_situacao": "",
            "situacao_especial": "",
            "data_situacao_especial": "",
            "capital_social": "60000.00",
        }
    """

    company_document_number = request.GET.get('company_document_number')
    url = f'https://www.receitaws.com.br/v1/cnpj/{company_document_number}'  
    response = requests.get(url)   
    data = response.json()
    return JsonResponse(data)

def get_professional_from_document(request):
    """Get the information about the professional from the document number and birthdate

    Args:
        request (_type_): _description_

    Returns:
        JSON: 
            {
                "code": 200,
                "code_message": "A requisição foi processada com sucesso.",
                "header": {
                    "api_version": "v2",
                    "api_version_full": "2.2.16-20240113081702",
                    "product": "Consultas",
                    "service": "receita-federal/cpf",
                    "parameters": {
                    "birthdate": "1985-12-14",
                    "cpf": "07921263607",
                    "origem": "web"
                    },
                    "client_name": "Jackson Faria Da Silva",
                    "token_name": "Jackson Faria Da Silva",
                    "billable": true,
                    "price": "0.24",
                    "requested_at": "2024-01-15T00:29:44.000-03:00",
                    "elapsed_time_in_milliseconds": 6962,
                    "remote_ip": "179.83.57.132",
                    "signature": "U2FsdGVkX18lVKOlzeQasBG5iMP319sTcp2v8N3X8oIL2vdXQhxUjFc0XhVKzFEUiVZedUJ1LGTgD/ih7a5wHQ=="
                },
                "data_count": 1,
                "data": [
                    {
                    "ano_obito": null,
                    "consulta_comprovante": "709D.BD86.8D13.505A",
                    "consulta_datahora": "15/01/2024 00:29:42",
                    "consulta_digito_verificador": "00",
                    "cpf": "079.212.636-07",
                    "data_inscricao": "04/12/2003",
                    "data_nascimento": "14/12/1985",
                    "nome": "JACKSON FARIA DA SILVA",
                    "nome_civil": "",
                    "nome_social": "",
                    "normalizado_ano_obito": 0,
                    "normalizado_consulta_datahora": "15/01/2024 00:29:42",
                    "normalizado_cpf": "07921263607",
                    "normalizado_data_inscricao": "04/12/2003",
                    "normalizado_data_nascimento": "14/12/1985",
                    "origem": "web",
                    "qrcode_url": "https://servicos.receita.fazenda.gov.br/Servicos/CPF/ca/ResultadoAut.asp?cp=07921263607&cc=709DBD868D13505A&de=15012024&he=002942&dv=00&em=01",
                    "situacao_cadastral": "REGULAR",
                    "site_receipt": "https://storage.googleapis.com/infosimples-api-tmp/api/receita-federal/cpf/20240115002943/rDjfpphdtw6hIE6oLVk7knDJUq11TB66/455ec6b0c8218ffb893aaee088d77874_0_Sis.html"
                    }
                ],
                "errors": [],
                "site_receipts": [
                    "https://storage.googleapis.com/infosimples-api-tmp/api/receita-federal/cpf/20240115002943/rDjfpphdtw6hIE6oLVk7knDJUq11TB66/455ec6b0c8218ffb893aaee088d77874_0_Sis.html"
                ]
            }

    """
    professional_document_number = request.GET.get('company_document_number')
    professional_birthdate = request.GET.get('professional_birthdate')
    print('professional_birthdate: ', professional_birthdate)
    token = 'EIj4Ujz-6aFwxzxwvQWBnidjwTrr_YNaP2DmgdBI'
    # url = f'https://api.infosimples.com/api/v2/consultas/receita-federal/cpf?token={token}&cpf={professional_document_number}&birthdate={professional_birthdate}&origem=web'
    url = 'https://api.infosimples.com/api/v2/consultas/receita-federal/cpf'
    args = {
        "cpf":       str(professional_document_number),
        "birthdate": str(professional_birthdate),
        "origem":    "web",
        "token":     token,
        "timeout":   300
    }
    response = requests.post(url, args)
    response_json = response.json()
    response.close()
    if response_json['code'] != 200:
        raise JsonResponse('Dados inválidos')
    
    return JsonResponse(response_json['data'][0])
    
def get_address_from_postal_code(request): 
    """Get the address from the postal code through the BrasilAPI: 
        "https://brasilapi.com.br/api/cep/v2/{postal_code}"  
    Args:
        request (string): postal code of the address

    Returns:
        Json: 
            {
                "cep": "01001000",
                "state": "SP",
                "city": "São Paulo",
                "neighborhood": "Sé",
                "street": "Praça da Sé - lado ímpar",
                "service": "correios-alt",
                "location": {
                    "type": "Point",
                    "coordinates": {        
                    }
            }
    """
    postal_code = request.GET.get('postal_code')
    url = f"https://brasilapi.com.br/api/cep/v2/{postal_code}"  
    response = requests.get(url)    
    data = response.json()
    print('d: ', data)    
    return JsonResponse( data)

def document_choice(request, supplier_id):
    """Choice what kind is the company (company or personal)

    Args:
        request (_type_): Request
        supplier_id (_type_): Supplier Id created by register function

    Returns:
        _type_: _description_
    """
    choice = request.GET.get('choice')
    
    if choice:
        if choice == 'CPF':
            return redirect('supplier:service_professional', supplier_id)
        return redirect('supplier:company', supplier_id)
    
    supplier = Supplier.get_byId(supplier_id)
    context = {
        'supplier': supplier,
    }
    return render(request, 'supplier/register/document-choice.html', context= context)

def company(request, supplier_id):
    """Create a new company, address and user to login

    Args:
        request (request): Browser request
        supplier_id (int): Id from Supplier created by register function

    Returns:
        Redirect: Sign Plan if all data is valid
    """
    supplier = Supplier.get_byId(supplier_id)
    errors = []
    if request.method == 'POST':
        company_data = request.POST.copy()
        address_form = verify_address_exists(company_data, supplier_id)
        if address_form.is_valid():
            supplier_form = SupplierForm(company_data, instance=supplier)
            if supplier_form.is_valid():
                supplier = supplier_form.save()
                address = address_form.save(commit=False)
                address.supplier = supplier            
                address.save()
                
                # CREATET AND LOGIN USER                 
                user_logged = create_user_and_login(request, username=supplier.email, password=company_data['password'])
                if user_logged is not None:
                    # Realizamos o login automático
                    auth.login(request, user_logged) 
                    return redirect('supplier:sign_plan', supplier_id)
                return redirect('supplier:login')
            errors += supplier_form.errors
        errors += address_form.errors            
    
    context = {
        'supplier': supplier,
        'errors': errors
    }
    return render(request, 'supplier/register/company.html', context=context)

def service_professional(request, supplier_id):
    """Create a new personal worker, address and user to login

    Args:
        request (request): Browser request
        supplier_id (int): Id from Supplier created by register function

    Returns:
        Redirect: Sign Plan if all data is valid
    """
    supplier = Supplier.get_byId(supplier_id)
    errors = []
    if request.method == 'POST':
        personal_data = request.POST.copy()
        address_form = verify_address_exists(personal_data, supplier_id)
        if address_form.is_valid():
            supplier_form = SupplierForm(personal_data, instance=supplier)
            if supplier_form.is_valid():
                supplier = supplier_form.save()
                address = address_form.save(commit=False)
                address.supplier = supplier            
                address.save()
                
                # CREATET AND LOGIN USER                 
                user_logged = create_user_and_login(request, username=supplier.email, password=personal_data['password'])
                if user_logged is not None:
                    # Realizamos o login automático
                    auth.login(request, user_logged) 
                    return redirect('supplier:sign_plan', supplier_id)
                return redirect('supplier:login')
            errors += supplier_form.errors
        errors += address_form.errors            
    
    context = {
        'supplier': supplier,
        'errors': errors
    }
    return render(request, 'supplier/register/service-professional.html', context=context)

@login_required(login_url='login')
def sign_plan(request, supplier_id):
    return render(request, 'supplier/register/sign-plan.html')
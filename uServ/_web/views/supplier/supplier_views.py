from datetime import datetime, timedelta
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from _utils.decorator import auth_supplier_required

from _web.models import Screen, SupplierOrder, Supplier,  SupplierAddress, SupplierDetails, api_get_supplier_information, Plan, PaymentCard 
from _auth.models import UserAuth
from _panel.models import Category

from _web.forms.supplier import SupplierForm, SupplierAddressForm, SupplierDetailsForm, PaymentForm

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

def _create_user_and_login(request, supplier, password):
    supplier_user = UserAuth.get_ByEmail(supplier.email)
    if not supplier_user:
        user_auth = UserAuth.objects.create_user(email=supplier.email, password=password, is_supplier=True)       
        print(user_auth)      
    # LOGIN USER                 
    return auth.authenticate(request=request, username=supplier.email, password=password)

def _update_csrf_token(request):
    # request.session['csrf_token'] = _add_new_csrf_cookie(request)
    
    return request

def _exists_email(email):
    if Supplier.get_ByEmail(email):        
        return True
    return False

# ==================== AJAX ========================
# AJAX - GET COMPANY INFORMATION FROM DOCUMENT NUMBER
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
    document = request.GET.get('company_document_number')
    if document:
        response = api_get_supplier_information(document) 
        return JsonResponse(response)

# AJAX - GET PROFESSIONAL INFORMATION FROM DOCUMENT NUMBER AND BIRTHDATE
def get_professional_from_document(request):   
    date_format = "%d-%m-%Y"
    print(request.GET.get('birthdate'))
    birthdate = datetime.strptime(request.GET.get('birthdate'), date_format).strftime('%Y-%m-%d')
    document = request.GET.get('document_number')
    # response = api_get_supplier_information(request.GET.get('document_number'), birthdate)
    data_test = {
        "code": 200,
        "code_message": "A requisição foi processada com sucesso.",
        "header": {
            "api_version": "v2",
            "api_version_full": "2.2.12-20230929113629",
            "product": "Consultas",
            "service": "receita-federal/cpf",
            "parameters": {
            "birthdate": "1111-11-11",
            "cpf": "123.456.789-01"
            },
            "client_name": "Minha Empresa",
            "token_name": "Token de Produção",
            "billable": True,
            "price": "0.2",
            "requested_at": "2023-09-29T13:16:10.000-03:00",
            "elapsed_time_in_milliseconds": 127,
            "remote_ip": "111.111.111.111",
            "signature": "U2FsdGVkX1+wRo/rgxRVkfOBcsPsWtK4dXaPpcbGNgRGxl4RsxQqDr0mrnEqONwDb9lrkUKh+fFPSDsnVqvy7g=="
        },
        "data_count": 1,
        "data": [
            {
            "ano_obito": None,
            "consulta_comprovante": "1111.1111.1111.1111",
            "consulta_datahora": "29/09/2023 13:16:08",
            "consulta_digito_verificador": "00",
            "cpf": "123.456.789-01",
            "data_inscricao": "11/11/1111",
            "data_nascimento": "11/11/1111",
            "nome": "Exemplo de Nome",
            "nome_civil": "Exemplo de Nome",
            "nome_social": "Exemplo de Nome",
            "normalizado_ano_obito": 0,
            "normalizado_consulta_datahora": "29/09/2023 13:16:08",
            "normalizado_cpf": "12345678901",
            "normalizado_data_inscricao": "11/11/1111",
            "normalizado_data_nascimento": "11/11/1111",
            "origem": "mobile",
            "qrcode_url": "https://www.exemplo.com/exemplo-de-url",
            "situacao_cadastral": "ATIVA",
            "site_receipt": "https://www.exemplo.com/exemplo-de-url"
            }
        ],
        "errors": [],
        "site_receipts": [
            "https://www.exemplo.com/exemplo-de-url"
        ]
    }
    
    # if response['code'] != 200:
    #     raise JsonResponse({ 'message': 'Dados inválidos' })
    return JsonResponse(data_test['data'][0])
   
# AJAX - GET ADDRESS INFORMATION FROM POSTAL CODE
def get_address_from_postal_code(request):     
    postal_code = request.GET.get('postal_code')
    response = SupplierAddress.api_get_addres_information(postal_code) 
    return JsonResponse( response )

# AJAX - VALIDATE EMAIL IF EXISTS
def validate_email(request):
    email = request.GET.get('email')
    if _exists_email(email):
        return JsonResponse({ 
                            'message': 'E-mail já existe.',
                            'exists': True})
    return JsonResponse({ 
                        'message': 'E-mail válido.',
                        'exists': False})
 
# AJAX - GET TYPE OF CREDIT CARD (VISA, MASTERCARD, ETC)
def get_cc_type(request):
    print('request.GET.get(card_number)', request.GET.get('card_number'))
    number = request.GET.get('card_number')
    cc_type = PaymentCard.get_cc_type(number)                       
    print('cc_type', cc_type)
    return JsonResponse({ 'cc_type': cc_type })

# ==================== VIEWS =======================
def home(request):
    # if request.user.is_authenticated:
    #     if request.user.is_client:
    #         auth.logout(request)
    form = SupplierForm()
    context = {
        # 'content_page': _set_screen_content(request),
        'form': form
    }    
    return render(request, 'supplier/index.html', context= context)

def login_supplier(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user_logged = auth.authenticate(request=request, username=email, password=password)
        
        if user_logged is not None and user_logged.is_supplier:
            auth.login(request, user_logged) 
            
            # logica do que falta no registro
            supplier = Supplier.get_ByEmail(email)
            if supplier:
                details = SupplierDetails.get_BySupplierId(supplier.id)
                if details is None:
                    return redirect('supplier:company_details', supplier.id)
                address = SupplierAddress.get_BySupplierId(supplier.id)
                if address is None:
                        return redirect('supplier:company_address', supplier.id)
                else: 
                    orders_valid = SupplierOrder.get_SupplierHasOrderValid(supplier)
                    if orders_valid is None:
                        return redirect('supplier:sign_plan', supplier.id)
                    else:
                        return redirect('panel:home', supplier.id)                  
        else:
            if _exists_email(email):
                messages.success(request, 'Senha inválida.')
            else:
                messages.success(request, 'E-mail inválido.')
            return redirect('supplier:login')  
    
    return render(request, 'supplier/authenticate/login.html')

def logout_supplier(request):
    auth.logout(request)
    return redirect("supplier:home")

# FIRST REGISTER - NAME, EMAIL, PHONE
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
        supplier = _exists_email(supplier_data['email'])  # Verify if already exists supplier with this email
       
        if not supplier:
            if form.is_valid():
                print('form: ', form)
                supplier = form.save()
                
                user_logged = _create_user_and_login(request, supplier=supplier, password=request.POST['password'])
                if user_logged is not None:
                    supplier.user_auth = user_logged
                    supplier.save()
                    auth.login(request, user_logged)
                    return redirect('supplier:company_details', supplier.id)
        
    context = {
        'form': form,
        # 'content_page': _set_screen_content(request)
    }
    return render(request, 'supplier/register/register.html', context=context)

@login_required(login_url='supplier:login')
@auth_supplier_required
def company_details(request, supplier_id):
    supplier = Supplier.get_ById(supplier_id)
    supplier_details = SupplierDetails.get_BySupplierId(supplier_id) 
    if supplier_details:
        if supplier_details.birthdate:
            supplier_details.birthdate = supplier_details.birthdate.strftime('%d/%m/%Y')
       
    form = SupplierDetailsForm(request.POST or None, request.FILES or None, instance=supplier_details)
    if request.method == 'POST':
        segment = Category.get_ById(request.POST['segment'])
        print(segment.name)
        form.instance.segment = segment        
        if form.is_valid():
            form.instance.supplier = supplier
            form.instance.user_auth = request.user
            supplier_details = form.save()
            return redirect('supplier:company_address', supplier_id)
    # print(form)
    return render(request, 'supplier/register/details.html', {
        'form': form, 
        'supplier': supplier,
        'step': 1})    

@login_required(login_url='login')
@auth_supplier_required
def company_address(request, supplier_id):    
    print(request.user)
    supplier = Supplier.get_ById(supplier_id)   
    address = SupplierAddress.get_BySupplierId(supplier_id) 
    form = SupplierAddressForm(request.POST or None, instance=address)   
    
    if request.method == 'POST':
        print('form', form)
        
        if form.is_valid():
            form.instance.supplier = supplier
            form.save()
            return redirect('supplier:sign_plan', supplier_id) 
    
    return render(request, 'supplier/register/address.html', {
        'form': form, 
        'supplier': supplier,
        'step': 2})
    
@login_required(login_url='login')
@auth_supplier_required
def sign_plan(request, supplier_id):    
    form = PaymentForm(request.POST or None)
    if request.method == 'POST':
        plan_id = request.POST.get('plan_id')
        if form.is_valid():                
            supplier = Supplier.get_ById(supplier_id)
            plan = Plan.get_ById(plan_id)
            supplier_order = SupplierOrder()
            supplier_order.supplier = supplier
            supplier_order.plan = plan
            supplier_order.value = plan.price    
            supplier_order.expires_at = datetime.now() + timedelta(days=plan.duration*30+5)  
            supplier_order.save()
            print('supplier_order: ', supplier_order.id)
            form.instance.order = supplier_order
            form.save()        
            return redirect('panel:home', supplier_id=supplier_id)
    print(form)
    plans = Plan.getPlans() 
    return render(request, 'supplier/register/sign-plan.html', {'plans': plans, 'form': form, 'step': 3})


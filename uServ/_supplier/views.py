from datetime import datetime
import json
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import  SupplierCreateForm, SupplierUpdateForm, AddressCreateForm, CieloCreditCardForm, CieloCustomerForm, LoginUserForm
from .models import SupplierUser, Supplier, Plan, Order
from .api.Cielo.models.TransactionSale import Transaction, Customer, Payment, CreditCard, CardOnFile
from .api.Cielo.models.TransactionEnums import Type, Interest
from .api.Cielo.models.CieloEcommerce import CieloEcommerce

from .utils.decorators import validate_url

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required

# 1 LOGIN
def login_user(request):        
    if request.method == 'POST':
        form = LoginUserForm(request, data=request.POST)        
        if form.is_valid():
            username = request.POST.get('username')            
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                auth.login(request, user)
                supplier = Supplier.objects.get(email=username)            
                return redirect('dashboard:dashboard', supplier.id)
            else:
                return render(request, 'dashboard/login/login.html', {
                    'form': form,
                        })
    else:
        form = LoginUserForm()
    context = { 'form': form}
    return render(request, 'supplier/public/login.html', context=context)

# 2 FORGOT PASSWORD
def password(request):   
    if request.method == 'POST':
        pass
    return render(request, 'supplier/public/password.html')

# 3 LOGOUT
def logout(request):
    auth.logout(request)
    messages.success(request, "Logout success!")
    return redirect("supplier:login")



def home(request):    
    return render(request, 'supplier/index.html')

def public_plans(request):
    return render(request, 'supplier/public/plans.html')

# register supplier [email, telefone, password] and user auth
def register_user(request):
    form = SupplierCreateForm()    
    if request.method == 'POST':        
        form = SupplierCreateForm(request.POST)
        if form.is_valid():
            new_supplier : Supplier = form.save()
            # CREATE USER
            user = SupplierUser.objects.create_user(
                email=new_supplier.email, 
                password=new_supplier.password, 
                supplier=new_supplier)          
            
            # LOGIN USER                 
            user_logged = authenticate(request, username=new_supplier.email, password=new_supplier.password)
            if user_logged is not None:
                # Realizamos o login automático
                login(request, user_logged)
                return redirect('suppplier:register_supplier', supplier_id= new_supplier.id)   
    
    context = { 'form_supplier': form }
    return render(request, 'supplier/public/register.html', context=context)

@login_required(login_url='login')
@validate_url(view_name='supplier')
def register_supplier(request, supplier_id,):
    supplier = get_object_or_404(Supplier, pk=supplier_id)   
    
    if request.method == 'POST':
        form_supplier = SupplierUpdateForm(request.POST, instance=supplier)
        form_address = AddressCreateForm(request.POST)
        if form_supplier.is_valid() and form_address.is_valid():
            form_supplier.save()
            form_address.save()
            
            print('updated successfully')
            return redirect('supplier:plan', supplier_id=supplier_id)  # Redirecione para a página desejada após a atualização
    else:        
        form_supplier = SupplierUpdateForm(instance=supplier)
        form_address = AddressCreateForm(initial={'supplier': supplier_id})    
    
    context={'form_supplier': form_supplier, 
            'form_address': form_address, 
            'supplier': supplier}
    
    
    return render(request, 'supplier/public/register.html', 
                  context=context) 

# check_card
def check_card(request):
    print(request)
    card_number = request.GET.get('CardNumber')    
    print(card_number)
    if len(str(card_number)) == 6:
        req_cielo = CieloEcommerce()
        reponse = req_cielo.query_card(cardnumber=card_number)
        
        return HttpResponse(reponse['Provider'])
    pass


# sign plan
@login_required(login_url='login')
@validate_url(view_name='plan')
def register_plan(request, supplier_id, message=None):   
    if request.method == 'POST':
        print(request.user.email)
        print(supplier_id)
        supplier = Supplier.objects.get(id=supplier_id)
        data = request.POST
        # CRIANDO ORDER
        print(data['plan_id'])
        plan = Plan.objects.get(id=data['plan_id'])        
        print(data['Birthdate'])
        
        expired_month = data['MM_ExpirationDate']
        expired_year = data['YY_ExpirationDate']
        
        # # CRIANDO TRANSACTION          
        customer = Customer(
            Name = data['Name'],
            Email = request.user.email,
            Birthdate = str(data['Birthdate'])
        )
               
        card_on_file = CardOnFile(
            Usage = "First",
            Reason = "Recurring"
        )   
               
        credit_card = CreditCard(
            CardNumber = data['CardNumber'],   
            Holder=data['Name'],    
            ExpirationDate = f'{expired_month}/{expired_year}',
            SecurityCode = data['SecurityCode'],
            SaveCard = False,
            Brand = 'Visa',
            CardOnFile = card_on_file,       
        ) 
        
        payment = Payment(
            Currency = 'BRL',
            Country = 'BRA',
            ServiceTaxAmount = 0,
            Installments = 1,
            Interest = Interest.Loja.value,
            Capture = True,
            Authenticate = False,
            Recurrent = True,
            SoftDescriptor = "USERVLTDA",
            Type = Type.CartaoCredito.value,
            Amount = "%d" % (float(data['plan_price'])*100),
            CreditCard = credit_card
        )
        
        transaction = Transaction(
            MerchantOrderId = Order.get_next_id(),
            Customer= customer,
            Payment = payment            
        )
        
        data_json = transaction.to_dict()
        print(data_json) 
        # transaction_json = json.dumps(transaction.to_dict(), indent=2)
        # print(transaction_json)
        request = CieloEcommerce()
        response = request.create_sale_creditcard(transaction=data_json)
        print(response.json())
        # customer.save()
        # card_on_file.save()
        # credit_card.save()
        # payment.save()
        # transaction.save()
        order = Order(plan=plan, 
                      supplier=supplier, 
                      value = data['plan_price'])
        
        order.save()
        
        return redirect('dashboard:dashboard', supplier.id)
    else:    
        plans = Plan.objects.all() 
        form_customer_cielo = CieloCustomerForm()
        form_credit_card = CieloCreditCardForm()
        return render(request, 'supplier/private/plan.html',  {'plans': plans, 
                                                       'form_customer_cielo': form_customer_cielo,
                                                       'form_credit_card': form_credit_card})




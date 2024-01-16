from django.shortcuts import render, redirect, get_object_or_404

from .forms import  SupplierCreateForm, SupplierUpdateForm, AddressCreateForm, LoginUserForm
from .models import SupplierUser, Supplier, Plan, Order


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


# sign plan
@login_required(login_url='login')
@validate_url(view_name='plan')
def register_plan(request, supplier_id, message=None):   
    if request.method == 'POST':
        supplier = Supplier.objects.get(id=supplier_id)
        data = request.POST
        
        # START - Create payment logic
        # ...
        # END - Create payment logic
        
        # CRIANDO ORDER
        plan = Plan.objects.get(id=data['plan_id'])         
       
        order = Order(plan=plan, 
                      supplier=supplier, 
                      value = data['plan_price'])
        
        order.save()
        
        return redirect('dashboard:dashboard', supplier.id)
    else:    
        plans = Plan.objects.all() 
        return render(request, 'supplier/private/plan.html',  {'plans': plans,})




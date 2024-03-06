from functools import wraps
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import auth

def auth_supplier_required(view_func):
    """
    Decorator que verifica se o usuário logado é um fornecedor.
    """    
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_supplier:            
                if 'supplier_id' in kwargs or 'supplier_id' in request.POST or 'supplier_id' in request.GET:
                    supplier_request = kwargs.get('supplier_id') or request.POST.get('supplier_id') or request.GET.get('supplier_id')
                    if str(supplier_request) == str(request.user.supplier.id):                    
                        # Se o usuário é um fornecedor, execute a view normalmente
                        return view_func(request, *args, **kwargs)
            else:
                auth.logout(request)
            return redirect('supplier:login')                
        # else:
        #     # Caso contrário, retorne uma resposta de proibido
        return redirect('supplier:login')
        # return view_func(request, *args, **kwargs)

    return wrapper

def auth_user_required(view_func):
    """
    Decorator que verifica se o usuário logado é um fornecedor.
    """    
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_client:
                if 'user_id' in kwargs or 'user_id' in request.POST or 'user_id' in request.GET:
                    user_request = kwargs.get('user_id') or request.POST.get('user_id') or request.GET.get('user_id')
                    if str(user_request) == str(request.user.supplier.id):                    
                
                
                
                # Se o usuário é um cliente, execute a view normalmente
                        return view_func(request, *args, **kwargs)
            else:
                auth.logout(request)
            return redirect('login')       
        return view_func(request, *args, **kwargs)

    return wrapper
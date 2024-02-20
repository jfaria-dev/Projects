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
                if 'supplier_id' in kwargs:
                    supplier_request = kwargs.get('supplier_id')
                    if supplier_request == request.user.supplier.id:                    
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
                # Se o usuário é um fornecedor, execute a view normalmente
                return view_func(request, *args, **kwargs)
            else:
                auth.logout(request)
            return redirect('login')                
        # else:
        #     # Caso contrário, retorne uma resposta de proibido
        #     return redirect('login')
        return view_func(request, *args, **kwargs)

    return wrapper
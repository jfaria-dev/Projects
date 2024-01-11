import datetime
from functools import wraps
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.contrib import messages
from ..models import Supplier


def validate_url(view_name):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            supplier = Supplier.objects.get(email=request.user.email)
            if supplier == None:
                return HttpResponseRedirect(f'/register',f"Efetue o cadastro de Prestador.") 
                
            if supplier.id == kwargs['supplier_id']:     
                if view_name == 'supplier':
                    if supplier.doc_number: 
                        messages.error(request, f"Cadastro para o Prestador {supplier.name} já realizado.", extra_tags='register_error')
                        return HttpResponseRedirect(f'/register/plan/{supplier.id}')
                           
                if view_name == 'plan':
                    if not supplier.doc_number:
                        messages.error(request, f"Finalize o cadastro para o Prestador {supplier.name}.", extra_tags='register_error')
                        
                        return HttpResponseRedirect(f'/register/{supplier.id}')
                        
                if view_name == 'dashboard':
                    if supplier.orders.filter(expirate_date__gte=datetime.date.today()).count() == 0:
                        messages.error(request, f"Assine um plano para o Prestador {supplier.name}.", extra_tags='register_error')                        
                        return HttpResponseRedirect(f'/register/plan/{supplier.id}')
        
                return view_func(request, *args, **kwargs)
            else:
                messages.error(request, f"Realize o Login para o Prestador {supplier.name}.")
                return HttpResponseRedirect('/logout')

        return _wrapped_view

    return decorator



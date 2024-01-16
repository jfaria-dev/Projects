from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.http import JsonResponse

from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required

from django.db.models import Q
from _supplier.utils.decorators import validate_url
from _supplier.models import Supplier
from _dashboard.models import Service, Category, Unity, SupplierService

from ..forms import ServiceForm, UnityForm

import requests

# sugestao de descriçao de serviço --> NAO USADA AINDA (TESTE)
def suggest_description(name):
    API_KEY_GOOGLE = 'AIzaSyDrGhTZZU4F04f2fCxxvDSPdEdi4no2P-8'
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY_GOOGLE}"
    
    header= {'Content-Type: application/json'}
    payload = {
      "contents": [{
          "parts":[{
              "text": name # f"faça uma descrição atrativa do serviço: {name}. Que essa descrição seja objetiva e sucinta"
              }]}
        ]}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        data = response.json()
        return data['candidates'][0]['content']['parts'][0]['text']
    else:
        return None


# 4 DASHBOARD
@login_required(login_url='login')
@validate_url(view_name='dashboard')
def dashboard(request, supplier_id):      
    supplier = Supplier.objects.get(id=supplier_id)
    context = {
        'supplier': supplier
    } 
    
    return render(request, 'dashboard/index.html', context=context)    

# 5 SERVICES
# 5.1 FETCH SERVICES
@login_required(login_url='login')
def home_services(request, supplier_id):
    supplier = Supplier.objects.get(id=supplier_id)
    context = {
        'supplier': supplier,
        'services': supplier.services.all(),
    }    
    return render(request, 'dashboard/services/home.html', context=context)  

# 5.2 ADD SERVICE
@login_required(login_url='login')
def add_service(request, supplier_id):          
    if request.method == 'POST':
        form_service = ServiceForm(request.POST, request.FILES)
        supplier = get_object_or_404(Supplier, pk=supplier_id) 
        form_service = ServiceForm(request.POST, request.FILES)
        if form_service.is_valid():
            form_service.instance.supplier = supplier
            form_service.instance.user = request.user
            form_service.instance.unit = form_service.cleaned_data['unit']
            form_service.save()            
            return redirect('dashboard:services', supplier_id=supplier_id) 
    else:        
        form_service = ServiceForm()
    
    categories = Category.objects.filter(parent__isnull=True)
    form_unity = UnityForm()
    context = {'form': form_service, 'form_unity': form_unity,'master_categories': categories}
    
    return render(request, 'dashboard/services/add.html', context = context)

# 5.3 UPDATE SERVICE
@login_required(login_url='login')
def edit_service(request, supplier_id, service_id):      
    supplier_service = get_object_or_404(SupplierService, pk=service_id) 
    if request.method == 'POST':
        form_service = ServiceForm(request.POST, request.FILES, instance=supplier_service) 
        print(form_service.errors)
        if form_service.is_valid():
            form_service.instance.unit = form_service.cleaned_data['unit']
            form_service.save()            
        return redirect('dashboard:services', supplier_id=supplier_id) 
    else:     
        # Include instance in the form
        form_service = ServiceForm(instance=supplier_service) 
        categories = Category.objects.filter(Q(parent__isnull=True) | Q(parent_id=supplier_service.service.category.parent.id))
        master_categories = categories.filter(parent__isnull=True)
        service_categories = categories.filter(parent_id=supplier_service.service.category.parent.id)
        services = Service.objects.filter(category_id=supplier_service.service.category)    
        # Form Unity - Add unity in modal
        form_unity = UnityForm()
        
        context = {
            'form': form_service, 
            'supplier_service': supplier_service,
            'form_unity': form_unity,
            'master_categories': master_categories,
            'service_categories': service_categories,
            'service_category': supplier_service.service.category,
            'services': services            
        }
    return render(request, 'dashboard/services/edit.html', context = context)

# 5.4 DELETE SERVICE
@login_required(login_url='login')
def delete_service(request, supplier_id, service_id):
    sup_service = get_object_or_404(SupplierService, pk=service_id) 
    sup_service.delete()
    return redirect('dashboard:services', supplier_id=supplier_id)

# 5.5 LOAD SERVICES CATEGORY
@login_required(login_url='login')
def load_services_category(request):
    master_category_id = request.GET.get('category')
    services_category = Category.objects.filter(parent_id=master_category_id)
    return render(request, 'dashboard/services/partials/_opt_cat.html', {'service_categories': services_category})

# 5.6 LOAD SERVICES
@login_required(login_url='login')
def load_services(request):
    service_category_id = request.GET.get('service_cat')
    services = Service.objects.filter(category_id=service_category_id)
    return render(request, 'dashboard/services/partials/_opt_serv.html', {'services': services})

# 6. ADD UNITY
@login_required(login_url='login')
def add_unity(request):
    if request.method == 'POST':
        unit = UnityForm(request.POST)
        if unit.is_valid():
            unit.save()
            response = []
            for un in Unity.objects.all():
                response.append({'id': un.id, 'text': un.unit})
            return JsonResponse({'status': 'success', 'message': 'Unidade cadastrada com sucesso!', 'data': response})
        else:
            return JsonResponse({'status': 'error', 'message': 'Erro ao cadastrar a unidade.'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Método não permitido.'})
    

    
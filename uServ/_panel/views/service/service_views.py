from django.shortcuts import render, redirect
from ...models import Category, Service, GeneralService
from _web.models import Supplier
from ...forms import ServiceForm

# ---------------------- AJAX FUNCTIONS ----------------------
def fetch_categories(request):
    master_category_id = request.GET.get('segment')
    categories = Category.objects.filter(parent_id=master_category_id)
    return render(request, 'service/partials/_select-categories.html', {'categories': categories})

def fetch_general_services(request):
    category_id = request.GET.get('category')
    services = GeneralService.objects.filter(category_id=category_id)
    return render(request, 'service/partials/_select-services.html', {'services': services})


# ---------------------- VIEWS ----------------------
def fetch_services(request, supplier_id):
    services = Service.get_BySupplierId(supplier_id)    
    media_url = request.build_absolute_uri('/media/')   
    return render(request, 'service/home.html', {'services': services, 'media_url': media_url})

def add_service(request, supplier_id):
    # categories master
    master_categories = Category.objects.filter(parent__isnull=True)
    supplier = Supplier.get_ById(supplier_id)
    form = ServiceForm(request.POST or None, request.FILES or None)
    print(form)
    if form.is_valid():
        form.instance.supplier = supplier
        service = form.save(commit=False)
        service.save()
        return redirect('panel:fetch_services', supplier_id=supplier_id) 
    else:
        master_category = request.POST.get('segment')
        category = request.POST.get('category')
        general_service = request.POST.get('general_service')
        categories = Category.objects.filter(parent_id=master_category)
        services = GeneralService.objects.filter(category_id=category)
        context = {
            'categories': categories,
            'services': services,
            'master_category': master_category,
            'category': category,
            'general_service': general_service
        }
    
    context.update({'form': form, 'master_categories': master_categories}) 
    return render(request, 'service/add.html', context=context)

def edit_service(request, supplier_id, service_id):
    service = Service.get_ById(service_id)
    if service:
        form = ServiceForm(request.POST or None, request.FILES or None, instance=service)
        if request.method == 'POST':      
            if form.is_valid():
                form.save()
                return redirect('panel:fetch_services', supplier_id=supplier_id) 
        category = service.general_service.category.id
        segment = service.general_service.category.parent.id
        general_service = service.general_service.id
        master_categories = Category.objects.filter(parent__isnull=True)    
        categories = Category.objects.filter(parent_id=segment)
        services = GeneralService.objects.filter(category_id=category)
        context = {
            'categories': categories,
            'master_categories': master_categories,
            'services': services,
            'master_category': segment,
            'category': category,
            'general_service': general_service,
            'form': form,
        }
        return render(request, 'service/edit.html', context=context)
    return redirect('panel:fetch_services', supplier_id=supplier_id)

def delete_service(request, supplier_id, service_id):
    service = Service.get_ById(service_id)
    if service:
        service.delete()
    return redirect('panel:fetch_services', supplier_id=supplier_id)
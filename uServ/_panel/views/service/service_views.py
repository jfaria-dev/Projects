from django.shortcuts import render, redirect
from _panel.models import Category, Service, GeneralService, Team, Worker
from _web.models import Supplier
from _panel.forms import ServiceForm
from _utils.decorator import auth_supplier_required

# ---------------------- AJAX FUNCTIONS ----------------------
@auth_supplier_required
def fetch_categories(request):
    master_category_id = request.GET.get('segment')
    categories = Category.objects.filter(parent_id=master_category_id)
    return render(request, 'service/partials/_select-categories.html', {'categories': categories})

# @auth_supplier_required
def fetch_general_services(request):
    category_id = request.GET.get('category')
    services = GeneralService.objects.filter(category_id=category_id)
    return render(request, 'service/partials/_select-services.html', {'services': services})

def fetch_units_for_service(request):
    general_service_id = request.GET.get('general_service_id')
    units = GeneralService.objects.get(id=general_service_id).units_for_service.all()
    return render(request, 'service/partials/_options-units-for-service.html', {'units': units})

def fetch_workers_by_team(request):
    team_id = request.GET.get('team_id')
    workers = Worker.objects.filter(team_id=team_id).order_by('name')
    return render(request, 'team/partials/_options-workers.html', {'workers': workers})

# ---------------------- VIEWS ----------------------
@auth_supplier_required
def fetch_services(request, supplier_id):
    services = Service.get_BySupplierId(supplier_id)    
    media_url = request.build_absolute_uri('/media/')   
    return render(request, 'service/services.html', {'services': services, 'media_url': media_url})

@auth_supplier_required
def add_service(request, supplier_id):
    supplier = Supplier.get_ById(supplier_id)
    print(supplier.available_times.all().count())
    if supplier.available_times.all().count() == 0:
        return redirect('panel:availability', supplier_id=supplier_id)    
    
    form = ServiceForm(request.POST or None, request.FILES or None, supplier=supplier)
    # print(form)
    if form.is_valid():
        form.instance.supplier = supplier
        # form.instance.team = Team.objects.filter(id=form.cleaned_data.get('team')).first()
        form.active = True
        service = form.save(commit=False)
        service.save()
        return redirect('panel:fetch_services', supplier_id=supplier_id) 
    else:
        segment_id = supplier.details.segment.id
        category = request.POST.get('category')
        categories = Category.objects.filter(parent_id=segment_id)
        services = GeneralService.objects.filter(category_id=category)
        context = {
            'categories': categories,
            'category': category,
            'services': services,
        }
    
    context.update({'form': form}) 
    return render(request, 'service/add.html', context=context)

@auth_supplier_required
def edit_service(request, supplier_id, service_id):
    service = Service.get_ById(service_id)
    if service:
        form = ServiceForm(request.POST or None, request.FILES or None, instance=service, supplier=service.supplier)
        if request.method == 'POST':      
            if form.is_valid():
                form.save()
                return redirect('panel:fetch_services', supplier_id=supplier_id)   
            
        category = service.general_service.category.id
        segment = service.general_service.category.parent.id
        categories = Category.objects.filter(parent_id=segment)
        services = GeneralService.objects.filter(category_id=category)
        context = {
            'categories': categories,
            'category': category,
            'services': services,
            'form': form,
        }
        return render(request, 'service/edit.html', context=context)
    return redirect('panel:fetch_services', supplier_id=supplier_id)

@auth_supplier_required
def delete_service(request, supplier_id, service_id):
    service = Service.get_ById(service_id)    
    if service:
        service.active = False
        service.save()
    return redirect('panel:fetch_services', supplier_id=supplier_id)


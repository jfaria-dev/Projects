from django.forms import formset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect
from _utils.decorator import auth_supplier_required

from _panel.forms.available_form import AvailableForm
from _panel.models import AvailableTime
from _web.models import Supplier

# ------------------------------ AJAX ------------------------------
@auth_supplier_required
def add_availability(request):
    supplier_id = request.POST.get('supplier_id')
    supplier = Supplier.get_ById(supplier_id)    
    data = {
        'day_of_week': request.POST.get('day_of_week'),
        'open_time': request.POST.get('open_time'),
        'close_time': request.POST.get('close_time')
    }
    form = AvailableForm(data, supplier=supplier)
    if form.is_valid():
        available_time = form.save(commit=False)
        available_time.supplier = supplier
        available_time.save()
        return render(request, 'panel/partials/_availability_line.html', {'available_time': available_time})

@auth_supplier_required
def delete_availability(request):
    available_time_id = request.POST.get('available_time_id')
    available_time = AvailableTime.get_ById(available_time_id)
    if available_time:
        available_time.delete()
        return HttpResponse(available_time.day_of_week)
    return HttpResponse('Erro ao excluir disponibilidade.')


# ------------------------------ VIEWS ------------------------------

# Create your views here.
@auth_supplier_required
def home(request, supplier_id):
    return render(request, 'panel/calendar.html', {})

@auth_supplier_required
def availability(request, supplier_id):
    supplier = Supplier.get_ById(supplier_id)    
    
    form = AvailableForm(supplier=supplier)
    
    context = {
        'supplier': supplier,
        'form': form,        
    }
    
    return render(request, 'panel/availability.html', context=context)






@auth_supplier_required
def edit_availability(request, supplier_id, available_time_id):
    supplier = Supplier.get_ById(supplier_id)
    available_time = supplier.available_times.get(id=available_time_id)
    form = AvailableForm(request.POST or None, instance=available_time)
    if request.POST:
        if form.is_valid():
            print(form)
    
    context = {
        'supplier': supplier,
        'form': form,        
    }
    return render(request, 'panel/availability.html', context=context)
    
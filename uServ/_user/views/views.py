from django.shortcuts import render
from _dashboard.models import SupplierService, Service

# Home
def home(request):
    return render(request, 'user/index.html')

# Add
def add_user(request):
    return render(request, 'user/add.html')

# Search
def search(request):
    print('request:', request.GET)
    query = request.GET.get('search')
    services = Service.objects.filter(description__icontains=query)
    # services = Service.objects.filter(description__istartswith=query)
    
    supplier_services = []
    for service in services:
        supplier_services.extend(SupplierService.objects.filter(service_id=service.id))
    
    return render(request, 'user/partials/_service-card.html', context= { 'sup_services': supplier_services })

# Schedule
def schedule(request, supplier_service_id):
    
    return render(request, 'user/schedule.html')
    
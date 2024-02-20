from django.shortcuts import render
from _panel.models import Service

def service(request, service_id):
    service = Service.get_ById(service_id)
    media_url = request.build_absolute_uri('/media/') 
    return render(request, 'supplier/service/service.html', context={ 'service': service, 'media_url': media_url})
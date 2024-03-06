from _panel.models import Service, GeneralService
from _api.serializers import ServiceSerializer, GeneralServiceSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def getGeneralServices(request, category_id):
    services = GeneralService.get_ByCategoryId(category_id)
    serializer = GeneralServiceSerializer(services, many=True)    
    return Response(serializer.data)

@api_view(['GET'])
def getServices(request, standard_service_id):
    services = Service.get_ByGeneralServiceId(standard_service_id)
    serializer = ServiceSerializer(services, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getServiceById(request, service_id):
    service = Service.get_ById(service_id)
    serializer = ServiceSerializer(service)
    return Response(serializer.data)

@api_view(['GET'])
def getServicesBySupplierId(request, supplier_id):
    services = Service.get_BySupplierId(supplier_id)
    serializer = ServiceSerializer(services, many=True)
    return Response(serializer.data)
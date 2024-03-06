from _web.models import Supplier
from _api.serializers import SupplierSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getSupplierById(request, supplier_id):
    supplier = Supplier.get_ById(supplier_id)
    serializer = SupplierSerializer(supplier)
    return Response(serializer.data)
from _web.models import Supplier
from ..serializers.supplier_serializer import SupplierSerializer

from rest_framework import generics

class SupplierListAPIView(generics.ListAPIView):
    queryset = Supplier.objects.filter(active=True)
    serializer_class = SupplierSerializer
    
supplier_list_view = SupplierListAPIView.as_view()
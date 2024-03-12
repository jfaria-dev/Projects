from _panel.models import Service
from rest_framework import serializers
from ..supplier.supplier_serializer import SupplierSerializer

class ServiceSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer()
    
    class Meta:
        model = Service
        fields = '__all__'
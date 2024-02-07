from _web.models import Supplier, SupplierDetails, SupplierAddress
from .category_serializer import CategorySerializer
from rest_framework import serializers



class SupplierDetailsSerializer(serializers.ModelSerializer):    
    class Meta:
        model = SupplierDetails
        fields = [
            'id',
            'document_type',
            'company_document_number',
            'birthdate',
            'company_name',
            'company_phone',
            'company_name_show',
            'owner_document_number',
            'photo',
            ]

class SupplierAddressSerializer(serializers.ModelSerializer):        
        class Meta:
            model = SupplierAddress
            fields = [
                'id',
                'street',
                'number',
                'complement',
                'neighborhood',
                'city',
                'state',
                'postal_code',
                ]

class SupplierSerializer(serializers.ModelSerializer):
    details = SupplierDetailsSerializer()
    address = SupplierAddressSerializer()
    
    class Meta:
        model = Supplier
        fields = [
            'id',
            'owner_name',
            'phone',
            'email',
            'details',
            'address',
            ]
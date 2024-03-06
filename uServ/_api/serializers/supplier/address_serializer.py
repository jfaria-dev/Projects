from _web.models import SupplierAddress
from rest_framework import serializers

class AddressSerializer(serializers.ModelSerializer):        
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
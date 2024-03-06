from _web.models import SupplierDetails
from rest_framework import serializers

class DetailsSerializer(serializers.ModelSerializer):    
    class Meta:
        model = SupplierDetails
        fields ='__all__'
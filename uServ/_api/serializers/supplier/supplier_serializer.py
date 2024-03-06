from _web.models import Supplier
from .details_serializer import DetailsSerializer
from .address_serializer import AddressSerializer
from _api.serializers import ServiceSerializer

from rest_framework import serializers


class SupplierSerializer(serializers.ModelSerializer):
    details = DetailsSerializer()
    address = AddressSerializer()
    
    class Meta:
        model = Supplier
        fields = [
                    "details",
                    "address",
                    "owner_name",
                    "email",
                    "phone",
                    "active",
                    "created_at",
                    "updated_at",
                  ]
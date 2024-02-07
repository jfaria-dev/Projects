from _panel.models import Service, GeneralService
from .category_serializer import CategorySerializer
from rest_framework import serializers

class GeneralServiceSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    
    class Meta:
        model = GeneralService
        fields = [
            'id',
            'description',
            'category',
            ]

class ServiceSerializer(serializers.ModelSerializer):
    general_service = GeneralServiceSerializer()
    supplier = serializers.StringRelatedField()
    
    class Meta:
        model = Service
        fields = [
            'id',
            'supplier',
            'general_service', 
            'price', 
            'unit',
            'execution_time',
            'service_image', 
            'requirements',
            'active'
            ]
    
    # def get_general_service(self, obj):
    #     return obj.general_service
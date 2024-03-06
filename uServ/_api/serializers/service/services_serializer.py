from _panel.models import Service
from rest_framework import serializers

class ServiceSerializer(serializers.ModelSerializer):
    # general_service = GeneralServiceSerializer()
    # supplier = serializers.StringRelatedField()
    
    class Meta:
        model = Service
        fields = '__all__'
    
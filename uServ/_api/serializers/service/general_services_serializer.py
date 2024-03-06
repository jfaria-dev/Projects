from _panel.models import Service, GeneralService
from _api.serializers import AllCategorySerializer
from rest_framework import serializers

class GeneralServiceSerializer(serializers.ModelSerializer):
    # category = AllCategorySerializer()
    
    class Meta:
        model = GeneralService
        fields = '__all__'
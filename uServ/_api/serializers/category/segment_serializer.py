from rest_framework.serializers import ModelSerializer
from _panel.models import Category

class SegmentSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
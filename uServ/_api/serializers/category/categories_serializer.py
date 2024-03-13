from rest_framework.serializers import ModelSerializer
from _panel.models import Category

class CategoriesSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'parent', 'active', 'children', 'text_color', 'bg_color')

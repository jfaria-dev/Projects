from rest_framework.serializers import ModelSerializer
from _panel.models import Category

class CategoriesSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'active', 'photo', 'text_color', 'bg_color', 'parent')

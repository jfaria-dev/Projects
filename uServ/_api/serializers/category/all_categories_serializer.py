from _panel.models import Category
from rest_framework import serializers

class AllCategorySerializer(serializers.ModelSerializer):    
    
    queryset = Category.objects.filter(parent__isnull=True, active=True)  # Filter for root categories
    children = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'parent', 'active', 'children', 'text_color', 'background_color')

    def get_children(self, obj):
        if obj.parents.exists():  # Check for child categories
            return AllCategorySerializer(obj.parents.all(), many=True).data
        return None
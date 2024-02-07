from _panel.models import Category
from ..serializers.category_serializer import CategorySerializer

from rest_framework import generics

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.filter(parent__isnull=True)  # Filter for root categories
    serializer_class = CategorySerializer
    
category_list_view = CategoryListAPIView.as_view()
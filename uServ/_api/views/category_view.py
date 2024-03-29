from _panel.models import Category
from _api.serializers import SegmentSerializer, CategoriesSerializer, AllCategorySerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getStructureService(request):
    structure = Category.get_Segments()
    serializer = AllCategorySerializer(structure, many=True)   
    print('entrou') 
    return Response(serializer.data)

@api_view(['GET'])
def getCategories(request):
    segments = Category.get_Segments()
    serializer = SegmentSerializer(segments, many=True)    
    return Response(serializer.data)

@api_view(['GET'])
def getProfessionals(request):
    category_id = request.GET.get('category_id')
    print(category_id)
    categories = Category.get_Children(category_id)
    serializer = CategoriesSerializer(categories, many=True)    
    return Response(serializer.data)
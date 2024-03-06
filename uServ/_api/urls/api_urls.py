from django.urls import path

from ..views import service_view, category_view, supplier_view

urlpatterns = [
    
    
    # Segments and Categories
    path('structure', category_view.getStructureService),
    path('segment', category_view.getSegments),
    path('segment/<str:segment_id>', category_view.getCategories),
       
    
    # Services
    path('standard-services/<str:category_id>', service_view.getGeneralServices),
    path('standard-services/services/<str:standard_service_id>', service_view.getServices),
    path('service/<str:service_id>', service_view.getServiceById),
    
    
    
    
    path('supplier/<str:supplier_id>', supplier_view.getSupplierById),
    path('supplier/<str:supplier_id>/services', service_view.getServicesBySupplierId),
]

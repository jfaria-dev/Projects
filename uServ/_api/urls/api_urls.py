from django.urls import path

from ..views import service_view, category_view, supplier_view

urlpatterns = [
    path('service', service_view.service_list_view),
    path('service/<int:pk>', service_view.service_detail_view),
    path('category', category_view.category_list_view),
    path('supplier', supplier_view.supplier_list_view),
]

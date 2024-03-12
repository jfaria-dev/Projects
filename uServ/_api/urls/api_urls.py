from django.urls import path
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.views import obtain_auth_token


from ..views import service_view, category_view, supplier_view, user_view


urlpatterns = [
    # Authentication user
    path('get-token', obtain_auth_token, name="get_token"),
    path('login', user_view.login, name="login"),
    path('signup', user_view.signup, name="signup"),
    path('logout', user_view.logout, name="logout"),
    path('test', user_view.test_auth, name="test"),
    
    
    # Segments and Categories
    path('structure', category_view.getStructureService),
    path('segment', category_view.getSegments),
    path('categories', category_view.getCategories),
    
    
    # Services
    path('standard-services/<str:category_id>', service_view.getGeneralServices),
    path('standard-services/services/<str:standard_service_id>', service_view.getServices),
    path('service/<str:service_id>', service_view.getServiceById),
    
        
    # Suppliers
    path('supplier/<str:supplier_id>', supplier_view.getSupplierById),
    path('supplier/<str:supplier_id>/services', service_view.getServicesBySupplierId),
]

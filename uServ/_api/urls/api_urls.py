from django.urls import path
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.views import obtain_auth_token


from ..views import service_view, category_view, supplier_view, user_view, api_view


urlpatterns = [
    # Endpoints
    path('', api_view.fetch_endpoints, name="home"),
    
    # Authentication user
    path('get-token', obtain_auth_token, name="get_token"),
    path('login', user_view.login, name="login"),
    path('signup', user_view.signup, name="signup"),
    path('logout', user_view.logout, name="logout"),
        
    # Categories and Professionals
    path('structure', category_view.getStructureService),
    path('sectors', category_view.getCategories),
    path('categories', category_view.getProfessionals),
        
    # Services
    path('standard-services/<int:category_id>', service_view.getGeneralServices), # busca os serviços pelos profissionais (categoria)
    path('services-by-generalservice/<int:general_service_id>', service_view.getServices),
    path('service/<int:service_id>', service_view.getServiceById),
    
    # Suppliers
    path('supplier/<int:supplier_id>', supplier_view.getSupplierById),
    path('supplier/<int:supplier_id>/services', service_view.getServicesBySupplierId),
]

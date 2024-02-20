from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ..views.supplier import supplier_views

app_name = 'supplier'
supplier_urls = [
    path('', supplier_views.home, name='home'),
    path('login', supplier_views.login_supplier, name='login'),
    path('logout', supplier_views.logout_supplier, name='logout'),
    path('register', supplier_views.register, name='register'),
    path('<int:supplier_id>', supplier_views.supplier, name='supplier'),
    path('register/<int:supplier_id>/details', supplier_views.company_details, name='company_details'),
    path('register/<int:supplier_id>/address', supplier_views.company_address, name='company_address'),
    path('register/<int:supplier_id>/plan', supplier_views.sign_plan, name='sign_plan'),
    
]

# AJAX/HTMX URLS
ajax_urls = [
    path('get_address_from_postal_code', supplier_views.get_address_from_postal_code, name='get_address_from_postal_code'),
    path('get_company_from_document', supplier_views.get_company_from_document, name='get_company_from_document'),
    path('get_professional_from_document', supplier_views.get_professional_from_document, name='get_professional_from_document'),
    path('validate_email', supplier_views.validate_email, name='validate_email'),
    path('get_cc_type', supplier_views.get_cc_type, name='get_cc_type'),
]

# IMAGES/FILES URLS
file_urls = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

supplier_urls += ajax_urls + file_urls
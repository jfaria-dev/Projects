from django.urls import path
from ..views.supplier import supplier_views

app_name = 'supplier'
supplier_urls = [
    path('', supplier_views.home, name='home'),
    path('login', supplier_views.login, name='login'),
    path('register', supplier_views.register, name='register'),
    path('register/choice/<int:supplier_id>', supplier_views.document_choice, name='document_choice'),
    path('register/<int:supplier_id>', supplier_views.company, name='company'),
    path('register/service_professional/<int:supplier_id>', supplier_views.service_professional, name='service_professional'),
    path('register/<int:supplier_id>/plan', supplier_views.sign_plan, name='sign_plan'),
    
]

htmx_urls = [
    path('get_address_from_postal_code', supplier_views.get_address_from_postal_code, name='get_address_from_postal_code'),
    path('get_company_from_document', supplier_views.get_company_from_document, name='get_company_from_document'),
    path('get_professional_from_document', supplier_views.get_professional_from_document, name='get_professional_from_document'),
]

supplier_urls += htmx_urls
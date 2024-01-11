from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

dashboard_urls = [   
    # Home
    path('supplier/<int:supplier_id>/dashboard', views.dashboard, name='dashboard'),
    # List Services
    path('supplier/<int:supplier_id>/dashboard/services', views.home_services, name='services'),
    # Add Service
    path('supplier/<int:supplier_id>/dashboard/services/add', views.add_service, name='add_service'),
    # Edit Service
    path('supplier/<int:supplier_id>/dashboard/services/<int:service_id>', views.edit_service, name='edit_service'),
    # Delete Service
    path('supplier/<int:supplier_id>/dashboard/services/delete/<int:service_id>', views.delete_service, name='delete_service'),   
]

# MODALS
modal_urls = [
    # Add Unity
    path('add_unity', views.add_unity, name='add_unity'),  
]
dashboard_urls += modal_urls


# HTMX URLS
htmx_urls = [
    # Load Services Categories
    path('load_services_category', views.load_services_category, name='load_services_category'),
    # Load Services
    path('load_services', views.load_services, name='load_services'),
]
dashboard_urls += htmx_urls

# IMAGES URLS
dashboard_urls += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


dashboard_urls = (dashboard_urls, 'dashboard')
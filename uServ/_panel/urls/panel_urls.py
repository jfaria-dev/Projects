from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from ..views.panel import panel_views
from ..views.service import service_views

# PANEL URLS
panel_urls = [
    path('<int:supplier_id>', panel_views.home , name='home'),
    path('<int:supplier_id>/services', service_views.fetch_services , name='fetch_services'),
    path('<int:supplier_id>/services/add', service_views.add_service , name='add_service'),
    path('<int:supplier_id>/services/edit/<int:service_id>', service_views.edit_service , name='edit_service'),
    path('<int:supplier_id>/services/delete/<int:service_id>', service_views.delete_service , name='delete_service')
]

# AJAX URLS
ajax_urls = [
    path('v1/ajax/fetch_categories', service_views.fetch_categories , name='fetch_categories'),
    path('v1/ajax/fetch_general_services', service_views.fetch_general_services , name='fetch_general_services')
]

# IMAGES URLS
images_urls = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


panel_urls += ajax_urls
panel_urls += images_urls
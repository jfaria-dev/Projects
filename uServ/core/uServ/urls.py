from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.views.generic import TemplateView

from _web.urls import user_urls, supplier_urls, schedule_urls
from _panel.urls import panel_urls
from _api.urls import api_urls

from rest_framework.schemas import get_schema_view

urlpatterns = [    
    path('admin/', admin.site.urls),    
    path('', include(user_urls)),
    path('schedule/', include((schedule_urls, 'schedule'), namespace='schedule')),
    path('supplier/', include((supplier_urls,'supplier'), namespace='supplier')),
    path('panel/', include((panel_urls,'panel'), namespace='panel')),
    path('api/', include((api_urls,'api'), namespace='api')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

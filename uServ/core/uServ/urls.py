"""
URL configuration for uServ project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from _user.urls import user_urls
from _web.urls import user_urls, supplier_urls
from _panel.urls import panel_urls
from _api.urls import api_urls

urlpatterns = [
    
    path('admin/', admin.site.urls),    
    path('', include(user_urls)),
    path('supplier/', include((supplier_urls,'supplier'), namespace='supplier')),
    path('panel/', include((panel_urls,'panel'), namespace='panel')),
    path('api/', include((api_urls,'api'), namespace='api')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

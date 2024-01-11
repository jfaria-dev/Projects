from django.urls import path
from . import views


user_urls = [
    path('', views.home, name='home'),
    path('add', views.add_user, name='add'),
    path('schedule/<int:supplier_service_id>', views.schedule, name='schedule'),
    
]

# Htmx urls
htmx_urls = [
    path('search', views.search, name='search'),
]

user_urls += htmx_urls
user_urls = (user_urls, 'user')
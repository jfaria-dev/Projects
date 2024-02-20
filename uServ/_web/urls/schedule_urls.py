from django.urls import path
from ..views.schedule import schedule_views

app_name = 'schedule'
schedule_urls = [    
    path('service/<int:service_id>', schedule_views.service, name='service'),
]
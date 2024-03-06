from django.urls import path
from ..views.schedule import schedule_views

app_name = 'schedule'
schedule_urls = [    
    path('service/<int:service_id>', schedule_views.service, name='service'),
    path('supplier/<int:supplier_id>', schedule_views.supplier, name='supplier'),
    path('checkout/<int:cart_id>', schedule_views.checkout, name='checkout'),
]

# AJAX
schedule_urls += [
    path('availability_by_worker', schedule_views.availability_by_worker, name='availability_by_worker'),
    path('add_schedule_to_cart', schedule_views.add_schedule_to_cart, name='add_schedule_to_cart'),
]
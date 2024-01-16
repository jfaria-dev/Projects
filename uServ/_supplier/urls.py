from django.urls import path
from . import views

supplier_urls = [
    path('', views.home, name='home'),   
     # Login
    path('login', views.login_user, name='login'),
    # Logout
    path('logout', views.logout, name='logout'),
    # Forgot password
    path('password', views.login_user, name='password'),    
    path('plans', views.public_plans, name='public_plans'),
    path('register', views.register_user, name='register_user'),
    # path('register/<int:supplier_id>', views.register_supplier, name='register_supplier'),
    # path('register/plan/<int:supplier_id>', views.register_plan, name='plan'),    
]

# HTMX URLS
htmx_urls = [
    # path('check_card', views.check_card, name='check_card'),   
]
supplier_urls += htmx_urls

supplier_urls = ( supplier_urls , 'supplier')
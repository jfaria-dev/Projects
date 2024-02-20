from django.urls import path
from ..views.user import user_views
from ..views.schedule import schedule_views

user_urls = [
    path('', user_views.home, name='home'),
    path('login', user_views.login, name='login'),
    path('logout', user_views.logout, name='logout'),
    path('register', user_views.register, name='register'),
]

# AJAX URLS
ajax_urls = [
    path('save_location_session', user_views.save_location_session, name='save_location_session'),
]

# HTMX URLS
htmx_urls = [
    path('search', user_views.search, name='search'),
]

user_urls += ajax_urls + htmx_urls
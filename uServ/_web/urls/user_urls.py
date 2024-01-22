from django.urls import path
from ..views.user import user_views

user_urls = [
    path('', user_views.home, name='home'),
    path('login', user_views.login, name='login'),
    path('logout', user_views.logout, name='logout'),
    path('register', user_views.register, name='register'),
]
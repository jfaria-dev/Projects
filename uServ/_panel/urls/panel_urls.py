from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from ..views.panel import panel_views
from ..views.service import service_views
from ..views.team import team_views, worker_views

# PANEL VIEW URLS
panel_urls = [
    path('<int:supplier_id>', panel_views.home , name='home'),
    path('<int:supplier_id>/availability', panel_views.availability, name='availability'),
    # path('<int:supplier_id>/availability/<int:id_available_time>', panel_views.edit_availability, name='edit_availability'),
]

# SERVICE URLS
panel_urls += [    
    path('<int:supplier_id>/services', service_views.fetch_services , name='fetch_services'),
    path('<int:supplier_id>/services/add', service_views.add_service , name='add_service'),
    path('<int:supplier_id>/services/edit/<int:service_id>', service_views.edit_service , name='edit_service'),
    path('<int:supplier_id>/services/delete/<int:service_id>', service_views.delete_service , name='delete_service')
]

# TEAMS URLS
panel_urls += [
    path('<int:supplier_id>/teams', team_views.fetch_teams , name='fetch_teams'),
    path('<int:supplier_id>/teams/<int:team_id>', team_views.view_team , name='view_team'),
    path('<int:supplier_id>/teams/add', team_views.add_team , name='add_team'),
    path('<int:supplier_id>/teams/edit/<int:team_id>', team_views.edit_team , name='edit_team'),
    path('<int:supplier_id>/teams/delete/<int:team_id>', team_views.delete_team , name='delete_team')
]

# WOKERS URLS
panel_urls += [
    path('<int:supplier_id>/teams/<int:team_id>/workers/add', worker_views.add_worker , name='add_worker'),
    path('<int:supplier_id>/teams/<int:team_id>/workers/edit/<int:worker_id>', worker_views.edit_worker , name='edit_worker'),
    path('<int:supplier_id>/teams/<int:team_id>/workers/delete/<int:worker_id>', worker_views.delete_worker , name='delete_worker')
]

# AJAX URLS
panel_urls += [
    path('v1/ajax/fetch_categories', service_views.fetch_categories , name='fetch_categories'),
    path('v1/ajax/fetch_general_services', service_views.fetch_general_services , name='fetch_general_services'),
    path('v1/ajax/fetch_units_for_service', service_views.fetch_units_for_service , name='fetch_units_for_service'),
    path('v1/ajax/fetch_workers_by_team', service_views.fetch_workers_by_team , name='fetch_workers_by_team'),
    path('v1/ajax/add_availability', panel_views.add_availability , name='add_availability'),
    path('v1/ajax/delete_availability', panel_views.delete_availability , name='delete_availability'),
    
]

# IMAGES URLS
panel_urls += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


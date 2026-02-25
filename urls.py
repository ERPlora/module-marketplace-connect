from django.urls import path
from . import views

app_name = 'marketplace_connect'

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Navigation tab aliases
    path('connections/', views.marketplace_connections_list, name='connections'),


    # MarketplaceConnection
    path('marketplace_connections/', views.marketplace_connections_list, name='marketplace_connections_list'),
    path('marketplace_connections/add/', views.marketplace_connection_add, name='marketplace_connection_add'),
    path('marketplace_connections/<uuid:pk>/edit/', views.marketplace_connection_edit, name='marketplace_connection_edit'),
    path('marketplace_connections/<uuid:pk>/delete/', views.marketplace_connection_delete, name='marketplace_connection_delete'),
    path('marketplace_connections/bulk/', views.marketplace_connections_bulk_action, name='marketplace_connections_bulk_action'),

    # Settings
    path('settings/', views.settings_view, name='settings'),
]

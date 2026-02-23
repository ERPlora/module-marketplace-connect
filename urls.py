from django.urls import path
from . import views

app_name = 'marketplace_connect'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('connections/', views.connections, name='connections'),
    path('settings/', views.settings, name='settings'),
]

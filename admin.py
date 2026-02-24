from django.contrib import admin

from .models import MarketplaceConnection

@admin.register(MarketplaceConnection)
class MarketplaceConnectionAdmin(admin.ModelAdmin):
    list_display = ['marketplace', 'name', 'status', 'api_key', 'last_sync_at', 'created_at']
    search_fields = ['marketplace', 'name', 'status', 'api_key']
    readonly_fields = ['created_at', 'updated_at']


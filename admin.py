from django.contrib import admin

from .models import MarketplaceConnection

@admin.register(MarketplaceConnection)
class MarketplaceConnectionAdmin(admin.ModelAdmin):
    list_display = ['marketplace', 'name', 'status', 'api_key', 'last_sync_at']
    readonly_fields = ['id', 'hub_id', 'created_at', 'updated_at']
    ordering = ['-created_at']


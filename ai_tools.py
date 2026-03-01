"""AI tools for the Marketplace Connect module."""
from assistant.tools import AssistantTool, register_tool


@register_tool
class ListMarketplaceConnections(AssistantTool):
    name = "list_marketplace_connections"
    description = "List marketplace connections (Amazon, eBay, etc.)."
    module_id = "marketplace_connect"
    required_permission = "marketplace_connect.view_marketplaceconnection"
    parameters = {"type": "object", "properties": {"status": {"type": "string"}, "marketplace": {"type": "string"}}, "required": [], "additionalProperties": False}

    def execute(self, args, request):
        from marketplace_connect.models import MarketplaceConnection
        qs = MarketplaceConnection.objects.all()
        if args.get('status'):
            qs = qs.filter(status=args['status'])
        if args.get('marketplace'):
            qs = qs.filter(marketplace=args['marketplace'])
        return {"connections": [{"id": str(c.id), "marketplace": c.marketplace, "name": c.name, "status": c.status, "sync_enabled": c.sync_enabled, "last_sync_at": c.last_sync_at.isoformat() if c.last_sync_at else None} for c in qs]}


@register_tool
class GetMarketplaceConnection(AssistantTool):
    name = "get_marketplace_connection"
    description = "Get detailed marketplace connection info."
    module_id = "marketplace_connect"
    required_permission = "marketplace_connect.view_marketplaceconnection"
    parameters = {
        "type": "object",
        "properties": {"connection_id": {"type": "string", "description": "Connection ID"}},
        "required": ["connection_id"],
        "additionalProperties": False,
    }

    def execute(self, args, request):
        from marketplace_connect.models import MarketplaceConnection
        c = MarketplaceConnection.objects.get(id=args['connection_id'])
        return {
            "id": str(c.id), "marketplace": c.marketplace, "name": c.name,
            "status": c.status, "sync_enabled": c.sync_enabled,
            "last_sync_at": c.last_sync_at.isoformat() if c.last_sync_at else None,
            "config": c.config if c.config else {},
            "api_key_set": bool(c.api_key),
        }


@register_tool
class ToggleMarketplaceSync(AssistantTool):
    name = "toggle_marketplace_sync"
    description = "Enable or disable sync for a marketplace connection."
    module_id = "marketplace_connect"
    required_permission = "marketplace_connect.change_marketplaceconnection"
    requires_confirmation = True
    parameters = {
        "type": "object",
        "properties": {
            "connection_id": {"type": "string", "description": "Connection ID"},
            "enabled": {"type": "boolean", "description": "Enable (true) or disable (false) sync"},
        },
        "required": ["connection_id", "enabled"],
        "additionalProperties": False,
    }

    def execute(self, args, request):
        from marketplace_connect.models import MarketplaceConnection
        c = MarketplaceConnection.objects.get(id=args['connection_id'])
        c.sync_enabled = args['enabled']
        c.save(update_fields=['sync_enabled'])
        return {"id": str(c.id), "name": c.name, "sync_enabled": c.sync_enabled}

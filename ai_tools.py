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

"""
AI context for the Marketplace Connect module.
Loaded into the assistant system prompt when this module's tools are active.
"""

CONTEXT = """
## Module Knowledge: Marketplace Connect

### Models

**MarketplaceConnection**
- `marketplace` (CharField, max 50) — identifier of the external marketplace (e.g. 'amazon', 'ebay', 'glovo')
- `name` (CharField) — human-readable connection name
- `status` (CharField) — choices: connected, disconnected, error
- `api_key` (CharField) — API credentials for the marketplace
- `last_sync_at` (DateTimeField, nullable) — when data was last synchronized
- `sync_enabled` (BooleanField, default False) — whether automatic sync is active
- `config` (JSONField) — flexible extra configuration per marketplace (shop IDs, region codes, etc.)

### Key flows

1. **Add connection**: Create a MarketplaceConnection with the marketplace identifier, name, and API credentials. Status starts as 'disconnected'.
2. **Activate**: Set `status='connected'` and `sync_enabled=True` after verifying credentials.
3. **Sync**: When a sync runs, update `last_sync_at` to the current timestamp.
4. **Error handling**: If the connection breaks, set `status='error'` and optionally disable `sync_enabled`.

### Relationships
- No FKs to other modules — this module manages external marketplace integrations independently.
- Products synced to marketplaces are referenced via `config` JSON or by marketplace-specific IDs.
- Multiple connections can exist per hub (one per external marketplace).
"""

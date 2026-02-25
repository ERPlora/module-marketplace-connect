# Marketplace Connectors Module

Connect to Amazon, eBay, Shopify and other marketplaces.

## Features

- Connect to external marketplaces (Amazon, eBay, Shopify, and others)
- Manage multiple marketplace connections per hub
- Connection status tracking: connected, disconnected, and error states
- API key storage for secure marketplace authentication
- Enable/disable sync per connection
- Last sync timestamp tracking for monitoring
- Flexible JSON configuration per connection for marketplace-specific settings

## Installation

This module is installed automatically via the ERPlora Marketplace.

## Configuration

Access settings via: **Menu > Marketplace Connectors > Settings**

## Usage

Access via: **Menu > Marketplace Connectors**

### Views

| View | URL | Description |
|------|-----|-------------|
| Dashboard | `/m/marketplace_connect/dashboard/` | Overview of marketplace connections and sync status |
| Connections | `/m/marketplace_connect/connections/` | Manage marketplace connections |
| Settings | `/m/marketplace_connect/settings/` | Module configuration |

## Models

| Model | Description |
|-------|-------------|
| `MarketplaceConnection` | Marketplace integration with name, marketplace type, status, API key, sync toggle, last sync timestamp, and JSON config |

## Permissions

| Permission | Description |
|------------|-------------|
| `marketplace_connect.view_marketplaceconnection` | View marketplace connections |
| `marketplace_connect.add_marketplaceconnection` | Create new connections |
| `marketplace_connect.change_marketplaceconnection` | Edit existing connections |
| `marketplace_connect.delete_marketplaceconnection` | Delete connections |
| `marketplace_connect.manage_settings` | Manage module settings |

## License

MIT

## Author

ERPlora Team - support@erplora.com

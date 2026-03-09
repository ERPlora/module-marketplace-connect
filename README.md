# Marketplace Connectors

## Overview

| Property | Value |
|----------|-------|
| **Module ID** | `marketplace_connect` |
| **Version** | `1.0.0` |
| **Icon** | `globe-outline` |
| **Dependencies** | None |

## Models

### `MarketplaceConnection`

MarketplaceConnection(id, hub_id, created_at, updated_at, created_by, updated_by, is_deleted, deleted_at, marketplace, name, status, api_key, last_sync_at, sync_enabled, config)

| Field | Type | Details |
|-------|------|---------|
| `marketplace` | CharField | max_length=50 |
| `name` | CharField | max_length=255 |
| `status` | CharField | max_length=20, choices: connected, disconnected, error |
| `api_key` | CharField | max_length=255, optional |
| `last_sync_at` | DateTimeField | optional |
| `sync_enabled` | BooleanField |  |
| `config` | JSONField | optional |

## URL Endpoints

Base path: `/m/marketplace_connect/`

| Path | Name | Method |
|------|------|--------|
| `(root)` | `dashboard` | GET |
| `connections/` | `connections` | GET |
| `marketplace_connections/` | `marketplace_connections_list` | GET |
| `marketplace_connections/add/` | `marketplace_connection_add` | GET/POST |
| `marketplace_connections/<uuid:pk>/edit/` | `marketplace_connection_edit` | GET |
| `marketplace_connections/<uuid:pk>/delete/` | `marketplace_connection_delete` | GET/POST |
| `marketplace_connections/bulk/` | `marketplace_connections_bulk_action` | GET/POST |
| `settings/` | `settings` | GET |

## Permissions

| Permission | Description |
|------------|-------------|
| `marketplace_connect.view_marketplaceconnection` | View Marketplaceconnection |
| `marketplace_connect.add_marketplaceconnection` | Add Marketplaceconnection |
| `marketplace_connect.change_marketplaceconnection` | Change Marketplaceconnection |
| `marketplace_connect.delete_marketplaceconnection` | Delete Marketplaceconnection |
| `marketplace_connect.manage_settings` | Manage Settings |

**Role assignments:**

- **admin**: All permissions
- **manager**: `add_marketplaceconnection`, `change_marketplaceconnection`, `view_marketplaceconnection`
- **employee**: `add_marketplaceconnection`, `view_marketplaceconnection`

## Navigation

| View | Icon | ID | Fullpage |
|------|------|----|----------|
| Dashboard | `speedometer-outline` | `dashboard` | No |
| Connections | `globe-outline` | `connections` | No |
| Settings | `settings-outline` | `settings` | No |

## AI Tools

Tools available for the AI assistant:

### `list_marketplace_connections`

List marketplace connections (Amazon, eBay, etc.).

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `status` | string | No |  |
| `marketplace` | string | No |  |

### `get_marketplace_connection`

Get detailed marketplace connection info.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `connection_id` | string | Yes | Connection ID |

### `toggle_marketplace_sync`

Enable or disable sync for a marketplace connection.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `connection_id` | string | Yes | Connection ID |
| `enabled` | boolean | Yes | Enable (true) or disable (false) sync |

## File Structure

```
README.md
__init__.py
admin.py
ai_tools.py
apps.py
forms.py
locale/
  en/
    LC_MESSAGES/
      django.po
  es/
    LC_MESSAGES/
      django.po
migrations/
  0001_initial.py
  __init__.py
models.py
module.py
static/
  icons/
    icon.svg
  marketplace_connect/
    css/
    js/
templates/
  marketplace_connect/
    pages/
      connections.html
      dashboard.html
      index.html
      marketplace_connection_add.html
      marketplace_connection_edit.html
      marketplace_connections.html
      settings.html
    partials/
      connections_content.html
      dashboard_content.html
      marketplace_connection_add_content.html
      marketplace_connection_edit_content.html
      marketplace_connections_content.html
      marketplace_connections_list.html
      panel_marketplace_connection_add.html
      panel_marketplace_connection_edit.html
      settings_content.html
tests/
  __init__.py
  conftest.py
  test_models.py
  test_views.py
urls.py
views.py
```

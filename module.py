    from django.utils.translation import gettext_lazy as _

    MODULE_ID = 'marketplace_connect'
    MODULE_NAME = _('Marketplace Connectors')
    MODULE_VERSION = '1.0.0'
    MODULE_ICON = 'globe-outline'
    MODULE_DESCRIPTION = _('Connect to Amazon, eBay, Shopify and other marketplaces')
    MODULE_AUTHOR = 'ERPlora'
    MODULE_CATEGORY = 'integrations'

    MENU = {
        'label': _('Marketplace Connectors'),
        'icon': 'globe-outline',
        'order': 86,
    }

    NAVIGATION = [
        {'label': _('Dashboard'), 'icon': 'speedometer-outline', 'id': 'dashboard'},
{'label': _('Connections'), 'icon': 'globe-outline', 'id': 'connections'},
{'label': _('Settings'), 'icon': 'settings-outline', 'id': 'settings'},
    ]

    DEPENDENCIES = []

    PERMISSIONS = [
        'marketplace_connect.view_marketplaceconnection',
'marketplace_connect.add_marketplaceconnection',
'marketplace_connect.change_marketplaceconnection',
'marketplace_connect.delete_marketplaceconnection',
'marketplace_connect.manage_settings',
    ]

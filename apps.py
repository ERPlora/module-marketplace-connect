from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MarketplaceConnectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'marketplace_connect'
    label = 'marketplace_connect'
    verbose_name = _('Marketplace Connectors')

    def ready(self):
        pass

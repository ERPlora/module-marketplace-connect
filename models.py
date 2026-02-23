from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models.base import HubBaseModel

CONN_STATUS = [
    ('connected', _('Connected')),
    ('disconnected', _('Disconnected')),
    ('error', _('Error')),
]

class MarketplaceConnection(HubBaseModel):
    marketplace = models.CharField(max_length=50, verbose_name=_('Marketplace'))
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    status = models.CharField(max_length=20, default='disconnected', choices=CONN_STATUS, verbose_name=_('Status'))
    api_key = models.CharField(max_length=255, blank=True, verbose_name=_('Api Key'))
    last_sync_at = models.DateTimeField(null=True, blank=True, verbose_name=_('Last Sync At'))
    sync_enabled = models.BooleanField(default=False, verbose_name=_('Sync Enabled'))
    config = models.JSONField(default=dict, blank=True, verbose_name=_('Config'))

    class Meta(HubBaseModel.Meta):
        db_table = 'marketplace_connect_marketplaceconnection'

    def __str__(self):
        return self.name


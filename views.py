"""
Marketplace Connectors Module Views
"""
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from apps.accounts.decorators import login_required
from apps.core.htmx import htmx_view
from apps.modules_runtime.navigation import with_module_nav


@login_required
@with_module_nav('marketplace_connect', 'dashboard')
@htmx_view('marketplace_connect/pages/dashboard.html', 'marketplace_connect/partials/dashboard_content.html')
def dashboard(request):
    """Dashboard view."""
    hub_id = request.session.get('hub_id')
    return {}


@login_required
@with_module_nav('marketplace_connect', 'connections')
@htmx_view('marketplace_connect/pages/connections.html', 'marketplace_connect/partials/connections_content.html')
def connections(request):
    """Connections view."""
    hub_id = request.session.get('hub_id')
    return {}


@login_required
@with_module_nav('marketplace_connect', 'settings')
@htmx_view('marketplace_connect/pages/settings.html', 'marketplace_connect/partials/settings_content.html')
def settings(request):
    """Settings view."""
    hub_id = request.session.get('hub_id')
    return {}


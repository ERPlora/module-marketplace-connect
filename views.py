"""
Marketplace Connectors Module Views
"""
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.shortcuts import get_object_or_404, render as django_render
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_POST

from apps.accounts.decorators import login_required
from apps.core.htmx import htmx_view
from apps.core.services import export_to_csv, export_to_excel
from apps.modules_runtime.navigation import with_module_nav

from .models import MarketplaceConnection

PER_PAGE_CHOICES = [10, 25, 50, 100]


# ======================================================================
# Dashboard
# ======================================================================

@login_required
@with_module_nav('marketplace_connect', 'dashboard')
@htmx_view('marketplace_connect/pages/index.html', 'marketplace_connect/partials/dashboard_content.html')
def dashboard(request):
    hub_id = request.session.get('hub_id')
    return {
        'total_marketplace_connections': MarketplaceConnection.objects.filter(hub_id=hub_id, is_deleted=False).count(),
    }


# ======================================================================
# MarketplaceConnection
# ======================================================================

MARKETPLACE_CONNECTION_SORT_FIELDS = {
    'name': 'name',
    'status': 'status',
    'sync_enabled': 'sync_enabled',
    'marketplace': 'marketplace',
    'api_key': 'api_key',
    'last_sync_at': 'last_sync_at',
    'created_at': 'created_at',
}

def _build_marketplace_connections_context(hub_id, per_page=10):
    qs = MarketplaceConnection.objects.filter(hub_id=hub_id, is_deleted=False).order_by('name')
    paginator = Paginator(qs, per_page)
    page_obj = paginator.get_page(1)
    return {
        'marketplace_connections': page_obj,
        'page_obj': page_obj,
        'search_query': '',
        'sort_field': 'name',
        'sort_dir': 'asc',
        'current_view': 'table',
        'per_page': per_page,
    }

def _render_marketplace_connections_list(request, hub_id, per_page=10):
    ctx = _build_marketplace_connections_context(hub_id, per_page)
    return django_render(request, 'marketplace_connect/partials/marketplace_connections_list.html', ctx)

@login_required
@with_module_nav('marketplace_connect', 'connections')
@htmx_view('marketplace_connect/pages/marketplace_connections.html', 'marketplace_connect/partials/marketplace_connections_content.html')
def marketplace_connections_list(request):
    hub_id = request.session.get('hub_id')
    search_query = request.GET.get('q', '').strip()
    sort_field = request.GET.get('sort', 'name')
    sort_dir = request.GET.get('dir', 'asc')
    page_number = request.GET.get('page', 1)
    current_view = request.GET.get('view', 'table')
    per_page = int(request.GET.get('per_page', 10))
    if per_page not in PER_PAGE_CHOICES:
        per_page = 10

    qs = MarketplaceConnection.objects.filter(hub_id=hub_id, is_deleted=False)

    if search_query:
        qs = qs.filter(Q(marketplace__icontains=search_query) | Q(name__icontains=search_query) | Q(status__icontains=search_query) | Q(api_key__icontains=search_query))

    order_by = MARKETPLACE_CONNECTION_SORT_FIELDS.get(sort_field, 'name')
    if sort_dir == 'desc':
        order_by = f'-{order_by}'
    qs = qs.order_by(order_by)

    export_format = request.GET.get('export')
    if export_format in ('csv', 'excel'):
        fields = ['name', 'status', 'sync_enabled', 'marketplace', 'api_key', 'last_sync_at']
        headers = ['Name', 'Status', 'Sync Enabled', 'Marketplace', 'Api Key', 'Last Sync At']
        if export_format == 'csv':
            return export_to_csv(qs, fields=fields, headers=headers, filename='marketplace_connections.csv')
        return export_to_excel(qs, fields=fields, headers=headers, filename='marketplace_connections.xlsx')

    paginator = Paginator(qs, per_page)
    page_obj = paginator.get_page(page_number)

    if request.htmx and request.htmx.target == 'datatable-body':
        return django_render(request, 'marketplace_connect/partials/marketplace_connections_list.html', {
            'marketplace_connections': page_obj, 'page_obj': page_obj,
            'search_query': search_query, 'sort_field': sort_field,
            'sort_dir': sort_dir, 'current_view': current_view, 'per_page': per_page,
        })

    return {
        'marketplace_connections': page_obj, 'page_obj': page_obj,
        'search_query': search_query, 'sort_field': sort_field,
        'sort_dir': sort_dir, 'current_view': current_view, 'per_page': per_page,
    }

@login_required
def marketplace_connection_add(request):
    hub_id = request.session.get('hub_id')
    if request.method == 'POST':
        marketplace = request.POST.get('marketplace', '').strip()
        name = request.POST.get('name', '').strip()
        status = request.POST.get('status', '').strip()
        api_key = request.POST.get('api_key', '').strip()
        last_sync_at = request.POST.get('last_sync_at') or None
        sync_enabled = request.POST.get('sync_enabled') == 'on'
        config = request.POST.get('config', '').strip()
        obj = MarketplaceConnection(hub_id=hub_id)
        obj.marketplace = marketplace
        obj.name = name
        obj.status = status
        obj.api_key = api_key
        obj.last_sync_at = last_sync_at
        obj.sync_enabled = sync_enabled
        obj.config = config
        obj.save()
        return _render_marketplace_connections_list(request, hub_id)
    return django_render(request, 'marketplace_connect/partials/panel_marketplace_connection_add.html', {})

@login_required
def marketplace_connection_edit(request, pk):
    hub_id = request.session.get('hub_id')
    obj = get_object_or_404(MarketplaceConnection, pk=pk, hub_id=hub_id, is_deleted=False)
    if request.method == 'POST':
        obj.marketplace = request.POST.get('marketplace', '').strip()
        obj.name = request.POST.get('name', '').strip()
        obj.status = request.POST.get('status', '').strip()
        obj.api_key = request.POST.get('api_key', '').strip()
        obj.last_sync_at = request.POST.get('last_sync_at') or None
        obj.sync_enabled = request.POST.get('sync_enabled') == 'on'
        obj.config = request.POST.get('config', '').strip()
        obj.save()
        return _render_marketplace_connections_list(request, hub_id)
    return django_render(request, 'marketplace_connect/partials/panel_marketplace_connection_edit.html', {'obj': obj})

@login_required
@require_POST
def marketplace_connection_delete(request, pk):
    hub_id = request.session.get('hub_id')
    obj = get_object_or_404(MarketplaceConnection, pk=pk, hub_id=hub_id, is_deleted=False)
    obj.is_deleted = True
    obj.deleted_at = timezone.now()
    obj.save(update_fields=['is_deleted', 'deleted_at', 'updated_at'])
    return _render_marketplace_connections_list(request, hub_id)

@login_required
@require_POST
def marketplace_connections_bulk_action(request):
    hub_id = request.session.get('hub_id')
    ids = [i.strip() for i in request.POST.get('ids', '').split(',') if i.strip()]
    action = request.POST.get('action', '')
    qs = MarketplaceConnection.objects.filter(hub_id=hub_id, is_deleted=False, id__in=ids)
    if action == 'delete':
        qs.update(is_deleted=True, deleted_at=timezone.now())
    return _render_marketplace_connections_list(request, hub_id)


@login_required
@with_module_nav('marketplace_connect', 'settings')
@htmx_view('marketplace_connect/pages/settings.html', 'marketplace_connect/partials/settings_content.html')
def settings_view(request):
    return {}


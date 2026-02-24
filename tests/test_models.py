"""Tests for marketplace_connect models."""
import pytest
from django.utils import timezone

from marketplace_connect.models import MarketplaceConnection


@pytest.mark.django_db
class TestMarketplaceConnection:
    """MarketplaceConnection model tests."""

    def test_create(self, marketplace_connection):
        """Test MarketplaceConnection creation."""
        assert marketplace_connection.pk is not None
        assert marketplace_connection.is_deleted is False

    def test_str(self, marketplace_connection):
        """Test string representation."""
        assert str(marketplace_connection) is not None
        assert len(str(marketplace_connection)) > 0

    def test_soft_delete(self, marketplace_connection):
        """Test soft delete."""
        pk = marketplace_connection.pk
        marketplace_connection.is_deleted = True
        marketplace_connection.deleted_at = timezone.now()
        marketplace_connection.save()
        assert not MarketplaceConnection.objects.filter(pk=pk).exists()
        assert MarketplaceConnection.all_objects.filter(pk=pk).exists()

    def test_queryset_excludes_deleted(self, hub_id, marketplace_connection):
        """Test default queryset excludes deleted."""
        marketplace_connection.is_deleted = True
        marketplace_connection.deleted_at = timezone.now()
        marketplace_connection.save()
        assert MarketplaceConnection.objects.filter(hub_id=hub_id).count() == 0



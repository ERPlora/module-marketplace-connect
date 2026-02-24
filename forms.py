from django import forms
from django.utils.translation import gettext_lazy as _

from .models import MarketplaceConnection

class MarketplaceConnectionForm(forms.ModelForm):
    class Meta:
        model = MarketplaceConnection
        fields = ['marketplace', 'name', 'status', 'api_key', 'last_sync_at', 'sync_enabled', 'config']
        widgets = {
            'marketplace': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'name': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'status': forms.Select(attrs={'class': 'select select-sm w-full'}),
            'api_key': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'last_sync_at': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'datetime-local'}),
            'sync_enabled': forms.CheckboxInput(attrs={'class': 'toggle'}),
            'config': forms.Textarea(attrs={'class': 'textarea textarea-sm w-full', 'rows': 3}),
        }


"""Action admin module."""
from django.contrib import admin
from .models import Action


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    """Register action model to admin dashboard."""

    list_display = (
        "user", "verb", "target", "created"
    )
    list_filter = ("created",)
    search_field = ("verb",)

"""Actions model."""
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models


class Action(models.Model):
    """Action model."""

    user = models.ForeignKey(
        'auth.User', related_name="actions",
        db_index=True, on_delete=models.CASCADE
    )
    verb = models.CharField(max_length=2455)
    target_ct = models.ForeignKey(
        ContentType, blank=True,
        null=True, related_name="target_obj",
        on_delete=models.CASCADE
    )
    target_id = models.PositiveIntegerField(
        null=True, blank=True, db_index=True
    )
    target = GenericForeignKey("target_ct", "target_id")
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        """Table ordering."""

        ordering = ('-created',)

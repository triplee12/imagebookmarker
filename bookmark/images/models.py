"""Image module."""
from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse


class Image(models.Model):
    """Image module."""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='image_created', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250)
    url = models.URLField()
    image = models.ImageField(upload_to="images/%Y/%m/%d/")
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True, db_index=True)
    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="images_liked", blank=True)
    total_likes = models.PositiveIntegerField(
        db_index=True, default=0
    )

    def __str__(self) -> str:
        """String representation."""
        return f'{self.title}'

    def save(self, *args, **kwargs):
        """Save slug field."""
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self) -> str:
        """Get absolute url."""
        return reverse('images:detail', args=[self.id, self.slug])

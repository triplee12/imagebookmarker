from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    photo_thumbnail = ImageSpecField(source='photo', processors = [ResizeToFill(100, 50)], format='JPEG', options={'quality': 100})

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

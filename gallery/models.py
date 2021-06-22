from django.db import models
from django.urls import reverse


class Gallery(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='gallery/')
    caption = models.CharField(max_length=500, null=True, blank=True)
    name = models.CharField(max_length=255, default='')

    def __str__(self):
        return str(self.caption)

    def get_absolute_url(self):
        return reverse('gallery-view')

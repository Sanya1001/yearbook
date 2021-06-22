from django.db import models
from django.urls import reverse


class Page(models.Model):
    name = models.CharField(max_length=255)
    quote = models.CharField(max_length=2083)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    stream = models.CharField(max_length=255)
    mail = models.EmailField(blank=True, null=True, default='')
    phone = models.CharField(max_length=10, blank=True, null=True, default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('base')


class Stream(models.Model):
    stream = models.CharField(max_length=255)

    def __str__(self):
        return self.stream

    def get_absolute_url(self):
        return reverse('base')

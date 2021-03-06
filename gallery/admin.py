from django.contrib import admin
from .models import Gallery


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('caption', 'image')


admin.site.register(Gallery)

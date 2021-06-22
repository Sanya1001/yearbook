from django.contrib import admin
from .models import Page, Stream


class PageAdmin(admin.ModelAdmin):
    list_display = ('name', 'quote')


admin.site.register(Page, PageAdmin)
admin.site.register(Stream)

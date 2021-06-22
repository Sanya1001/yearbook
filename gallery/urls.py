from django.urls import path
from .views import GalleryAdd, GalleryList


urlpatterns = [
    path('add/', GalleryAdd.as_view(), name='add-to-gallery'),
    path('', GalleryList.as_view(), name='gallery-view')
               ]

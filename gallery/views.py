from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Gallery
from .forms import GalleryForm


class GalleryAdd(CreateView):
    model = Gallery
    form_class = GalleryForm
    template_name = 'add_to_gallery.html'


class GalleryList(ListView):
    model = Gallery
    template_name = 'gallery_view.html'

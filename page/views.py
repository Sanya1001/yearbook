from django.shortcuts import render
from django.http import HttpResponse
from .models import Page
from .forms import PageForm
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView


def base(request):
    model = Page
    return render(request, 'home.html', {})


def ask_help(request):
    return render(request, 'help.html', {})


def contact(request):
    return render(request, 'contact_admin.html', {})


# def accept_form(request):
#     form = PageForm(request.POST, request.FILES or None)
#     if form.is_valid():
#         form.save()
#         form = PageForm()
#     context = {'form': form}
#     return render(request, 'form.html', context)


class HomeView(ListView):
    model = Page
    template_name = 'index.html'
    ordering = ['name']


class PageDetailView(DetailView):
    model = Page
    template_name = 'page_detail.html'


class PageAddView(CreateView):
    model = Page
    form_class = PageForm
    template_name = 'form.html'


# class UpdatePageView(UpdateView):
#     model = Page
#     template_name = 'update_page.html'
#     form_class = PageForm
#     Unused due to authentication issue


class ScienceListView(ListView):
    model = Page
    template_name = 'science_list.html'
    ordering = ['name']


class HumListView(ListView):
    model = Page
    template_name = 'hum_list.html'
    ordering = ['name']


class CommListView(ListView):
    model = Page
    template_name = 'comm_list.html'
    ordering = ['name']


class ContactDetailView(DetailView):
    model = Page
    template_name = 'contact_detail.html'

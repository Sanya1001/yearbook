from django.urls import path
from . import views

urlpatterns = [path('', views.HomeView.as_view(), name='home'),
               path('input/', views.PageAddView.as_view(), name='add-page'),
               path('<int:pk>/', views.PageDetailView.as_view(), name='page-detail'),
               path('stream/science/', views.ScienceListView.as_view(), name='science-list'),
               path('stream/humanities/', views.HumListView.as_view(), name='hum-list'),
               path('stream/commerce/', views.CommListView.as_view(), name='comm-list'),
               path('help/', views.ask_help, name='ask-help'),
               path('<int:pk>/contact/', views.ContactDetailView.as_view(), name='contact-detail'),
               path('contact/', views.contact, name='contact')
               ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/abstract/', views.abstract, name='abstract'),
    path('products/blackandwhite/', views.blackandwhite, name='blackandwhite'),
    path('products/banaras/', views.banaras, name='banaras'),
    path('products/indiantradition/', views.indiantradition, name='indiantradition'),
    path('products/asthetic/', views.asthetic, name='asthetic'),
    path('products/cityspaces/', views.cityspaces, name='cityspaces'),


]

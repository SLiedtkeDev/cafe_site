from django.urls import path
from menu import views

menu_urlpatterns = ([
    path('', views.menu_list, name='menu_list'),
], 'menus')

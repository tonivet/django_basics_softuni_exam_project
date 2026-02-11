from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.announcements_list, name='announcements-list'),
    path('create/', views.announcements_create, name='announcements-create'),
]
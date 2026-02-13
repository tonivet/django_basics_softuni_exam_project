from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.AnnouncementsListView.as_view(), name='announcements-list'),
    path('create/', views.AnnouncementsCreateView.as_view(), name='announcements-create'),
]
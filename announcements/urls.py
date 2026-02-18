from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.AnnouncementsListView.as_view(), name='announcements-list'),
    path('create/', views.AnnouncementsCreateView.as_view(), name='announcements-create'),
    path('<int:pk>/', include([
        path('update/', views.AnnouncementsUpdateView.as_view(), name='announcements-update'),
        path('delete/', views.AnnouncementsDeleteView.as_view(), name='announcements-delete'),
        ]),
    ),
]
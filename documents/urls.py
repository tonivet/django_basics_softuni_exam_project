from django.urls import path

from . import views

urlpatterns = [
    path('', views.DocumentsListView.as_view(), name='documents-list'),
    path('create/', views.DocumentCreateView.as_view(), name='documents-create'),
    path("documents/<int:pk>/download/", views.DocumentDownloadView.as_view(), name="document-download"),
    path('delete/<int:pk>/', views.DocumentDeleteView.as_view(), name='document-delete'),
]


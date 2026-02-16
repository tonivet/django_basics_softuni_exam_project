from django.urls import path

from . import views

urlpatterns = [
    path('', views.DocumentsListView.as_view(), name='documents-list'),
    path("documents/<int:pk>/download/", views.DocumentDownloadView.as_view(), name="document-download"),
]


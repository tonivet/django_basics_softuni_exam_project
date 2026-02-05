from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('condominium/resident-book/', views.resident_book, name='resident-book'),
    path('condominium/resident-book-create/', views.resident_book_create, name='resident-book-create'),
    path('condominium/resident-book-edit/<int:pk>', views.resident_book_edit, name='resident-book-edit'),
    path('condominium/resident-book-delete/<int:pk>', views.resident_book_delete, name='resident-book-delete'),
]
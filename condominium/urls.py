from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('resident-book/', include([
        path('', views.resident_book, name='resident-book'),
        path('create/', views.resident_book_create, name='resident-book-create'),
        path('<int:pk>/', include([
            path('edit/', views.resident_book_edit, name='resident-book-edit'),
            path('delete/', views.resident_book_delete, name='resident-book-delete'),
        ])),
    ]))
]
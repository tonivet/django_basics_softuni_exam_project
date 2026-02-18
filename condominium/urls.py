from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='homepage'),
    path('resident-book/', include([
        path('', views.ResidentBookListView.as_view(), name='resident-book'),
        path('create/', views.ResidentBookCreateView.as_view(), name='resident-book-create'),
        path('<int:pk>/', include([
            path('update/', views.ResidentBookUpdateView.as_view(), name='resident-book-update'),
            path('delete/', views.ResidentBookDeleteView.as_view(), name='resident-book-delete'),
        ])),
    ]))
]
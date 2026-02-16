from django.urls import path, include

from . import views

htmx_urlpatterns = [
    path('search', views.ResidentBookSearchView.as_view(), name='resident-book-search'),
    path('filter', views.ResidentBookFilterView.as_view(), name='resident-book-filter'),
]

urlpatterns = [
    path('', views.HomePageView.as_view(), name='homepage'),
    path('resident-book/', include([
        path('', views.ResidentBookListView.as_view(), name='resident-book'),
        path('create/', views.ResidentBookCreateView.as_view(), name='resident-book-create'),
        path('<int:pk>/', include([
            path('edit/', views.ResidentBookUpdateView.as_view(), name='resident-book-edit'),
            path('delete/', views.ResidentBookDeleteView.as_view(), name='resident-book-delete'),
        ])),
    ]))
] + htmx_urlpatterns
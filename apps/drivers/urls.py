from django.urls import path

from . import views

app_name = 'drivers'

urlpatterns = [
    path('', views.DriversListView.as_view(), name='list'),
    path('create/', views.DriversCreateView.as_view(),
         name='create-driver'),
    path('<int:pk>/update/', views.DriversUpdateView.as_view(),
         name='update-driver'),
    path('<int:pk>/delete/', views.DriversDeleteView.as_view(),
         name='delete-driver')
]

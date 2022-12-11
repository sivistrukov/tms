from django.urls import path

from . import views

app_name = 'counterparties'

urlpatterns = [
    path('', views.CounterpartiesListView.as_view(), name='list'),
    path('create/', views.CounterpartiesCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', views.CounterpartiesUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete', views.CounterpartiesDeleteView.as_view(), name='delete'),
]

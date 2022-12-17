from django.urls import path

from . import views

app_name = 'shipping'

urlpatterns = [
    path('', views.ShippingsListView.as_view(), name='list'),
    path('create/', views.ShippingCreateView.as_view(), name='create-shipping'),
    path('<int:pk>/edit/', views.ShippingUpdateView.as_view(), name='edit-shipping'),
    path('<int:pk>/delete/', views.ShippingDeleteView.as_view(), name='delete-shipping'),
    path('<int:pk>/sercive-complete-pdf/', views.service_complete_pdf, name='service-complete-pdf')
]

from django.urls import path

from . import views

app_name = 'assignments'

urlpatterns = [
    path('', views.AssignmentsListView.as_view(), name='list'),
    path('create/', views.AssignmentCreateView.as_view(), name='create-assignment'),
    path('edit/<int:pk>/', views.AssignmentUpdateView.as_view(), name='update-assignment'),
    path('delete/<int:pk>/', views.AssignmentDeleteView.as_view(), name='delete-assignment'),
]

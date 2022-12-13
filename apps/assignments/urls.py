from django.urls import path

from . import views

app_name = 'assignments'

urlpatterns = [
    path('', views.AssignmentsListView.as_view(), name='list'),
    path('create/', views.AssignmentCreateView.as_view(), name='create-assignment'),
    path('edit/<int:pk>/', views.AssignmentUpdateView.as_view(), name='update-assignment'),
    path('delete/<int:pk>/', views.AssignmentDeleteView.as_view(), name='delete-assignment'),

    path('create/redirect/', views.AssignmentCreateAndRedirectView.as_view(),
         name='create-assignment-redirect'),

    path('<int:assignment_id>/payloads/add', views.create_payload, name='add-payload'),
    path('<int:assignment_id>/payloads/<int:payload_id>/edit/', views.update_payload, name='edit-payload'),
    path('<int:assignment_id>/payloads/<int:pk>/delete/', views.PayloadDeleteView.as_view(),
         name='delete-payload'),
]

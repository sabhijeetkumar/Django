from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('peeps/', views.peep_list, name='list_peeps'),  # URL for listing all peeps
    path('peeps/create/', views.peep_create, name='create_peep'),  # URL for creating a new peep
    path('peeps/<int:peep_id>/edit/', views.peep_edit, name='peep_edit'),  # URL for editing a peep
    path('peeps/<int:peep_id>/delete/', views.peep_delete, name='peep_delete'),  # URL for deleting a peep
]

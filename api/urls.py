from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.project_list, name='project-list'),
    path('project/<str:pk>/', views.project_detail, name='project-detail'),
    path('project/new/', views.project_create, name='project-create'),
    path('project/<str:pk>/update', views.project_update, name='project-update'),
    path('project/<str:pk>/delete', views.project_delete, name='project-delete'),
]

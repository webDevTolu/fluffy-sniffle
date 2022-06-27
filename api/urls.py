from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


app_name = 'api'

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.project_list, name='project-list'),
    path('project/add/', views.project_add, name='project-create'),
    path('project/<str:pk>/', views.project_detail, name='project-detail'),
    path('project/<str:pk>/update', views.project_update, name='project-update'),
    path('project/<str:pk>/delete', views.project_delete, name='project-delete'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

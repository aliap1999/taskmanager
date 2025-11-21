from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'), 
    path('task/edit/<int:pk>/', views.task_edit, name='task_edit'),
    path('task/delete/<int:pk>/', views.task_delete, name='task_delete'),
]

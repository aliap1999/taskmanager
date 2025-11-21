from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'), 
]

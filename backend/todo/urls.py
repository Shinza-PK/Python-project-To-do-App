from django.urls import path, include
from .views import TodoList, TodoDetail
from rest_framework import routers
from django.urls import path
from . import views

urlpatterns = [
    
    path('todo/', views.TodoList.as_view(), name='todo-list'),
    path('todo/<int:pk>/', views.TodoDetail.as_view(), name='todo-detail'),
]

from django.urls import path, re_path
from api import views

urlpatterns = [
    path('task_lists/', views.showTaskLists),
    path('task_lists/<int:pk>/tasks/', views.task_list),
    path('task_lists/<int:pk>/', views.task_lists)
]
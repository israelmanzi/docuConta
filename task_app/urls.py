from django.urls import path
from task_app import views

urlpatterns = [
    path('', views.TaskList.as_view(), name='task_list'),
    path('/<int:pk>', views.TaskView.as_view(), name='task_view'),
    path('', views.TaskCreate.as_view(), name='task_new'),
    path('/<int:pk>', views.TaskUpdate.as_view(), name='task_edit'),
    path('/<int:pk>', views.TaskDelete.as_view(), name='task_delete'),
]
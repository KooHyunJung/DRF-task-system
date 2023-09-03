from django.urls import path

from task.views import TaskWithSubTaskDetailView, TaskListAPIMixins, TaskDetailAPIMixins

urlpatterns = [
    path('task/<int:pk>', TaskWithSubTaskDetailView.as_view()),
    path('task/list', TaskListAPIMixins.as_view()),
    path('task/detail/<int:pk>', TaskDetailAPIMixins.as_view()),
]

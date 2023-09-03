from django.urls import path

from sub_task.views import SubTaskListAPIMixins, SubTaskDetailAPIMixins

urlpatterns = [
    path('sub-task/list', SubTaskListAPIMixins.as_view()),
    path('sub-task/detail/<int:pk>', SubTaskDetailAPIMixins.as_view()),
]
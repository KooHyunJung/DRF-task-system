from django.urls import path

from user.views import UserListAPIMixins, UserDetailAPIMixins, hello_world_drf

urlpatterns = [
    path('test/', hello_world_drf),
    path('user/list', UserListAPIMixins.as_view()),
    path('user/list/<int:pk>', UserListAPIMixins.as_view()),
    path('user/detail/<int:pk>', UserDetailAPIMixins.as_view()),
]

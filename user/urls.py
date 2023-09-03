from django.urls import path

from user.views import UserAPIMixins, hello_world_drf

urlpatterns = [
    path('test/', hello_world_drf),
    path('user/', UserAPIMixins.as_view()),
    path('user/<int:id>/', UserAPIMixins.as_view()),
]

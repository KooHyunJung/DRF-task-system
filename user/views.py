from django.shortcuts import render
from rest_framework.response import Response


# test
def hello_world_drf(request):
    return Response({'msg': 'hello_world!!!'})

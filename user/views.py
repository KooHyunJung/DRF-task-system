from rest_framework import mixins, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from user.models import User
from user.serializers import UserSerializer


# test
@api_view()
def hello_world_drf(request):
    return Response({'msg': 'hello_world!!!'})


class UserListAPIMixins(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserDetailAPIMixins(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

from rest_framework.generics import CreateAPIView

from users.models import User
from users.serializers import CreateUserSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()

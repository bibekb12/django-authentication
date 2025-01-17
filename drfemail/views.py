from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer, UserCreateSerializer, UserDeleteSerializer
from django.contrib.auth.models import User


class RegisterUserView(ModelViewSet):
    queryset = User.objects.all()
    http_method_names = ["get", "post", "delete", "head", "options"]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return UserSerializer
        elif self.action == "POST":
            return UserCreateSerializer
        elif self.action == "DELETE":
            return UserDeleteSerializer
        return UserSerializer

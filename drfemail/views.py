from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from django.contrib.auth.models import User
from drfemail.tasks import send_delete_email_notification

from .serializers import UserCreateSerializer, UserDeleteSerializer, UserSerializer


class RegisterUserView(ModelViewSet):
    queryset = User.objects.all()
    http_method_names = ["get", "post", "delete", "head", "options"]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return UserSerializer
        elif self.request.method == "POST":
            return UserCreateSerializer
        elif self.request.method == "DELETE":
            return UserDeleteSerializer
        return UserSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print(instance)
        send_delete_email_notification.delay(instance.username, instance.email)
        # self.perform_destroy(instance)
        return Response("deleted")

from django.contrib.auth.models import User
from rest_framework import serializers, status
from rest_framework.response import Response

from drfemail.tasks import send_mail


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]
        extra_kwargs = {"password": {"write_only": True, "required": True}}


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True, "required": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        send_mail.apply_async(
            args=(user.username, user.email, validated_data["password"]),
            countdown=5,
        )
        return user


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]
        extra_kwargs = {"password": {"write_only": True, "required": True}}

    def delete(self, pk):
        instance = User.objects.get(pk=pk)
        instance.delete()
        return instance

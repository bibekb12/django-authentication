from rest_framework import serializers

from django.contrib.auth.models import User
from drfemail.tasks import (
    send_delete_email_notification,
    send_registration_email_notification,
)

from drfemail.models import UserInformation


class UserInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInformation
        fields = "__all__"


class CreateUserInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInformation
        fields = "__all__"

    def create(self, validated_data):
        userid = self.context["request"].user.id
        # print(userid, "-----------------")
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            user=userid,
        )
        return user

    def to_representation(self, instance):
        return {"created user information"}


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
        send_registration_email_notification.apply_async(
            args=[user.username, user.email, validated_data["password"]], countdown=10
        )
        return user


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]
        extra_kwargs = {"password": {"write_only": True, "required": True}}

    def delete(self, pk):
        instance = User.objects.get(pk=pk)
        username = instance.username
        email = instance.email
        print(f"{username}, {email}")
        breakpoint()

        try:
            send_delete_email_notification(username, email)
        except Exception as e:
            print(f"Error sending email: {e}")
        # return instance.delete()

    def to_representation(self, instance):
        return {"deleted"}

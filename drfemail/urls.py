from django.urls import path

from .views import RegisterUserView, UserInformationView

urlpatterns = [
    path("userinfo/", UserInformationView.as_view({"get": "list"}), name="userinfo"),
    path("userinfo/create/", UserInformationView.as_view({"post": "create"})),
    path(
        "register/",
        RegisterUserView.as_view({"post": "create", "get": "list"}),
        name="register",
    ),
    path("register/delete/<int:pk>", RegisterUserView.as_view({"delete": "destroy"})),
]

from django.urls import path

from .views import RegisterUserView

urlpatterns = [
    path(
        "register/",
        RegisterUserView.as_view({"post": "create", "get": "list"}),
        name="register",
    ),
    path("register/delete/<int:pk>", RegisterUserView.as_view({"delete": "destroy"})),
]

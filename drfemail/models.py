from simple_history import register
from django.contrib.auth.models import User
from django.db import models


class UserInformation(models.Model):
    user = models.IntegerField(User, default=1, null=False)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


register(
    UserInformation,
    app="history_app",
    table_name="new_History_UserInformation",
    use_base_model_db=False,
    custom_model_name=lambda x: f"History{x}",
    history_user_id_field=models.TextField(null=True, blank=True),
)


# register(
#     User,
#     app="history_app",
#     table_name="History_User",
#     use_base_model_db=False,
#     custom_model_name=lambda x: f"History{x}",
#     history_user_id_field=models.TextField(null=True, blank=True),
# )

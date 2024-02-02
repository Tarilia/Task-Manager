from django.urls import path

from task_manager.users.views import IndexUsersView, CreateUserView


urlpatterns = [
    path("", IndexUsersView.as_view(), name="index_users"),
    path("create/", CreateUserView.as_view(), name="create_users"),
]

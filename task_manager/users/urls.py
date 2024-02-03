from django.urls import path

from task_manager.users.views import (IndexUsersView, CreateUserView,
                                      UpdateUserView)


urlpatterns = [
    path("", IndexUsersView.as_view(), name="index_users"),
    path("create/", CreateUserView.as_view(), name="create_users"),
    path("<int:pk>/update/", UpdateUserView.as_view(), name="update_users"),
]

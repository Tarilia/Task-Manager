from django.urls import path

from task_manager.users.views import IndexUsersView


urlpatterns = [
    path("", IndexUsersView.as_view(), name="index_users"),
]

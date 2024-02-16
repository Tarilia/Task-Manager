from django.urls import path

from task_manager.tasks.views import (IndexTasksView, CreateTasksView,
                                      UpdateTasksView)

urlpatterns = [
    path("", IndexTasksView.as_view(), name="index_tasks"),
    path("create/", CreateTasksView.as_view(), name="create_tasks"),
    path("<int:pk>/update/", UpdateTasksView.as_view(), name="update_tasks"),
]

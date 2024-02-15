from django.urls import path

from task_manager.tasks.views import IndexTasksView, CreateTasksView

urlpatterns = [
    path("", IndexTasksView.as_view(), name="index_tasks"),
    path("create/", CreateTasksView.as_view(), name="create_tasks"),
]

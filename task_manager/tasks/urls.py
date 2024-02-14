from django.urls import path

from task_manager.tasks.views import IndexTasksView

urlpatterns = [
    path("", IndexTasksView.as_view(), name="index_tasks"),
]

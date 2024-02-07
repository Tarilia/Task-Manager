from django.urls import path

from task_manager.statuses.views import IndexStatusesView

urlpatterns = [
    path("", IndexStatusesView.as_view(), name="index_statuses"),
]

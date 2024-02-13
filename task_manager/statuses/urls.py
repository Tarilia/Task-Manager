from django.urls import path

from task_manager.statuses.views import (IndexStatusesView, CreateStatusesView,
                                         UpdateStatusesView, DeleteStatusesView)

urlpatterns = [
    path("", IndexStatusesView.as_view(), name="index_statuses"),
    path("create/", CreateStatusesView.as_view(), name="create_statuses"),
    path("<int:pk>/update/", UpdateStatusesView.as_view(),
         name="update_statuses"),
    path("<int:pk>/delete/", DeleteStatusesView.as_view(),
         name="delete_statuses"),
]

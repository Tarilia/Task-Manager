from django.urls import path

from task_manager.statuses.views import (IndexStatusesView, CreateStatusesView,
                                         UpdateStatusesView)

urlpatterns = [
    path("", IndexStatusesView.as_view(), name="index_statuses"),
    path("create/", CreateStatusesView.as_view(), name="create_statuses"),
    path("<int:pk>/update/", UpdateStatusesView.as_view(),
         name="update_statuses"),
]

from django.urls import path

from task_manager.labels.views import (IndexLabelsView, CreateLabelsView,
                                       UpdateLabelsView, DeleteLabelsView)


urlpatterns = [
    path("", IndexLabelsView.as_view(), name="index_labels"),
    path("create/", CreateLabelsView.as_view(), name="create_labels"),
    path("<int:pk>/update/", UpdateLabelsView.as_view(), name="update_labels"),
    path("<int:pk>/delete/", DeleteLabelsView.as_view(), name="delete_labels"),
]

from django.urls import path

from task_manager.labels.views import IndexLabelsView, CreateLabelsView


urlpatterns = [
    path("", IndexLabelsView.as_view(), name="index_labels"),
    path("create/", CreateLabelsView.as_view(), name="create_labels"),
]

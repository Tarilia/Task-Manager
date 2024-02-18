from django.urls import path

from task_manager.labels.views import IndexLabelsView


urlpatterns = [
    path("", IndexLabelsView.as_view(), name="index_labels"),
]

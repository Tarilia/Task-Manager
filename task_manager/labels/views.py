from django.views.generic import ListView
from django.views.generic.base import ContextMixin

from task_manager.labels.models import Label
from task_manager.utils import AuthRequiredMixin


class IndexLabelsView(AuthRequiredMixin, ListView, ContextMixin):
    template_name = "labels/index.html"
    model = Label

from django.views.generic import ListView
from django.views.generic.base import ContextMixin

from task_manager.tasks.models import Tasks
from task_manager.utils import AuthRequiredMixin


class IndexTasksView(AuthRequiredMixin, ListView, ContextMixin):
    template_name = "tasks/index.html"
    model = Tasks

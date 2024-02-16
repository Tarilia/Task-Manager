from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.base import ContextMixin
from django.utils.translation import gettext as _

from task_manager.tasks.forms import CreateTasksForm
from task_manager.tasks.models import Tasks
from task_manager.utils import AuthRequiredMixin


class IndexTasksView(AuthRequiredMixin, ListView, ContextMixin):
    template_name = "tasks/index.html"
    model = Tasks


class CreateTasksView(AuthRequiredMixin, SuccessMessageMixin,
                      CreateView):
    template_name = "tasks/create.html"
    form_class = CreateTasksForm
    success_url = reverse_lazy("index_tasks")
    success_message = _("Task created successfully")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateTasksView(AuthRequiredMixin, SuccessMessageMixin,
                      UpdateView):
    template_name = "tasks/update.html"
    model = Tasks
    form_class = CreateTasksForm
    success_url = reverse_lazy("index_tasks")
    success_message = _("Task was successfully modified")

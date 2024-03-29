from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (CreateView, UpdateView,
                                  DeleteView, DetailView)
from django.views.generic.base import ContextMixin
from django.utils.translation import gettext as _
from django_filters.views import FilterView

from task_manager.tasks.filters import TaskFilter
from task_manager.tasks.forms import CreateTasksForm
from task_manager.tasks.models import Tasks
from task_manager.utils import AuthRequiredMixin, PermissionAuthorMixin


class IndexTasksView(AuthRequiredMixin, FilterView, ContextMixin):
    template_name = "tasks/index.html"
    model = Tasks
    form_class = CreateTasksForm
    filterset_class = TaskFilter


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


class DeleteTasksView(AuthRequiredMixin, SuccessMessageMixin,
                      PermissionAuthorMixin, DeleteView):
    template_name = "tasks/delete.html"
    model = Tasks
    success_message = _("Task successfully deleted")
    success_url = reverse_lazy("index_tasks")
    no_permission_message = _('Only its author can delete a task')
    no_permission_url = reverse_lazy("index_tasks")


class DetailTasksView(AuthRequiredMixin, DetailView):
    template_name = "tasks/detail.html"
    model = Tasks

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (ListView, CreateView, UpdateView,
                                  DeleteView)
from django.views.generic.base import ContextMixin
from django.utils.translation import gettext as _

from task_manager.statuses.forms import CreateStatusesForm
from task_manager.statuses.models import Status
from task_manager.utils import AuthRequiredMixin, ProtectedDeletionMixin


class IndexStatusesView(AuthRequiredMixin, ListView, ContextMixin):
    template_name = "statuses/index.html"
    model = Status


class CreateStatusesView(AuthRequiredMixin, SuccessMessageMixin,
                         CreateView):
    template_name = "statuses/create.html"
    form_class = CreateStatusesForm
    success_url = reverse_lazy("index_statuses")
    success_message = _("Status successfully created")


class UpdateStatusesView(AuthRequiredMixin, SuccessMessageMixin,
                         UpdateView):
    template_name = "statuses/update.html"
    model = Status
    form_class = CreateStatusesForm
    success_url = reverse_lazy("index_statuses")
    success_message = _("Status changed successfully")


class DeleteStatusesView(AuthRequiredMixin, SuccessMessageMixin,
                         ProtectedDeletionMixin, DeleteView):
    template_name = "statuses/delete.html"
    model = Status
    success_url = reverse_lazy("index_statuses")
    success_message = _("Status successfully deleted")
    protected_url = reverse_lazy("index_users")
    protected_message = _('Cannot delete status because it is in use')

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (ListView, CreateView, UpdateView,
                                  DeleteView)
from django.views.generic.base import ContextMixin
from django.utils.translation import gettext as _

from task_manager.labels.forms import LabelsForm
from task_manager.labels.models import Label
from task_manager.utils import AuthRequiredMixin, ProtectedDeletionMixin


class IndexLabelsView(AuthRequiredMixin, ListView, ContextMixin):
    template_name = "labels/index.html"
    model = Label


class CreateLabelsView(AuthRequiredMixin, SuccessMessageMixin,
                       CreateView):
    template_name = "labels/create.html"
    form_class = LabelsForm
    success_url = reverse_lazy("index_labels")
    success_message = _("Label successfully created")


class UpdateLabelsView(AuthRequiredMixin, SuccessMessageMixin,
                       UpdateView):
    template_name = "labels/update.html"
    model = Label
    form_class = LabelsForm
    success_url = reverse_lazy("index_labels")
    success_message = _("Label changed successfully")


class DeleteLabelsView(AuthRequiredMixin, SuccessMessageMixin,
                       ProtectedDeletionMixin, DeleteView):
    template_name = "labels/delete.html"
    model = Label
    success_message = _("Label successfully deleted")
    success_url = reverse_lazy("index_labels")
    protected_message = _('Cannot delete label because it is in use')
    no_protected_redirect_url = reverse_lazy("index_labels")

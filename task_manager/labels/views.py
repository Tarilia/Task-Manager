from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.base import ContextMixin
from django.utils.translation import gettext as _

from task_manager.labels.forms import LabelsForm
from task_manager.labels.models import Label
from task_manager.utils import AuthRequiredMixin


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

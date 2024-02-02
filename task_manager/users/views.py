from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import ListView, CreateView
from django.views.generic.base import ContextMixin

from task_manager.users.forms import CreateUserForm


class IndexUsersView(ListView, ContextMixin):
    template_name = "users/index.html"
    model = get_user_model()


class CreateUserView(SuccessMessageMixin, CreateView):
    template_name = "users/create.html"
    form_class = CreateUserForm
    success_url = reverse_lazy("login")
    success_message = _("User is successfully registered")

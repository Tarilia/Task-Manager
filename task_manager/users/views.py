from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.base import ContextMixin

from task_manager.users.forms import CreateUserForm, UpdateUserForm
from task_manager.utils import PermissionUserMixin, AuthRequiredMixin


class IndexUsersView(ListView, ContextMixin):
    template_name = "users/index.html"
    model = get_user_model()


class CreateUserView(SuccessMessageMixin, CreateView):
    template_name = "users/create.html"
    form_class = CreateUserForm
    success_url = reverse_lazy("login")
    success_message = _("User is successfully registered")


class UpdateUserView(AuthRequiredMixin, PermissionUserMixin,
                     SuccessMessageMixin, UpdateView):
    template_name = "users/update.html"
    model = get_user_model()
    form_class = UpdateUserForm
    success_url = reverse_lazy("index_users")
    success_message = _("User changed successfully")
    no_permis_url = reverse_lazy("login")
    no_permis_message = _("You do not have permission to change another user.")

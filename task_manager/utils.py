from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext as _


class AuthRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _("You are not logged in! Please log in."))
            return redirect(reverse_lazy("login"))

        return super().dispatch(request, *args, **kwargs)


class PermissionUserMixin(UserPassesTestMixin):
    no_permis_message = None
    no_permis_url = None

    def test_func(self):
        return self.get_object() == self.request.user

    def handle_no_permission(self):
        messages.warning(self.request, self.no_permis_message)
        return redirect(self.no_permis_url)

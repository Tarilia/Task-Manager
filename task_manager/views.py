from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView

from task_manager.forms import LoginUserForm


class IndexPageView(TemplateView):
    template_name = "index.html"


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'
    next_page = reverse_lazy("index")

    def form_valid(self, form):
        messages.success(self.request, _('You are logged in'))
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request,
                         _("Please enter the correct username and password. "
                           "Both fields can be case sensitive."),)
        return self.render_to_response(self.get_context_data(form=form))


class LogoutUserView(SuccessMessageMixin, LogoutView):
    next_page = reverse_lazy("index")

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _("You are logged out"))
        return super().dispatch(request, *args, **kwargs)

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
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


class LogoutUserView(SuccessMessageMixin, LogoutView):
    next_page = reverse_lazy("index")

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _("You are logged out"))
        return super().dispatch(request, *args, **kwargs)

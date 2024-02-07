from django.contrib.auth import get_user_model
from django.views.generic import ListView
from django.views.generic.base import ContextMixin

from task_manager.utils import AuthRequiredMixin


class IndexStatusesView(AuthRequiredMixin, ListView, ContextMixin):
    template_name = "statuses/index.html"
    model = get_user_model()

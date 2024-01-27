from django.contrib.auth.models import User
from django.views.generic import ListView


class IndexUsersView(ListView):
    template_name = "users/index.html"
    model = User
    context_object_name = "users"
    ordering = ["id"]

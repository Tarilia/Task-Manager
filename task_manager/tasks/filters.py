import django_filters
from django.utils.translation import gettext_lazy as _
from django.forms import CheckboxInput

from task_manager.tasks.models import Tasks
from task_manager.labels.models import Label


class TaskFilter(django_filters.FilterSet):
    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(), field_name="labels", label=_("Label"))

    tasks = django_filters.BooleanFilter(field_name="author",
                                         label=_("Show only my tasks"),
                                         method="filter_user",
                                         widget=CheckboxInput,)

    def filter_user(self, queryset, author, value):
        current_user = self.request.user.pk
        if value:
            return queryset.filter(author=current_user)
        return queryset

    class Meta:
        model = Tasks
        fields = ['status', 'executor']

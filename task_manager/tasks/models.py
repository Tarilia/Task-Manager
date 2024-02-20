from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from task_manager.labels.models import Label
from task_manager.statuses.models import Status


class Tasks(models.Model):
    name = models.CharField(max_length=100, unique=True,
                            verbose_name=_("Name"))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    status = models.ForeignKey(Status, on_delete=models.PROTECT,
                               verbose_name=_('Status'))
    author = models.ForeignKey(get_user_model(), on_delete=models.PROTECT,
                               related_name='tasks_author',
                               verbose_name=_('Author'))
    executor = models.ForeignKey(get_user_model(), on_delete=models.PROTECT,
                                 blank=True, null=True,
                                 related_name='executor',
                                 verbose_name=_('Executor'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_("Created at"))
    labels = models.ManyToManyField(Label, through="TaskAndLabel",
                                    related_name=_("labels"),
                                    verbose_name=_("Labels"), blank=True)

    class Meta:
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")

    def __str__(self):
        return self.name


class TaskAndLabel(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)

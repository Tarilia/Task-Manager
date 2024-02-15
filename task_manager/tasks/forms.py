from django import forms

from task_manager.tasks.models import Tasks


class CreateTasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ["name", "description", "executor", "status"]

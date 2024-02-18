from django import forms

from task_manager.labels.models import Label


class LabelsForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ['name']

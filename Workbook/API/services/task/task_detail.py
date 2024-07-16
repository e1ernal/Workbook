from typing import Optional

from django import forms
from django.db.models import QuerySet
from rest_framework.exceptions import NotFound
from service_objects.services import Service

from ModelsApp.models import Task


class TaskDetailService(Service):
    task_id = forms.IntegerField()

    def process(self):
        return self._task

    @property
    def _task(self) -> Optional[Task]:
        tasks: QuerySet = Task.objects.filter(id=self.cleaned_data.get("task_id"))
        if not tasks.exists():
            raise NotFound(detail="Not found")
        return tasks.first()

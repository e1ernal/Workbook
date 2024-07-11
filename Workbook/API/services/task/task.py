from service_objects.fields import ListField
from service_objects.services import Service

from ModelsApp.models import Task


class TaskListService(Service):
    filters = ListField(required=False)

    def process(self):
        return self._tasks

    @property
    def _tasks(self):
        filters = self.cleaned_data["filters"]
        if not filters:
            return Task.objects.all()
        return Task.objects.filter(filters__name__in=filters)

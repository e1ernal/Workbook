from service_objects.services import Service

from ModelsApp.models import Task


class TaskListService(Service):
    def process(self):
        return self._tasks

    @property
    def _tasks(self):
        return Task.objects.all()


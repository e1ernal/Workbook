from django.contrib.postgres.search import TrigramSimilarity
from django.forms import CharField
from service_objects.fields import ListField
from service_objects.services import Service

from ModelsApp.models import Task


class TaskListService(Service):
    filters = ListField(required=False)
    search = CharField(required=False)

    def process(self):
        return self._tasks

    @property
    def _tasks(self):
        filters = self.cleaned_data["filters"]
        search = self.cleaned_data["search"]
        result = Task.objects.all()
        if filters:
            result = result.filter(filters__name__in=filters)
        if search:
            result = result.annotate(
                similarity=TrigramSimilarity("text", search)
            ).filter(
                similarity__gt=0.05
            ).order_by("-similarity")
        return result

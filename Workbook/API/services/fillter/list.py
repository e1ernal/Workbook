from service_objects.services import Service

from ModelsApp.models import Filter


class FilterListService(Service):

    def process(self):
        return self._filters

    @property
    def _filters(self):
        return Filter.objects.all()

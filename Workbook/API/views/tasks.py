from rest_framework.response import Response
from rest_framework.views import APIView

from API.serializers.tasks import TaskListSerializer
from API.services.task.task import TaskListService


class TaskListView(APIView):

    def get(self, request, *args, **kwargs):
        tasks = TaskListService.execute({})
        serializer = TaskListSerializer(tasks, many=True)
        return Response(serializer.data)

from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from API.serializers.tasks import TaskListSerializer, TaskDetailSerializer
from API.services.task.task import TaskListService
from API.services.task.task_detail import TaskDetailService


class TaskListView(APIView):

    def get(self, request, *args, **kwargs):
        filters = request.query_params.getlist("filters")
        tasks = TaskListService.execute({"filters": filters})
        serializer = TaskListSerializer(tasks, many=True)
        return Response(serializer.data)


class TaskDetailView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            task = TaskDetailService.execute({"task_id": kwargs["task_id"]})
            serializer = TaskDetailSerializer(task)
            return Response(serializer.data)
        except NotFound as e:
            return Response({"error": e.detail}, status=status.HTTP_404_NOT_FOUND)

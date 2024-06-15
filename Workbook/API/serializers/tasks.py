from rest_framework import serializers

from API.serializers.filters import FilterListSerializer
from API.serializers.images import ImageListSerializer
from ModelsApp.models import Task


class TaskListSerializer(serializers.ModelSerializer):
    filters = FilterListSerializer(many=True)
    images = ImageListSerializer(many=True)

    class Meta:
        model = Task
        fields = (
            'id',
            'text',
            'images',
            'solution',
            'answer',
            'filters'
        )

from rest_framework import serializers

from API.serializers.filters import FilterListSerializer
from ModelsApp.models import Task


class TaskListSerializer(serializers.ModelSerializer):
    filters = FilterListSerializer(many=True)

    class Meta:
        model = Task
        fields = (
            'id',
            'text',
            # 'text_image',
            'solution',
            'answer',
            'filters'
        )

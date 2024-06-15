from rest_framework import serializers

from API.serializers.filters import FilterListSerializer
from API.serializers.images import ImageListSerializer
from ModelsApp.models import Task, TaskImage, Image


class TaskListSerializer(serializers.ModelSerializer):
    filters = FilterListSerializer(many=True)
    images = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = (
            'id',
            'text',
            'images',
            'filters'
        )

    def get_images(self, obj):
        images = obj.taskimage_set.filter(type=TaskImage.TASK).values_list("image", flat=True)
        return ImageListSerializer(Image.objects.filter(id__in=images), many=True).data
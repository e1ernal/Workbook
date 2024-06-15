from rest_framework import serializers

from ModelsApp.models import Image


class ImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            'id',
            'image'
        )

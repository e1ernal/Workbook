from rest_framework import serializers

from ModelsApp.models import Filter


class FilterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filter
        fields = (
            'id',
            'name'
        )

from rest_framework.response import Response
from rest_framework.views import APIView

from API.serializers.filters import FilterListSerializer
from API.services.fillter.list import FilterListService


class FilterListView(APIView):

    def get(self, request, *args, **kwargs):
        filters = FilterListService.execute({})
        serializer = FilterListSerializer(filters, many=True)
        return Response(serializer.data)

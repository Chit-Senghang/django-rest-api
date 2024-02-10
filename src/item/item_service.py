from rest_framework import status
from rest_framework.response import Response

from shared_resources.common.exception.resource_not_found_exception import ResourceNotFoundException
from src.item.models import Item
from src.item.serializers import ItemSerializer


async def get_items(pk):
    try:
        item = await Item.objects.get(pk=pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Item.DoesNotExist:
        raise ResourceNotFoundException()

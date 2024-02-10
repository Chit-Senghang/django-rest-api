from django.contrib.auth.decorators import permission_required
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .item_service import get_items
from .models import Item
from .serializers import ItemSerializer


@swagger_auto_schema(
    method='GET',
    responses={200: openapi.Response(description="List of items", schema=ItemSerializer(many=True))}
)
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_required("item.view_item", raise_exception=True)
def get_all_items(request):
    paginator = PageNumberPagination()
    items = Item.objects.all()
    data = paginator.paginate_queryset(items, request)
    serializer = ItemSerializer(data, many=True)
    return paginator.get_paginated_response(serializer.data)


@swagger_auto_schema(
    method='GET',
    responses={200: openapi.Response(description="List of item", schema=ItemSerializer(many=True))}
)
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_required("item.view_item", raise_exception=True)
def get_item(req, pk):
    return get_items(pk)


@swagger_auto_schema(
    method='POST',
    request_body=ItemSerializer,
    responses={201: openapi.Response(description="Create item", schema=ItemSerializer(many=True))}
)
@api_view(['POST'])
def create_item(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='PUT',
    request_body=ItemSerializer,
    responses={200: ItemSerializer(), 400: "Bad Request", 404: "Not Found"}
)
@api_view(['PUT'])
def update_item(request, pk):
    try:
        item = Item.objects.get(pk=pk)
        serializer = ItemSerializer(instance=item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Item.DoesNotExist:
        return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)


@swagger_auto_schema(
    method='DELETE',
    responses={204: "No Content", 404: "Not Found"}
)
@api_view(['DELETE'])
def delete_item(request, pk):
    try:
        item = Item.objects.get(pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Item.DoesNotExist:
        return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

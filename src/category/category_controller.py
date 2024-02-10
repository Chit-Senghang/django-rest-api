from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from src.category.serializers import CategorySerializer
from src.item.models import Category


@swagger_auto_schema(
    method='POST',
    request_body=CategorySerializer(),
    responses={201: CategorySerializer()}
)
@api_view(['POST'])
def create_category(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@swagger_auto_schema(
    method='GET',
    responses={200: CategorySerializer()}
)
@api_view(['GET'])
def get_category(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

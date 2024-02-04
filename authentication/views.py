from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from authentication.models import User
from authentication.serializers import UserSerializer
from shared_resources.common.middleware.permission import IsAccessPermission


@swagger_auto_schema(
    method='GET',
    responses={200: UserSerializer()}
)
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAccessPermission])
def get_user(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

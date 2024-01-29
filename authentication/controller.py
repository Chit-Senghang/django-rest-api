from rest_framework import viewsets

from authentication.model.models import User
from authentication.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

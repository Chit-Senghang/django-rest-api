from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class IsAccessPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if request.user.is_authenticated:
            return True
        else:
            raise PermissionDenied("No permission")

# permissions_middleware.py
from django.http import HttpResponseForbidden


class CheckPermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Get the user's roles (groups)
            user_roles = request.user.groups.values_list('name', flat=True)
            # Check if the user has the required role or permission
            if 'admin' not in user_roles:
                return HttpResponseForbidden("Permission denied. You must be an admin.")
        raise PermissionError("Permission denied. You must be an admin.")

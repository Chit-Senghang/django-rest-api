from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_404_NOT_FOUND


class ResourceNotFoundException(APIException):
    status_code = HTTP_404_NOT_FOUND
    default_detail = 'Resource not found'
    default_code = 'resource_not_found'

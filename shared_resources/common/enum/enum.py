from cryptography.utils import Enum


class HttpMethod(Enum):
    GET = 1
    POST = 2
    PUT = 3
    DELETE = 4

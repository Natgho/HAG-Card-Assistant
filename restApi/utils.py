# Created by SezerBozkir<admin@sezerbozkir.com> at 10/26/2020
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None and response.status_code == 404:
        response.data = {
            "status": "404",
            "message": "404 Not Found"
        }

    return response

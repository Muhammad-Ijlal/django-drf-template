import logging

from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework.exceptions import ValidationError as DRFValidationError
from rest_framework.serializers import ValidationError as SerializerValidationError
from rest_framework.views import exception_handler

from .response import JSendResponse

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    """
    Custom exception handler that formats all responses in JSend format.

    Handles:
    - DRF ValidationError (including serializer validation errors)
    - Django ValidationError
    - Other DRF exceptions
    - Unhandled exceptions
    """
    # Handle DRF validation errors (including serializer validation)
    if isinstance(exc, (DRFValidationError, SerializerValidationError)):
        logger.error(f"DRF validation error: {exc}")
        return JSendResponse.fail(data=exc.detail, status_code=400)

    # Handle Django validation errors
    if isinstance(exc, DjangoValidationError):
        logger.error(f"Django validation error: {exc}")
        return JSendResponse.fail(
            data=(
                exc.message_dict
                if hasattr(exc, "message_dict")
                else {"error": exc.messages}
            ),
            status_code=400,
        )

    # Let DRF handle the exception but format it according to JSend
    response = exception_handler(exc, context)

    if response is not None:
        # Server errors (500+) are treated as "error" responses
        if response.status_code >= 500:
            logger.error(f"Server error: {exc}")
            return JSendResponse.error(
                message=str(exc), status_code=response.status_code
            )
        # Client errors (400-499) are treated as "fail" responses
        logger.error(f"Client error: {exc}")
        return JSendResponse.fail(data=response.data, status_code=response.status_code)

    # Unhandled exceptions are treated as server errors
    logger.error(f"Unhandled exception: {exc}")
    return JSendResponse.error(message="Internal Server Error", status_code=500)

from rest_framework import status
from rest_framework.response import Response


class JSendResponse:
    """JSendResponse is a utility class for creating JSend-formatted responses."""

    @staticmethod
    def success(data=None, status_code=status.HTTP_200_OK, **kwargs):
        return Response(
            {"status": "success", "data": data}, status=status_code, **kwargs
        )

    @staticmethod
    def fail(
        data=None, message=None, status_code=status.HTTP_400_BAD_REQUEST, **kwargs
    ):
        return Response({"status": "fail", "data": data}, status=status_code, **kwargs)

    @staticmethod
    def error(message, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, **kwargs):
        return Response(
            {"status": "error", "message": message}, status=status_code, **kwargs
        )


class JSendResponseMixin:
    """JSendResponseMixin to standardize responses across all views."""

    def finalize_response(self, request, response, *args, **kwargs):
        if not hasattr(response, "data"):
            return response

        if isinstance(response.data, dict) and "status" in response.data:
            return response

        if response.status_code >= 400:
            if response.status_code >= 500:
                return JSendResponse.error(
                    str(response.data), response.status_code, **kwargs
                )
            return JSendResponse.fail(response.data, response.status_code, **kwargs)

        return JSendResponse.success(response.data, response.status_code, **kwargs)

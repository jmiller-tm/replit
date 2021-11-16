import json

from third_party.python3.requests.exceptions import HTTPError


class ClientError(HTTPError):
    """A generic exception that all other exceptions of this module inherit from.

    Uses requests.exception.HTTPError as its base, which contains the request
    and response objects.

    The main purpose of this exception class, is to allow setting custom
    messages based on the API method that raises the exception.

    Args:
        err: The original HTTPError containing the request and response objects.
        message: A custom message that can include more context behind the
            API response. This will get joined with the message returned from
            the server.
    """

    def __init__(self, err=None, message=""):
        if err:
            reason = "\n".join([message, json.loads(err.response.text).get("message", "")])
            super().__init__(reason, request=err.request, response=err.response)


class NotAuthorized(ClientError):
    """The client is unauthorized; usually means credentials are missing or invalid.
    """

    def __init__(self, err):
        super().__init__(err, "Valid credentials missing from client request.")


class PermissionDenied(ClientError):
    """The client does not have permissions to access a given endpoint.

    Can also mean the requested endpoint does not exist.
    """


class BadRequest(ClientError):
    """The client has sent a request with missing or unsupported data.
    """

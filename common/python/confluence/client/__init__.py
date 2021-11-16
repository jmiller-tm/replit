"""A module that provides a client for interacting with Confluence.

Defines a class that exposes methods for making requests to the Confluence API.
The methods themselves are close approximations of what is described in the
`Confluence API documentation`_.

To use the client, you will need to provide an API token for a user. For
details on how to generated an API token, see the `API token documentation`_.

Example:
    Create an instance of the client, passing in the Confluence instance URL,
    a username (typically an e-mail address), and an API token::

        from common.python.confluence.client import ConfluenceClient

        client = ConfluenceClient(
            "https://my-confluence.com/wiki/",
            "my-user@my-domain.com",
            "my-token",
        )

        for c in client.get_content("page", "MYSPACE"):
            print(c)

Todo:
    * Add support for paginated APIs.
    * Define objects to unmarshal JSON objects into.

.. _Confluence API documentation:
   https://developer.atlassian.com/cloud/confluence/rest/
.. _API token documentation:
   https://confluence.atlassian.com/cloud/api-tokens-938839638.html
"""

import json
import mimetypes
from typing import Iterator
from urllib.parse import urljoin, quote

from third_party.python3.requests import Session
from third_party.python3.requests.exceptions import HTTPError

from common.python.confluence.client.exceptions import NotAuthorized, PermissionDenied, BadRequest


class ConfluenceClient:
    """Exposes methods for interacting with the Confluence REST API.

    Uses basic authentication to access the API, by base64 encoding the string
    formed by the format ``{username}:{token}`` and passing it as part of the
    request headers.

    Each method can handle a specific set of HTTP errors, and will decorate and
    raise an appropriate exception to be handled by the calling module. Any
    unhandled HTTP errors will be simply re-raised.

    Args:
        url: The Confluence instance URL; should end in ``/wiki/``.
            Note the trailing '/' character, this important for the URL
            join to behave correctly.
        username: The Atlassian username (email address) to authenticate as.
        token: The API token to authenticate with.
    """

    def __init__(self, url: str, username: str, token: str):
        self.url = urljoin(url, "rest/api/")
        self.username = username

        self.session = Session()
        self.session.auth = (username, token)
        self.session.headers.update(
            {
                "Accept": "application/json",
                "X-Atlassian-Token": "nocheck",  # bypass XSRF
            }
        )

    def _request(self, method: str, api: str, params: dict = {}, data=None, files=None):
        url = urljoin(self.url, api)

        response = None
        if files is not None:
            response = self.session.request(method, url, params=params, data=data, files=files)
        else:
            payload = json.dumps(data)
            response = self.session.request(
                method,
                url,
                params=params,
                data=payload,
                headers={
                    "Content-Type": "application/json",
                },
            )

        response.raise_for_status()
        return response

    def get_content(
        self, *, content_type: str = "", space: str = "", title: str = ""
    ) -> Iterator[dict]:
        """Returns content from a Confluence instance.

        ``GET /wiki/rest/api/content``

        Can optionally filter by content type, space, and title.

        Args:
            content_type: The type of content; defaults to ``page``.
                Valid values are ``page`` and `blogpost``.
            space: The key of the space to be queried for content.
            title: The title of the page to be returned.
                Required if ``content_type="page"``.

        Yields:
            JSON dictionaries representing the returned content from the given
            query.

        Raises:
            NotAuthorized: Credentials are missing from the request.
            PermissionDenied: The user does not have permissions to view the
                requested content.
        """

        try:
            results = (
                self._request(
                    "GET",
                    "content",
                    params={
                        "type": content_type,
                        "spaceKey": space,
                        "title": title,
                        "expand": [
                            "body.editor",
                        ],
                    },
                )
                .json()
                .get("results")
            )

            for content in results:
                yield content
        except HTTPError as err:
            exceptions = {
                401: NotAuthorized(err),
                404: PermissionDenied(
                    err,
                    (
                        f"The user '{self.username}' does not have permissions to "
                        "view the requested content, or it does not exist."
                    ),
                ),
            }
            raise exceptions.get(err.response.status_code) or err

    def create_content(
        self, *, content_type: str, space: str, title: str, body: str, ancestor_id: str = ""
    ) -> dict:
        """Creates a new piece of content.

        ``POST /wiki/rest/api/content``

        Can optionally provide the content ID that will be used as the parent
        of the created content.

        Args:
            content_type: The type of content to create.
                Valid values are ``page``, ``blogpost``, ``comment``, and
                ``attachment``.
            space: The key for the space to create the content in.
            title: The title of the new content.
            body: The body of the content.
            ancestor_id: The ID of the content to use as the parent.

        Returns:
            A JSON dictionary representing the created content.

        Raises:
            NotAuthorized: Credentials are missing from the request.
            PermissionDenied: The user does not have permissions to create
                content in the requested space, or the space does not exist.
        """

        try:
            data = {
                "type": content_type,
                "space": {
                    "key": space,
                },
                "title": title,
                "body": {
                    "editor": {
                        "value": body,
                        "representation": "editor",
                    },
                },
                "metadata": {
                    "properties": {
                        "editor": {
                            "value": "v2",
                        },
                    },
                },
            }

            if ancestor_id:
                data["ancestors"] = [{"id": ancestor_id}]

            return self._request("POST", "content", data=data).json()
        except HTTPError as err:
            exceptions = {
                401: NotAuthorized(err),
                404: PermissionDenied(
                    err,
                    (
                        f"The user '{self.username}' does not have permissions to "
                        f"add content to space '{space}', or it does not exist."
                    ),
                ),
            }
            raise exceptions.get(err.response.status_code) or err

    def get_content_by_id(self, *, content_id: str) -> dict:
        """Retrieve a single piece of content from an ID.

        ``GET /wiki/rest/api/content/{content_id}``

        Args:
            content_id: The ID of the content to retrieve.

        Returns:
            A JSON dictionary representing the retrieved content.

        Raises:
            NotAuthorized: Credentials are missing from the request.
            PermissionDenied: The user does not have permissions to view the
                requested content, or the content does not exist.
        """

        try:
            return self._request("GET", f"content/{content_id}").json()
        except HTTPError as err:
            exceptions = {
                401: NotAuthorized(err),
                404: PermissionDenied(
                    err,
                    (
                        f"The user '{self.username}' does not have permissions to "
                        f"view content with ID '{content_id}', or it does not exist."
                    ),
                ),
            }
            raise exceptions.get(err.response.status_code) or err

    def update_content(
        self,
        *,
        content_id: str,
        version: int,
        title: str,
        content_type: str,
        ancestor_id: str = "",
        body: str = "",
    ) -> dict:
        """Updates a piece of content at a given ID.

        ``PUT /wiki/rest/api/content/{content_id}``

        Can be used to change the title, body, or parent.

        Args:
            content_id: The ID of the content to update.
            version: The version number to publish the new content to.
                Set this to the current version, incremented by 1.
            title: The updated title of the content.
                If not changing the title, you must still set this to the
                current title.
            content_type: The type of the content to update.
                Valid values are ``page``, ``blogpost``, ``comment``, and
                ``attachment``.
            ancestor_id: The ID of the content to use as the parent.
            body: The body of the content.

        Returns:
            A JSON dictionary representing the updated content.

        Raises:
            BadRequest: The required parameters title, type, and version are
                either missing, or using unsupported values.
            NotAuthorized: Credentials are missing from the request.
        """

        try:
            data = {
                "version": {
                    "number": version,
                },
                "title": title,
                "type": content_type,
                "body": {
                    "editor": {
                        "value": body,
                        "representation": "editor",
                    },
                },
            }

            if ancestor_id:
                data["ancestors"] = [{"id": ancestor_id}]

            return self._request("PUT", f"content/{content_id}", data=data).json()
        except HTTPError as err:
            exceptions = {
                400: BadRequest(
                    err,
                    (
                        "Required parameters are missing, or using unsupported values: "
                        f"(version='{version}', type='{content_type}', title='{title}')"
                    ),
                ),
                401: NotAuthorized(err),
                409: BadRequest(
                    err,
                    (
                        "Version property has not been set correctly; must be current "
                        f"version incremented by 1, but got '{version}'."
                    ),
                ),
            }
            raise exceptions.get(err.response.status_code) or err

    def get_attachment(self, *, content_id: str, name: str):
        """Returns an attachment by the given name associated with the given Content ID.

        ``GET /wiki/rest/api/{content_id}/child/attachment``

        Args:
            content_id: The ID of the content associated with the attachment.
            name: The name of the attachment to retrieve.

        Returns:
            A JSON dictionary representing the retrieved attachment. None if the
            attachment was not found.
        """
        try:
            response = self._request(
                "GET",
                f"content/{content_id}/child/attachment",
                params={
                    "expand": ["version"],
                },
            ).json()

            # filter by name
            response["results"] = [
                attachment
                for attachment in response.get("results")
                if attachment.get("title") == name
            ]

            if len(response.get("results")) < 1:
                return None

            return self._attachment_from_response(response)
        except HTTPError as err:
            raise err

    def _attachment_from_response(self, response):
        """Adds data to attachment responses
        This function adds additional keys to the attachment response:
         - download_url: a fully-qualified download url for the attachment.
        """
        results = response.get("results")
        attachment = results[0]
        # strip off the leading / because urljoin is dumb
        download_url = attachment.get("_links").get("download")[1:]
        # add a / to the base url because urljoin is dumb
        base_url = response.get("_links").get("base") + "/"

        attachment["download_url"] = urljoin(base_url, download_url)

        return attachment

    def create_attachment(self, *, content_id: str, name: str, file_path: str, comment: str):
        """Creates an attachment associated with the given Content.

        ``POST /wiki/rest/api/content/{content_id}/child/attachment``

        Args:
            content_id: The content to associate the attachment with.
            name: The name to upload the attachment as.
            file_path: The payload of the attachment.
            comment: The comment value of the attachment.

        Returns:
            A JSON dictionary representing the uploaded attachment.
        """
        try:
            content_type = mimetypes.guess_type(file_path)[0]
            response = self._request(
                "POST",
                f"content/{content_id}/child/attachment",
                files={
                    "file": (quote(name), open(file_path, "rb"), content_type),
                },
                data={
                    "comment": comment,
                },
            ).json()

            return self._attachment_from_response(response)
        except HTTPError as err:
            raise err

    def update_attachment(self, *, content_id: str, name: str, file_path: str, comment: str):
        """Updates an attachment associated with the given Content ID by the given attachment Name.

        ``PUT /wiki/rest/api/content/{content_id}/child/attachment``

        Args:
            content_id: The content which the attachment is associated with.
            name: The attachment identified by its name to update.
            file_path: The new payload of the attachment.
            comment: The new comment value of the attachment.
        """
        try:
            content_type = mimetypes.guess_type(file_path)[0]
            response = self._request(
                "PUT",
                f"content/{content_id}/child/attachment",
                files={
                    "file": (quote(name), open(file_path, "rb"), content_type),
                },
                data={
                    "comment": comment,
                    "minorEdit": "true",
                },
            ).json()

            return self._attachment_from_response(response)
        except HTTPError as err:
            raise err

    def get_labels_for_content(self, *, content_id: str, prefix: str = "") -> Iterator[dict]:
        """Retrieves a list of labels for content at a given ID.

        ``GET /wiki/rest/api/content/{content_id}/label``

        Can optionally provide the label prefix to filter for. If not
        supplied, will return labels for any prefix.

        Args:
            content_id: The ID of the content to get labels for.
            prefix: The label prefix to filter for.
                Valid values are ``global``, ``my``, and ``team``.

        Yields:
            JSON dictionaries representing the labels.

        Raises:
            PermissionDenied: The content at the given ID does not exist,
                or the user does not have permissions to view it.
        """

        try:
            results = (
                self._request(
                    "GET",
                    f"content/{content_id}/label",
                    params={
                        "prefix": prefix,
                    },
                )
                .json()
                .get("results")
            )

            for label in results:
                yield label
        except HTTPError as err:
            exceptions = {
                404: PermissionDenied(
                    err,
                    (
                        f"The user '{self.username}' does not have permissions to "
                        f"view content with ID '{content_id}', or it does not exist."
                    ),
                ),
            }
            raise exceptions.get(err.response.status_code) or err

    def add_labels_to_content(self, content_id: str, labels: set = {}) -> Iterator[dict]:
        """Adds labels to content at a given ID.

        ``POST /wiki/rest/api/content/{content_id}/label``

        Currently only supports adding labels with the global prefix.

        Args:
            content_id: The ID of the content to add labels to.
            labels: A list of labels that will be added to the content.
                All labels will have the ``global`` prefix.

        Yields:
            JSON dictionaries representing the added labels.

        Raises:
            PermissionDenied: The content at the given ID does not exist,
                or the user does not have permissions to view it.
        """

        try:
            results = (
                self._request(
                    "POST",
                    f"content/{content_id}/label",
                    data=[{"prefix": "global", "name": name} for name in labels],
                )
                .json()
                .get("results")
            )

            for label in results:
                yield label
        except HTTPError as err:
            exceptions = {
                404: PermissionDenied(
                    err,
                    (
                        f"The user '{self.username}' does not have permissions to "
                        f"view content with ID '{content_id}', or it does not exist."
                    ),
                ),
            }
            raise exceptions.get(err.response.status_code) or err

    def remove_label_from_content(self, content_id: str, label: str):
        """Removes a label from content at a given ID.

        ``DELETE /wiki/rest/api/content/{content_id}/label/{label}``

        Can only be used with labels that do not contain the `/` character.

        Args:
            content_id: The ID of the content to remove the label from.
            label: The label to remove from the content.

        Raises:
            BadRequest: The label to be removed contains the '/' character,
                which is not supported by this endpoint.
            PermissionDenied: The content at the given ID does not exist, or
                the user does not have permissions to view or delete its labels.
        """

        try:
            self._request("DELETE", f"content/{content_id}/label/{label}")
        except HTTPError as err:
            exceptions = {
                400: BadRequest(
                    err,
                    (
                        f"The label '{label}' contains the '/' character; this is "
                        "not permitted for security reasons."
                    ),
                ),
                403: PermissionDenied(
                    err,
                    (
                        f"The user '{self.username}' does not have permissions to "
                        f"edit content with ID '{content_id}'."
                    ),
                ),
                404: PermissionDenied(
                    err,
                    (
                        f"The user '{self.username}' does not have permissions to "
                        f"view content with ID '{content_id}', or it does not exist."
                    ),
                ),
            }
            raise exceptions.get(err.response.status_code) or err

from unittest import TestCase

from third_party.python3.requests_mock import Adapter

from common.python.confluence.client import ConfluenceClient
from common.python.confluence.client.exceptions import (
    NotAuthorized, PermissionDenied, BadRequest
)


class ConfluenceClientTest(TestCase):

    CLIENT = ConfluenceClient("https://test.com/wiki/", "", "")

    TESTS = [
        {
            "func": CLIENT.get_content,
            "exceptions": {
                200: None,
                401: NotAuthorized,
                404: PermissionDenied,
            },
            "kwargs": {
                "content_type": "page",
                "space": "TEST",
                "title": "Test",
            },
            "method": "GET",
            "url": ("https://test.com/wiki/rest/api/content"
                    "?type=page&spaceKey=TEST&title=Test"),
            "response": {"results": []},
            "expected": [],
        },
        {
            "func": CLIENT.create_content,
            "exceptions": {
                200: None,
                401: NotAuthorized,
                404: PermissionDenied,
            },
            "kwargs": {
                "content_type": "page",
                "space": "TEST",
                "title": "Test",
                "body": "",
                "ancestor_id": "test",
            },
            "method": "POST",
            "url": "https://test.com/wiki/rest/api/content",
            "response": {"id": "test"},
            "expected": {"id": "test"},
        },
        {
            "func": CLIENT.get_content_by_id,
            "exceptions": {
                200: None,
                401: NotAuthorized,
                404: PermissionDenied,
            },
            "kwargs": {
                "content_id": "test",
            },
            "method": "GET",
            "url": "https://test.com/wiki/rest/api/content/test",
            "response": {"version": {"number": 1}},
            "expected": {"version": {"number": 1}},
        },
        {
            "func": CLIENT.update_content,
            "exceptions": {
                200: None,
                400: BadRequest,
                401: NotAuthorized,
                409: BadRequest,
            },
            "kwargs": {
                "content_id": "test",
                "version": 1,
                "title": "Test",
                "content_type": "page",
                "ancestor_id": "test",
            },
            "method": "PUT",
            "url": "https://test.com/wiki/rest/api/content/test",
            "response": {"id": "test"},
            "expected": {"id": "test"},
        },
        {
            "func": CLIENT.get_labels_for_content,
            "exceptions": {
                200: None,
                404: PermissionDenied,
            },
            "kwargs": {
                "content_id": "test",
            },
            "method": "GET",
            "url": "https://test.com/wiki/rest/api/content/test/label",
            "response": {"results": []},
            "expected": [],
        },
        {
            "func": CLIENT.add_labels_to_content,
            "exceptions": {
                200: None,
                404: PermissionDenied,
            },
            "kwargs": {
                "content_id": "test",
                "labels": {"test"},
            },
            "method": "POST",
            "url": "https://test.com/wiki/rest/api/content/test/label",
            "response": {"results": [{"name": "test"}]},
            "expected": [{"name": "test"}],
        },
        {
            "func": CLIENT.remove_label_from_content,
            "exceptions": {
                200: None,
                400: BadRequest,
                403: PermissionDenied,
                404: PermissionDenied,
            },
            "kwargs": {
                "content_id": "test",
                "label": "test",
            },
            "method": "DELETE",
            "url": "https://test.com/wiki/rest/api/content/test/label/test",
            "response": {},
            "expected": None,
        },
    ]

    def test_client_methods(self):
        for test in self.TESTS:
            for code, err in test["exceptions"].items():
                adapter = Adapter()
                self.CLIENT.session.mount("https://", adapter)
                adapter.register_uri(test["method"], test["url"],
                                     status_code=code, json=test["response"])

                if code != 200:
                    with self.assertRaises(err):
                        list(test["func"](**test["kwargs"]))
                else:
                    actual = test["func"](**test["kwargs"])
                    self.assertEqual(
                        test["expected"],
                        list(actual) if type(test["expected"]) == list
                        else actual
                    )

# coding: utf-8

"""
    vault/kernel/core_api/proto/v1/accounts/core_api_account_schedule_tags.proto

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PostingsApiClientsListPostingsAPIClientsResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'postings_api_clients': 'list[PostingsApiClientsPostingsAPIClient]',
        'previous_page_token': 'str',
        'next_page_token': 'str'
    }

    attribute_map = {
        'postings_api_clients': 'postings_api_clients',
        'previous_page_token': 'previous_page_token',
        'next_page_token': 'next_page_token'
    }

    def __init__(self, postings_api_clients=None, previous_page_token=None, next_page_token=None):  # noqa: E501
        """PostingsApiClientsListPostingsAPIClientsResponse - a model defined in Swagger"""  # noqa: E501
        self._postings_api_clients = None
        self._previous_page_token = None
        self._next_page_token = None
        self.discriminator = None
        if postings_api_clients is not None:
            self.postings_api_clients = postings_api_clients
        if previous_page_token is not None:
            self.previous_page_token = previous_page_token
        if next_page_token is not None:
            self.next_page_token = next_page_token

    @property
    def postings_api_clients(self):
        """Gets the postings_api_clients of this PostingsApiClientsListPostingsAPIClientsResponse.  # noqa: E501

        A list of `PostingsAPIClient` objects.  # noqa: E501

        :return: The postings_api_clients of this PostingsApiClientsListPostingsAPIClientsResponse.  # noqa: E501
        :rtype: list[PostingsApiClientsPostingsAPIClient]
        """
        return self._postings_api_clients

    @postings_api_clients.setter
    def postings_api_clients(self, postings_api_clients):
        """Sets the postings_api_clients of this PostingsApiClientsListPostingsAPIClientsResponse.

        A list of `PostingsAPIClient` objects.  # noqa: E501

        :param postings_api_clients: The postings_api_clients of this PostingsApiClientsListPostingsAPIClientsResponse.  # noqa: E501
        :type: list[PostingsApiClientsPostingsAPIClient]
        """

        self._postings_api_clients = postings_api_clients

    @property
    def previous_page_token(self):
        """Gets the previous_page_token of this PostingsApiClientsListPostingsAPIClientsResponse.  # noqa: E501

        The pagination token used to retrieve the previous page. If empty, this returns the first page of results.  # noqa: E501

        :return: The previous_page_token of this PostingsApiClientsListPostingsAPIClientsResponse.  # noqa: E501
        :rtype: str
        """
        return self._previous_page_token

    @previous_page_token.setter
    def previous_page_token(self, previous_page_token):
        """Sets the previous_page_token of this PostingsApiClientsListPostingsAPIClientsResponse.

        The pagination token used to retrieve the previous page. If empty, this returns the first page of results.  # noqa: E501

        :param previous_page_token: The previous_page_token of this PostingsApiClientsListPostingsAPIClientsResponse.  # noqa: E501
        :type: str
        """

        self._previous_page_token = previous_page_token

    @property
    def next_page_token(self):
        """Gets the next_page_token of this PostingsApiClientsListPostingsAPIClientsResponse.  # noqa: E501

        The pagination token used to retrieve the next page. If empty, this returns the last page of results.  # noqa: E501

        :return: The next_page_token of this PostingsApiClientsListPostingsAPIClientsResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_page_token

    @next_page_token.setter
    def next_page_token(self, next_page_token):
        """Sets the next_page_token of this PostingsApiClientsListPostingsAPIClientsResponse.

        The pagination token used to retrieve the next page. If empty, this returns the last page of results.  # noqa: E501

        :param next_page_token: The next_page_token of this PostingsApiClientsListPostingsAPIClientsResponse.  # noqa: E501
        :type: str
        """

        self._next_page_token = next_page_token

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PostingsApiClientsListPostingsAPIClientsResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PostingsApiClientsListPostingsAPIClientsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

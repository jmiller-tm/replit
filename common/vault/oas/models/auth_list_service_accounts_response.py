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

class AuthListServiceAccountsResponse(object):
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
        'service_accounts': 'list[AuthServiceAccount]',
        'next_page_token': 'str',
        'previous_page_token': 'str'
    }

    attribute_map = {
        'service_accounts': 'service_accounts',
        'next_page_token': 'next_page_token',
        'previous_page_token': 'previous_page_token'
    }

    def __init__(self, service_accounts=None, next_page_token=None, previous_page_token=None):  # noqa: E501
        """AuthListServiceAccountsResponse - a model defined in Swagger"""  # noqa: E501
        self._service_accounts = None
        self._next_page_token = None
        self._previous_page_token = None
        self.discriminator = None
        if service_accounts is not None:
            self.service_accounts = service_accounts
        if next_page_token is not None:
            self.next_page_token = next_page_token
        if previous_page_token is not None:
            self.previous_page_token = previous_page_token

    @property
    def service_accounts(self):
        """Gets the service_accounts of this AuthListServiceAccountsResponse.  # noqa: E501

        The list of service accounts which match the parameters of the request. Service accounts are ordered by ascending ID.  # noqa: E501

        :return: The service_accounts of this AuthListServiceAccountsResponse.  # noqa: E501
        :rtype: list[AuthServiceAccount]
        """
        return self._service_accounts

    @service_accounts.setter
    def service_accounts(self, service_accounts):
        """Sets the service_accounts of this AuthListServiceAccountsResponse.

        The list of service accounts which match the parameters of the request. Service accounts are ordered by ascending ID.  # noqa: E501

        :param service_accounts: The service_accounts of this AuthListServiceAccountsResponse.  # noqa: E501
        :type: list[AuthServiceAccount]
        """

        self._service_accounts = service_accounts

    @property
    def next_page_token(self):
        """Gets the next_page_token of this AuthListServiceAccountsResponse.  # noqa: E501

        Pagination token. This can be used as the page_token in subsequent requests to retrieve the next page of results. The next_page_token is empty when the final page of results has been reached.  # noqa: E501

        :return: The next_page_token of this AuthListServiceAccountsResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_page_token

    @next_page_token.setter
    def next_page_token(self, next_page_token):
        """Sets the next_page_token of this AuthListServiceAccountsResponse.

        Pagination token. This can be used as the page_token in subsequent requests to retrieve the next page of results. The next_page_token is empty when the final page of results has been reached.  # noqa: E501

        :param next_page_token: The next_page_token of this AuthListServiceAccountsResponse.  # noqa: E501
        :type: str
        """

        self._next_page_token = next_page_token

    @property
    def previous_page_token(self):
        """Gets the previous_page_token of this AuthListServiceAccountsResponse.  # noqa: E501

        Pagination token. This can be used as the page_token in subsequent requests to retrieve the previous page of results. The previous_page_token is empty when the first page of results has been reached.  # noqa: E501

        :return: The previous_page_token of this AuthListServiceAccountsResponse.  # noqa: E501
        :rtype: str
        """
        return self._previous_page_token

    @previous_page_token.setter
    def previous_page_token(self, previous_page_token):
        """Sets the previous_page_token of this AuthListServiceAccountsResponse.

        Pagination token. This can be used as the page_token in subsequent requests to retrieve the previous page of results. The previous_page_token is empty when the first page of results has been reached.  # noqa: E501

        :param previous_page_token: The previous_page_token of this AuthListServiceAccountsResponse.  # noqa: E501
        :type: str
        """

        self._previous_page_token = previous_page_token

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
        if issubclass(AuthListServiceAccountsResponse, dict):
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
        if not isinstance(other, AuthListServiceAccountsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

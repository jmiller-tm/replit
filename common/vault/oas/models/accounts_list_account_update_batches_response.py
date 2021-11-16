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

class AccountsListAccountUpdateBatchesResponse(object):
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
        'account_update_batches': 'list[AccountsAccountUpdateBatch]',
        'previous_page_token': 'str',
        'next_page_token': 'str'
    }

    attribute_map = {
        'account_update_batches': 'account_update_batches',
        'previous_page_token': 'previous_page_token',
        'next_page_token': 'next_page_token'
    }

    def __init__(self, account_update_batches=None, previous_page_token=None, next_page_token=None):  # noqa: E501
        """AccountsListAccountUpdateBatchesResponse - a model defined in Swagger"""  # noqa: E501
        self._account_update_batches = None
        self._previous_page_token = None
        self._next_page_token = None
        self.discriminator = None
        if account_update_batches is not None:
            self.account_update_batches = account_update_batches
        if previous_page_token is not None:
            self.previous_page_token = previous_page_token
        if next_page_token is not None:
            self.next_page_token = next_page_token

    @property
    def account_update_batches(self):
        """Gets the account_update_batches of this AccountsListAccountUpdateBatchesResponse.  # noqa: E501

        A list of matching account update batches, ordered by descending `create_timestamp`.  # noqa: E501

        :return: The account_update_batches of this AccountsListAccountUpdateBatchesResponse.  # noqa: E501
        :rtype: list[AccountsAccountUpdateBatch]
        """
        return self._account_update_batches

    @account_update_batches.setter
    def account_update_batches(self, account_update_batches):
        """Sets the account_update_batches of this AccountsListAccountUpdateBatchesResponse.

        A list of matching account update batches, ordered by descending `create_timestamp`.  # noqa: E501

        :param account_update_batches: The account_update_batches of this AccountsListAccountUpdateBatchesResponse.  # noqa: E501
        :type: list[AccountsAccountUpdateBatch]
        """

        self._account_update_batches = account_update_batches

    @property
    def previous_page_token(self):
        """Gets the previous_page_token of this AccountsListAccountUpdateBatchesResponse.  # noqa: E501

        The pagination token used to retrieve the previous page. If empty, returns the first page of results.  # noqa: E501

        :return: The previous_page_token of this AccountsListAccountUpdateBatchesResponse.  # noqa: E501
        :rtype: str
        """
        return self._previous_page_token

    @previous_page_token.setter
    def previous_page_token(self, previous_page_token):
        """Sets the previous_page_token of this AccountsListAccountUpdateBatchesResponse.

        The pagination token used to retrieve the previous page. If empty, returns the first page of results.  # noqa: E501

        :param previous_page_token: The previous_page_token of this AccountsListAccountUpdateBatchesResponse.  # noqa: E501
        :type: str
        """

        self._previous_page_token = previous_page_token

    @property
    def next_page_token(self):
        """Gets the next_page_token of this AccountsListAccountUpdateBatchesResponse.  # noqa: E501

        The pagination token used to retrieve the next page. If empty, returns the last page of results.  # noqa: E501

        :return: The next_page_token of this AccountsListAccountUpdateBatchesResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_page_token

    @next_page_token.setter
    def next_page_token(self, next_page_token):
        """Sets the next_page_token of this AccountsListAccountUpdateBatchesResponse.

        The pagination token used to retrieve the next page. If empty, returns the last page of results.  # noqa: E501

        :param next_page_token: The next_page_token of this AccountsListAccountUpdateBatchesResponse.  # noqa: E501
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
        if issubclass(AccountsListAccountUpdateBatchesResponse, dict):
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
        if not isinstance(other, AccountsListAccountUpdateBatchesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

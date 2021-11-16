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

class AccountsUpdateAccountDetailsRequest(object):
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
        'account_id': 'str',
        'request_id': 'str',
        'items_to_add': 'dict(str, str)',
        'items_to_remove': 'list[str]'
    }

    attribute_map = {
        'account_id': 'account_id',
        'request_id': 'request_id',
        'items_to_add': 'items_to_add',
        'items_to_remove': 'items_to_remove'
    }

    def __init__(self, account_id=None, request_id=None, items_to_add=None, items_to_remove=None):  # noqa: E501
        """AccountsUpdateAccountDetailsRequest - a model defined in Swagger"""  # noqa: E501
        self._account_id = None
        self._request_id = None
        self._items_to_add = None
        self._items_to_remove = None
        self.discriminator = None
        if account_id is not None:
            self.account_id = account_id
        self.request_id = request_id
        if items_to_add is not None:
            self.items_to_add = items_to_add
        if items_to_remove is not None:
            self.items_to_remove = items_to_remove

    @property
    def account_id(self):
        """Gets the account_id of this AccountsUpdateAccountDetailsRequest.  # noqa: E501

        The account that is to be updated. Required.  # noqa: E501

        :return: The account_id of this AccountsUpdateAccountDetailsRequest.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AccountsUpdateAccountDetailsRequest.

        The account that is to be updated. Required.  # noqa: E501

        :param account_id: The account_id of this AccountsUpdateAccountDetailsRequest.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def request_id(self):
        """Gets the request_id of this AccountsUpdateAccountDetailsRequest.  # noqa: E501

        A unique string ID used to ensure the request is idempotent.  Required. Max length: 512 characters.  # noqa: E501

        :return: The request_id of this AccountsUpdateAccountDetailsRequest.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this AccountsUpdateAccountDetailsRequest.

        A unique string ID used to ensure the request is idempotent.  Required. Max length: 512 characters.  # noqa: E501

        :param request_id: The request_id of this AccountsUpdateAccountDetailsRequest.  # noqa: E501
        :type: str
        """
        if request_id is None:
            raise ValueError("Invalid value for `request_id`, must not be `None`")  # noqa: E501

        self._request_id = request_id

    @property
    def items_to_add(self):
        """Gets the items_to_add of this AccountsUpdateAccountDetailsRequest.  # noqa: E501

        Map of key to item to add to the account details. If the key already exists, the value will be updated. If the key already exists and the value is set to empty, the key will be removed. Optional.  # noqa: E501

        :return: The items_to_add of this AccountsUpdateAccountDetailsRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._items_to_add

    @items_to_add.setter
    def items_to_add(self, items_to_add):
        """Sets the items_to_add of this AccountsUpdateAccountDetailsRequest.

        Map of key to item to add to the account details. If the key already exists, the value will be updated. If the key already exists and the value is set to empty, the key will be removed. Optional.  # noqa: E501

        :param items_to_add: The items_to_add of this AccountsUpdateAccountDetailsRequest.  # noqa: E501
        :type: dict(str, str)
        """

        self._items_to_add = items_to_add

    @property
    def items_to_remove(self):
        """Gets the items_to_remove of this AccountsUpdateAccountDetailsRequest.  # noqa: E501

        A list of the keys that are to be removed from the account details; removing the key also removes its value. Optional.  # noqa: E501

        :return: The items_to_remove of this AccountsUpdateAccountDetailsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._items_to_remove

    @items_to_remove.setter
    def items_to_remove(self, items_to_remove):
        """Sets the items_to_remove of this AccountsUpdateAccountDetailsRequest.

        A list of the keys that are to be removed from the account details; removing the key also removes its value. Optional.  # noqa: E501

        :param items_to_remove: The items_to_remove of this AccountsUpdateAccountDetailsRequest.  # noqa: E501
        :type: list[str]
        """

        self._items_to_remove = items_to_remove

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
        if issubclass(AccountsUpdateAccountDetailsRequest, dict):
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
        if not isinstance(other, AccountsUpdateAccountDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

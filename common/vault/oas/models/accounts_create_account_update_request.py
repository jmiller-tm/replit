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

class AccountsCreateAccountUpdateRequest(object):
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
        'request_id': 'str',
        'account_update': 'AccountsAccountUpdate'
    }

    attribute_map = {
        'request_id': 'request_id',
        'account_update': 'account_update'
    }

    def __init__(self, request_id=None, account_update=None):  # noqa: E501
        """AccountsCreateAccountUpdateRequest - a model defined in Swagger"""  # noqa: E501
        self._request_id = None
        self._account_update = None
        self.discriminator = None
        self.request_id = request_id
        if account_update is not None:
            self.account_update = account_update

    @property
    def request_id(self):
        """Gets the request_id of this AccountsCreateAccountUpdateRequest.  # noqa: E501

        A unique string ID used to ensure the request is idempotent. Required.  Required. Max length: 512 characters.  # noqa: E501

        :return: The request_id of this AccountsCreateAccountUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this AccountsCreateAccountUpdateRequest.

        A unique string ID used to ensure the request is idempotent. Required.  Required. Max length: 512 characters.  # noqa: E501

        :param request_id: The request_id of this AccountsCreateAccountUpdateRequest.  # noqa: E501
        :type: str
        """
        if request_id is None:
            raise ValueError("Invalid value for `request_id`, must not be `None`")  # noqa: E501

        self._request_id = request_id

    @property
    def account_update(self):
        """Gets the account_update of this AccountsCreateAccountUpdateRequest.  # noqa: E501


        :return: The account_update of this AccountsCreateAccountUpdateRequest.  # noqa: E501
        :rtype: AccountsAccountUpdate
        """
        return self._account_update

    @account_update.setter
    def account_update(self, account_update):
        """Sets the account_update of this AccountsCreateAccountUpdateRequest.


        :param account_update: The account_update of this AccountsCreateAccountUpdateRequest.  # noqa: E501
        :type: AccountsAccountUpdate
        """

        self._account_update = account_update

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
        if issubclass(AccountsCreateAccountUpdateRequest, dict):
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
        if not isinstance(other, AccountsCreateAccountUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

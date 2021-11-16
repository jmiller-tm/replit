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

class InternalAccountsBatchGetInternalAccountsResponse(object):
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
        'internal_accounts': 'dict(str, InternalAccountsInternalAccount)'
    }

    attribute_map = {
        'internal_accounts': 'internal_accounts'
    }

    def __init__(self, internal_accounts=None):  # noqa: E501
        """InternalAccountsBatchGetInternalAccountsResponse - a model defined in Swagger"""  # noqa: E501
        self._internal_accounts = None
        self.discriminator = None
        if internal_accounts is not None:
            self.internal_accounts = internal_accounts

    @property
    def internal_accounts(self):
        """Gets the internal_accounts of this InternalAccountsBatchGetInternalAccountsResponse.  # noqa: E501

        Map of the internal account ID to the internal account.  # noqa: E501

        :return: The internal_accounts of this InternalAccountsBatchGetInternalAccountsResponse.  # noqa: E501
        :rtype: dict(str, InternalAccountsInternalAccount)
        """
        return self._internal_accounts

    @internal_accounts.setter
    def internal_accounts(self, internal_accounts):
        """Sets the internal_accounts of this InternalAccountsBatchGetInternalAccountsResponse.

        Map of the internal account ID to the internal account.  # noqa: E501

        :param internal_accounts: The internal_accounts of this InternalAccountsBatchGetInternalAccountsResponse.  # noqa: E501
        :type: dict(str, InternalAccountsInternalAccount)
        """

        self._internal_accounts = internal_accounts

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
        if issubclass(InternalAccountsBatchGetInternalAccountsResponse, dict):
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
        if not isinstance(other, InternalAccountsBatchGetInternalAccountsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
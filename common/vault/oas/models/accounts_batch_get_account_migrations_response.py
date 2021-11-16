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

class AccountsBatchGetAccountMigrationsResponse(object):
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
        'account_migrations': 'dict(str, AccountsAccountMigration)'
    }

    attribute_map = {
        'account_migrations': 'account_migrations'
    }

    def __init__(self, account_migrations=None):  # noqa: E501
        """AccountsBatchGetAccountMigrationsResponse - a model defined in Swagger"""  # noqa: E501
        self._account_migrations = None
        self.discriminator = None
        if account_migrations is not None:
            self.account_migrations = account_migrations

    @property
    def account_migrations(self):
        """Gets the account_migrations of this AccountsBatchGetAccountMigrationsResponse.  # noqa: E501

        Map of account migration IDs to their value.  # noqa: E501

        :return: The account_migrations of this AccountsBatchGetAccountMigrationsResponse.  # noqa: E501
        :rtype: dict(str, AccountsAccountMigration)
        """
        return self._account_migrations

    @account_migrations.setter
    def account_migrations(self, account_migrations):
        """Sets the account_migrations of this AccountsBatchGetAccountMigrationsResponse.

        Map of account migration IDs to their value.  # noqa: E501

        :param account_migrations: The account_migrations of this AccountsBatchGetAccountMigrationsResponse.  # noqa: E501
        :type: dict(str, AccountsAccountMigration)
        """

        self._account_migrations = account_migrations

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
        if issubclass(AccountsBatchGetAccountMigrationsResponse, dict):
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
        if not isinstance(other, AccountsBatchGetAccountMigrationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
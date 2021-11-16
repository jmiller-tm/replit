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

class ContractsAccountNotes(object):
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
        'account_notes': 'list[AccountsCommonAccountNote]'
    }

    attribute_map = {
        'account_notes': 'account_notes'
    }

    def __init__(self, account_notes=None):  # noqa: E501
        """ContractsAccountNotes - a model defined in Swagger"""  # noqa: E501
        self._account_notes = None
        self.discriminator = None
        if account_notes is not None:
            self.account_notes = account_notes

    @property
    def account_notes(self):
        """Gets the account_notes of this ContractsAccountNotes.  # noqa: E501

        Account notes for the account.  # noqa: E501

        :return: The account_notes of this ContractsAccountNotes.  # noqa: E501
        :rtype: list[AccountsCommonAccountNote]
        """
        return self._account_notes

    @account_notes.setter
    def account_notes(self, account_notes):
        """Sets the account_notes of this ContractsAccountNotes.

        Account notes for the account.  # noqa: E501

        :param account_notes: The account_notes of this ContractsAccountNotes.  # noqa: E501
        :type: list[AccountsCommonAccountNote]
        """

        self._account_notes = account_notes

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
        if issubclass(ContractsAccountNotes, dict):
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
        if not isinstance(other, ContractsAccountNotes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

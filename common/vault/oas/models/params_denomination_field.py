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

class ParamsDenominationField(object):
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
        'permitted_denominations': 'list[str]'
    }

    attribute_map = {
        'permitted_denominations': 'permitted_denominations'
    }

    def __init__(self, permitted_denominations=None):  # noqa: E501
        """ParamsDenominationField - a model defined in Swagger"""  # noqa: E501
        self._permitted_denominations = None
        self.discriminator = None
        if permitted_denominations is not None:
            self.permitted_denominations = permitted_denominations

    @property
    def permitted_denominations(self):
        """Gets the permitted_denominations of this ParamsDenominationField.  # noqa: E501

        ISO 4217 denomination codes - empty means any denomination.  # noqa: E501

        :return: The permitted_denominations of this ParamsDenominationField.  # noqa: E501
        :rtype: list[str]
        """
        return self._permitted_denominations

    @permitted_denominations.setter
    def permitted_denominations(self, permitted_denominations):
        """Sets the permitted_denominations of this ParamsDenominationField.

        ISO 4217 denomination codes - empty means any denomination.  # noqa: E501

        :param permitted_denominations: The permitted_denominations of this ParamsDenominationField.  # noqa: E501
        :type: list[str]
        """

        self._permitted_denominations = permitted_denominations

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
        if issubclass(ParamsDenominationField, dict):
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
        if not isinstance(other, ParamsDenominationField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
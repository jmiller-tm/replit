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

class RestrictionsRestrictionDefinition(object):
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
        'restriction_type': 'RestrictionsRestrictionType',
        'required_restriction_levels': 'list[RestrictionsRestrictionLevel]'
    }

    attribute_map = {
        'restriction_type': 'restriction_type',
        'required_restriction_levels': 'required_restriction_levels'
    }

    def __init__(self, restriction_type=None, required_restriction_levels=None):  # noqa: E501
        """RestrictionsRestrictionDefinition - a model defined in Swagger"""  # noqa: E501
        self._restriction_type = None
        self._required_restriction_levels = None
        self.discriminator = None
        if restriction_type is not None:
            self.restriction_type = restriction_type
        if required_restriction_levels is not None:
            self.required_restriction_levels = required_restriction_levels

    @property
    def restriction_type(self):
        """Gets the restriction_type of this RestrictionsRestrictionDefinition.  # noqa: E501


        :return: The restriction_type of this RestrictionsRestrictionDefinition.  # noqa: E501
        :rtype: RestrictionsRestrictionType
        """
        return self._restriction_type

    @restriction_type.setter
    def restriction_type(self, restriction_type):
        """Sets the restriction_type of this RestrictionsRestrictionDefinition.


        :param restriction_type: The restriction_type of this RestrictionsRestrictionDefinition.  # noqa: E501
        :type: RestrictionsRestrictionType
        """

        self._restriction_type = restriction_type

    @property
    def required_restriction_levels(self):
        """Gets the required_restriction_levels of this RestrictionsRestrictionDefinition.  # noqa: E501

        The restriction levels required when instantiating from the definition. Required for create requests; no duplicates; may not be unknown.  # noqa: E501

        :return: The required_restriction_levels of this RestrictionsRestrictionDefinition.  # noqa: E501
        :rtype: list[RestrictionsRestrictionLevel]
        """
        return self._required_restriction_levels

    @required_restriction_levels.setter
    def required_restriction_levels(self, required_restriction_levels):
        """Sets the required_restriction_levels of this RestrictionsRestrictionDefinition.

        The restriction levels required when instantiating from the definition. Required for create requests; no duplicates; may not be unknown.  # noqa: E501

        :param required_restriction_levels: The required_restriction_levels of this RestrictionsRestrictionDefinition.  # noqa: E501
        :type: list[RestrictionsRestrictionLevel]
        """

        self._required_restriction_levels = required_restriction_levels

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
        if issubclass(RestrictionsRestrictionDefinition, dict):
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
        if not isinstance(other, RestrictionsRestrictionDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
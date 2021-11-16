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

class RestrictionsListRestrictionSetDefinitionVersionsResponse(object):
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
        'restriction_set_definition_versions': 'list[RestrictionsRestrictionSetDefinitionVersion]'
    }

    attribute_map = {
        'restriction_set_definition_versions': 'restriction_set_definition_versions'
    }

    def __init__(self, restriction_set_definition_versions=None):  # noqa: E501
        """RestrictionsListRestrictionSetDefinitionVersionsResponse - a model defined in Swagger"""  # noqa: E501
        self._restriction_set_definition_versions = None
        self.discriminator = None
        if restriction_set_definition_versions is not None:
            self.restriction_set_definition_versions = restriction_set_definition_versions

    @property
    def restriction_set_definition_versions(self):
        """Gets the restriction_set_definition_versions of this RestrictionsListRestrictionSetDefinitionVersionsResponse.  # noqa: E501

        A list of matching restriction set definition versions, ordered by ascending `create_timestamp`.  # noqa: E501

        :return: The restriction_set_definition_versions of this RestrictionsListRestrictionSetDefinitionVersionsResponse.  # noqa: E501
        :rtype: list[RestrictionsRestrictionSetDefinitionVersion]
        """
        return self._restriction_set_definition_versions

    @restriction_set_definition_versions.setter
    def restriction_set_definition_versions(self, restriction_set_definition_versions):
        """Sets the restriction_set_definition_versions of this RestrictionsListRestrictionSetDefinitionVersionsResponse.

        A list of matching restriction set definition versions, ordered by ascending `create_timestamp`.  # noqa: E501

        :param restriction_set_definition_versions: The restriction_set_definition_versions of this RestrictionsListRestrictionSetDefinitionVersionsResponse.  # noqa: E501
        :type: list[RestrictionsRestrictionSetDefinitionVersion]
        """

        self._restriction_set_definition_versions = restriction_set_definition_versions

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
        if issubclass(RestrictionsListRestrictionSetDefinitionVersionsResponse, dict):
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
        if not isinstance(other, RestrictionsListRestrictionSetDefinitionVersionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

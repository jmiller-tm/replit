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

class RestrictionsCreateRestrictionSetDefinitionVersionRequest(object):
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
        'restriction_set_definition_version': 'RestrictionsRestrictionSetDefinitionVersion',
        'request_id': 'str'
    }

    attribute_map = {
        'restriction_set_definition_version': 'restriction_set_definition_version',
        'request_id': 'request_id'
    }

    def __init__(self, restriction_set_definition_version=None, request_id=None):  # noqa: E501
        """RestrictionsCreateRestrictionSetDefinitionVersionRequest - a model defined in Swagger"""  # noqa: E501
        self._restriction_set_definition_version = None
        self._request_id = None
        self.discriminator = None
        if restriction_set_definition_version is not None:
            self.restriction_set_definition_version = restriction_set_definition_version
        self.request_id = request_id

    @property
    def restriction_set_definition_version(self):
        """Gets the restriction_set_definition_version of this RestrictionsCreateRestrictionSetDefinitionVersionRequest.  # noqa: E501


        :return: The restriction_set_definition_version of this RestrictionsCreateRestrictionSetDefinitionVersionRequest.  # noqa: E501
        :rtype: RestrictionsRestrictionSetDefinitionVersion
        """
        return self._restriction_set_definition_version

    @restriction_set_definition_version.setter
    def restriction_set_definition_version(self, restriction_set_definition_version):
        """Sets the restriction_set_definition_version of this RestrictionsCreateRestrictionSetDefinitionVersionRequest.


        :param restriction_set_definition_version: The restriction_set_definition_version of this RestrictionsCreateRestrictionSetDefinitionVersionRequest.  # noqa: E501
        :type: RestrictionsRestrictionSetDefinitionVersion
        """

        self._restriction_set_definition_version = restriction_set_definition_version

    @property
    def request_id(self):
        """Gets the request_id of this RestrictionsCreateRestrictionSetDefinitionVersionRequest.  # noqa: E501

        The unique string ID used to ensure this request is idempotent. Required.  Required. Max length: 256 characters.  # noqa: E501

        :return: The request_id of this RestrictionsCreateRestrictionSetDefinitionVersionRequest.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this RestrictionsCreateRestrictionSetDefinitionVersionRequest.

        The unique string ID used to ensure this request is idempotent. Required.  Required. Max length: 256 characters.  # noqa: E501

        :param request_id: The request_id of this RestrictionsCreateRestrictionSetDefinitionVersionRequest.  # noqa: E501
        :type: str
        """
        if request_id is None:
            raise ValueError("Invalid value for `request_id`, must not be `None`")  # noqa: E501

        self._request_id = request_id

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
        if issubclass(RestrictionsCreateRestrictionSetDefinitionVersionRequest, dict):
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
        if not isinstance(other, RestrictionsCreateRestrictionSetDefinitionVersionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

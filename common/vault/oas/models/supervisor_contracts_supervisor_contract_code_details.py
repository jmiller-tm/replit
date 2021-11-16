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

class SupervisorContractsSupervisorContractCodeDetails(object):
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
        'api_version': 'VersionSemVer',
        'display_version': 'VersionSemVer'
    }

    attribute_map = {
        'api_version': 'api_version',
        'display_version': 'display_version'
    }

    def __init__(self, api_version=None, display_version=None):  # noqa: E501
        """SupervisorContractsSupervisorContractCodeDetails - a model defined in Swagger"""  # noqa: E501
        self._api_version = None
        self._display_version = None
        self.discriminator = None
        if api_version is not None:
            self.api_version = api_version
        if display_version is not None:
            self.display_version = display_version

    @property
    def api_version(self):
        """Gets the api_version of this SupervisorContractsSupervisorContractCodeDetails.  # noqa: E501


        :return: The api_version of this SupervisorContractsSupervisorContractCodeDetails.  # noqa: E501
        :rtype: VersionSemVer
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this SupervisorContractsSupervisorContractCodeDetails.


        :param api_version: The api_version of this SupervisorContractsSupervisorContractCodeDetails.  # noqa: E501
        :type: VersionSemVer
        """

        self._api_version = api_version

    @property
    def display_version(self):
        """Gets the display_version of this SupervisorContractsSupervisorContractCodeDetails.  # noqa: E501


        :return: The display_version of this SupervisorContractsSupervisorContractCodeDetails.  # noqa: E501
        :rtype: VersionSemVer
        """
        return self._display_version

    @display_version.setter
    def display_version(self, display_version):
        """Sets the display_version of this SupervisorContractsSupervisorContractCodeDetails.


        :param display_version: The display_version of this SupervisorContractsSupervisorContractCodeDetails.  # noqa: E501
        :type: VersionSemVer
        """

        self._display_version = display_version

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
        if issubclass(SupervisorContractsSupervisorContractCodeDetails, dict):
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
        if not isinstance(other, SupervisorContractsSupervisorContractCodeDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
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

class ContractModulesSharedFunctionDetails(object):
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
        'shared_functions': 'list[ContractModulesSharedFunction]'
    }

    attribute_map = {
        'shared_functions': 'shared_functions'
    }

    def __init__(self, shared_functions=None):  # noqa: E501
        """ContractModulesSharedFunctionDetails - a model defined in Swagger"""  # noqa: E501
        self._shared_functions = None
        self.discriminator = None
        if shared_functions is not None:
            self.shared_functions = shared_functions

    @property
    def shared_functions(self):
        """Gets the shared_functions of this ContractModulesSharedFunctionDetails.  # noqa: E501

        The shared functions that are implemented in the Contract Module.  # noqa: E501

        :return: The shared_functions of this ContractModulesSharedFunctionDetails.  # noqa: E501
        :rtype: list[ContractModulesSharedFunction]
        """
        return self._shared_functions

    @shared_functions.setter
    def shared_functions(self, shared_functions):
        """Sets the shared_functions of this ContractModulesSharedFunctionDetails.

        The shared functions that are implemented in the Contract Module.  # noqa: E501

        :param shared_functions: The shared_functions of this ContractModulesSharedFunctionDetails.  # noqa: E501
        :type: list[ContractModulesSharedFunction]
        """

        self._shared_functions = shared_functions

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
        if issubclass(ContractModulesSharedFunctionDetails, dict):
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
        if not isinstance(other, ContractModulesSharedFunctionDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

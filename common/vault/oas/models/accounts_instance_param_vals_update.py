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

class AccountsInstanceParamValsUpdate(object):
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
        'instance_param_vals': 'dict(str, str)'
    }

    attribute_map = {
        'instance_param_vals': 'instance_param_vals'
    }

    def __init__(self, instance_param_vals=None):  # noqa: E501
        """AccountsInstanceParamValsUpdate - a model defined in Swagger"""  # noqa: E501
        self._instance_param_vals = None
        self.discriminator = None
        if instance_param_vals is not None:
            self.instance_param_vals = instance_param_vals

    @property
    def instance_param_vals(self):
        """Gets the instance_param_vals of this AccountsInstanceParamValsUpdate.  # noqa: E501

        The new instance parameter values that are to be applied to the account. The parameters must be non-derived instance-level parameters that have been defined in the account's Smart Contract code.  # noqa: E501

        :return: The instance_param_vals of this AccountsInstanceParamValsUpdate.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._instance_param_vals

    @instance_param_vals.setter
    def instance_param_vals(self, instance_param_vals):
        """Sets the instance_param_vals of this AccountsInstanceParamValsUpdate.

        The new instance parameter values that are to be applied to the account. The parameters must be non-derived instance-level parameters that have been defined in the account's Smart Contract code.  # noqa: E501

        :param instance_param_vals: The instance_param_vals of this AccountsInstanceParamValsUpdate.  # noqa: E501
        :type: dict(str, str)
        """

        self._instance_param_vals = instance_param_vals

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
        if issubclass(AccountsInstanceParamValsUpdate, dict):
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
        if not isinstance(other, AccountsInstanceParamValsUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
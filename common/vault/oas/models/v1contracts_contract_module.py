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

class V1contractsContractModule(object):
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
        'code': 'str',
        'contract_module_version_id': 'str'
    }

    attribute_map = {
        'code': 'code',
        'contract_module_version_id': 'contract_module_version_id'
    }

    def __init__(self, code=None, contract_module_version_id=None):  # noqa: E501
        """V1contractsContractModule - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._contract_module_version_id = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if contract_module_version_id is not None:
            self.contract_module_version_id = contract_module_version_id

    @property
    def code(self):
        """Gets the code of this V1contractsContractModule.  # noqa: E501

        Source code of the Contract Module that is to be simulated.  # noqa: E501

        :return: The code of this V1contractsContractModule.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this V1contractsContractModule.

        Source code of the Contract Module that is to be simulated.  # noqa: E501

        :param code: The code of this V1contractsContractModule.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def contract_module_version_id(self):
        """Gets the contract_module_version_id of this V1contractsContractModule.  # noqa: E501

        The ID that will be used as the Contract Module version ID in the simulation. Can be referenced by the simulation instructions.  # noqa: E501

        :return: The contract_module_version_id of this V1contractsContractModule.  # noqa: E501
        :rtype: str
        """
        return self._contract_module_version_id

    @contract_module_version_id.setter
    def contract_module_version_id(self, contract_module_version_id):
        """Sets the contract_module_version_id of this V1contractsContractModule.

        The ID that will be used as the Contract Module version ID in the simulation. Can be referenced by the simulation instructions.  # noqa: E501

        :param contract_module_version_id: The contract_module_version_id of this V1contractsContractModule.  # noqa: E501
        :type: str
        """

        self._contract_module_version_id = contract_module_version_id

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
        if issubclass(V1contractsContractModule, dict):
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
        if not isinstance(other, V1contractsContractModule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

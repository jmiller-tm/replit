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

class ContractsSupervisorContract(object):
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
        'supervisor_contract_version_id': 'str'
    }

    attribute_map = {
        'code': 'code',
        'supervisor_contract_version_id': 'supervisor_contract_version_id'
    }

    def __init__(self, code=None, supervisor_contract_version_id=None):  # noqa: E501
        """ContractsSupervisorContract - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._supervisor_contract_version_id = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if supervisor_contract_version_id is not None:
            self.supervisor_contract_version_id = supervisor_contract_version_id

    @property
    def code(self):
        """Gets the code of this ContractsSupervisorContract.  # noqa: E501

        Source code of the Supervisor Contract that is to be simulated.  # noqa: E501

        :return: The code of this ContractsSupervisorContract.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ContractsSupervisorContract.

        Source code of the Supervisor Contract that is to be simulated.  # noqa: E501

        :param code: The code of this ContractsSupervisorContract.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def supervisor_contract_version_id(self):
        """Gets the supervisor_contract_version_id of this ContractsSupervisorContract.  # noqa: E501

        The ID that will be used as the Supervisor Contract version ID in the simulation and can be referenced by the simulation instructions.  # noqa: E501

        :return: The supervisor_contract_version_id of this ContractsSupervisorContract.  # noqa: E501
        :rtype: str
        """
        return self._supervisor_contract_version_id

    @supervisor_contract_version_id.setter
    def supervisor_contract_version_id(self, supervisor_contract_version_id):
        """Sets the supervisor_contract_version_id of this ContractsSupervisorContract.

        The ID that will be used as the Supervisor Contract version ID in the simulation and can be referenced by the simulation instructions.  # noqa: E501

        :param supervisor_contract_version_id: The supervisor_contract_version_id of this ContractsSupervisorContract.  # noqa: E501
        :type: str
        """

        self._supervisor_contract_version_id = supervisor_contract_version_id

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
        if issubclass(ContractsSupervisorContract, dict):
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
        if not isinstance(other, ContractsSupervisorContract):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
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

class PlansSupervisorContractVersionUpdate(object):
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
        'supervisor_contract_version_id': 'str',
        'schedule_migration_type': 'PlansScheduleMigrationType'
    }

    attribute_map = {
        'supervisor_contract_version_id': 'supervisor_contract_version_id',
        'schedule_migration_type': 'schedule_migration_type'
    }

    def __init__(self, supervisor_contract_version_id=None, schedule_migration_type=None):  # noqa: E501
        """PlansSupervisorContractVersionUpdate - a model defined in Swagger"""  # noqa: E501
        self._supervisor_contract_version_id = None
        self._schedule_migration_type = None
        self.discriminator = None
        if supervisor_contract_version_id is not None:
            self.supervisor_contract_version_id = supervisor_contract_version_id
        if schedule_migration_type is not None:
            self.schedule_migration_type = schedule_migration_type

    @property
    def supervisor_contract_version_id(self):
        """Gets the supervisor_contract_version_id of this PlansSupervisorContractVersionUpdate.  # noqa: E501

        The ID of the Supervisor Contract version to update the plan to.  # noqa: E501

        :return: The supervisor_contract_version_id of this PlansSupervisorContractVersionUpdate.  # noqa: E501
        :rtype: str
        """
        return self._supervisor_contract_version_id

    @supervisor_contract_version_id.setter
    def supervisor_contract_version_id(self, supervisor_contract_version_id):
        """Sets the supervisor_contract_version_id of this PlansSupervisorContractVersionUpdate.

        The ID of the Supervisor Contract version to update the plan to.  # noqa: E501

        :param supervisor_contract_version_id: The supervisor_contract_version_id of this PlansSupervisorContractVersionUpdate.  # noqa: E501
        :type: str
        """

        self._supervisor_contract_version_id = supervisor_contract_version_id

    @property
    def schedule_migration_type(self):
        """Gets the schedule_migration_type of this PlansSupervisorContractVersionUpdate.  # noqa: E501


        :return: The schedule_migration_type of this PlansSupervisorContractVersionUpdate.  # noqa: E501
        :rtype: PlansScheduleMigrationType
        """
        return self._schedule_migration_type

    @schedule_migration_type.setter
    def schedule_migration_type(self, schedule_migration_type):
        """Sets the schedule_migration_type of this PlansSupervisorContractVersionUpdate.


        :param schedule_migration_type: The schedule_migration_type of this PlansSupervisorContractVersionUpdate.  # noqa: E501
        :type: PlansScheduleMigrationType
        """

        self._schedule_migration_type = schedule_migration_type

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
        if issubclass(PlansSupervisorContractVersionUpdate, dict):
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
        if not isinstance(other, PlansSupervisorContractVersionUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

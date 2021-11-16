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

class AccountsProductVersionUpdate(object):
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
        'product_version_id': 'str',
        'instance_param_vals_to_add': 'dict(str, str)',
        'schedule_migration_type': 'V1accountsScheduleMigrationType'
    }

    attribute_map = {
        'product_version_id': 'product_version_id',
        'instance_param_vals_to_add': 'instance_param_vals_to_add',
        'schedule_migration_type': 'schedule_migration_type'
    }

    def __init__(self, product_version_id=None, instance_param_vals_to_add=None, schedule_migration_type=None):  # noqa: E501
        """AccountsProductVersionUpdate - a model defined in Swagger"""  # noqa: E501
        self._product_version_id = None
        self._instance_param_vals_to_add = None
        self._schedule_migration_type = None
        self.discriminator = None
        if product_version_id is not None:
            self.product_version_id = product_version_id
        if instance_param_vals_to_add is not None:
            self.instance_param_vals_to_add = instance_param_vals_to_add
        if schedule_migration_type is not None:
            self.schedule_migration_type = schedule_migration_type

    @property
    def product_version_id(self):
        """Gets the product_version_id of this AccountsProductVersionUpdate.  # noqa: E501

        The product version ID of the product that the account is to be updated to. The product version ID can be for any type of product provided it supports all the denominations and has the same tside as the current product. For updates to product versions that make use of contract modules, each named contract module in the target product version must have a corresponding Smart Contract module versions link.  # noqa: E501

        :return: The product_version_id of this AccountsProductVersionUpdate.  # noqa: E501
        :rtype: str
        """
        return self._product_version_id

    @product_version_id.setter
    def product_version_id(self, product_version_id):
        """Sets the product_version_id of this AccountsProductVersionUpdate.

        The product version ID of the product that the account is to be updated to. The product version ID can be for any type of product provided it supports all the denominations and has the same tside as the current product. For updates to product versions that make use of contract modules, each named contract module in the target product version must have a corresponding Smart Contract module versions link.  # noqa: E501

        :param product_version_id: The product_version_id of this AccountsProductVersionUpdate.  # noqa: E501
        :type: str
        """

        self._product_version_id = product_version_id

    @property
    def instance_param_vals_to_add(self):
        """Gets the instance_param_vals_to_add of this AccountsProductVersionUpdate.  # noqa: E501

        A map from the new instance parameter name to its value, which will get added when updating the product version. All of the parameters provided must be new instance parameters defined in the product version.  # noqa: E501

        :return: The instance_param_vals_to_add of this AccountsProductVersionUpdate.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._instance_param_vals_to_add

    @instance_param_vals_to_add.setter
    def instance_param_vals_to_add(self, instance_param_vals_to_add):
        """Sets the instance_param_vals_to_add of this AccountsProductVersionUpdate.

        A map from the new instance parameter name to its value, which will get added when updating the product version. All of the parameters provided must be new instance parameters defined in the product version.  # noqa: E501

        :param instance_param_vals_to_add: The instance_param_vals_to_add of this AccountsProductVersionUpdate.  # noqa: E501
        :type: dict(str, str)
        """

        self._instance_param_vals_to_add = instance_param_vals_to_add

    @property
    def schedule_migration_type(self):
        """Gets the schedule_migration_type of this AccountsProductVersionUpdate.  # noqa: E501


        :return: The schedule_migration_type of this AccountsProductVersionUpdate.  # noqa: E501
        :rtype: V1accountsScheduleMigrationType
        """
        return self._schedule_migration_type

    @schedule_migration_type.setter
    def schedule_migration_type(self, schedule_migration_type):
        """Sets the schedule_migration_type of this AccountsProductVersionUpdate.


        :param schedule_migration_type: The schedule_migration_type of this AccountsProductVersionUpdate.  # noqa: E501
        :type: V1accountsScheduleMigrationType
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
        if issubclass(AccountsProductVersionUpdate, dict):
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
        if not isinstance(other, AccountsProductVersionUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
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

class PlansBatchGetPlanUpdatesResponse(object):
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
        'plan_updates': 'dict(str, PlansPlanUpdate)'
    }

    attribute_map = {
        'plan_updates': 'plan_updates'
    }

    def __init__(self, plan_updates=None):  # noqa: E501
        """PlansBatchGetPlanUpdatesResponse - a model defined in Swagger"""  # noqa: E501
        self._plan_updates = None
        self.discriminator = None
        if plan_updates is not None:
            self.plan_updates = plan_updates

    @property
    def plan_updates(self):
        """Gets the plan_updates of this PlansBatchGetPlanUpdatesResponse.  # noqa: E501

        A map of the plan update ID to the plan update.  # noqa: E501

        :return: The plan_updates of this PlansBatchGetPlanUpdatesResponse.  # noqa: E501
        :rtype: dict(str, PlansPlanUpdate)
        """
        return self._plan_updates

    @plan_updates.setter
    def plan_updates(self, plan_updates):
        """Sets the plan_updates of this PlansBatchGetPlanUpdatesResponse.

        A map of the plan update ID to the plan update.  # noqa: E501

        :param plan_updates: The plan_updates of this PlansBatchGetPlanUpdatesResponse.  # noqa: E501
        :type: dict(str, PlansPlanUpdate)
        """

        self._plan_updates = plan_updates

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
        if issubclass(PlansBatchGetPlanUpdatesResponse, dict):
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
        if not isinstance(other, PlansBatchGetPlanUpdatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

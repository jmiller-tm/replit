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

class AccountScheduleTagsBatchGetAccountScheduleTagsResponse(object):
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
        'account_schedule_tags': 'dict(str, AccountScheduleTagsAccountScheduleTag)'
    }

    attribute_map = {
        'account_schedule_tags': 'account_schedule_tags'
    }

    def __init__(self, account_schedule_tags=None):  # noqa: E501
        """AccountScheduleTagsBatchGetAccountScheduleTagsResponse - a model defined in Swagger"""  # noqa: E501
        self._account_schedule_tags = None
        self.discriminator = None
        if account_schedule_tags is not None:
            self.account_schedule_tags = account_schedule_tags

    @property
    def account_schedule_tags(self):
        """Gets the account_schedule_tags of this AccountScheduleTagsBatchGetAccountScheduleTagsResponse.  # noqa: E501

        A map of the AccountScheduleTag ID to the AccountScheduleTag.  # noqa: E501

        :return: The account_schedule_tags of this AccountScheduleTagsBatchGetAccountScheduleTagsResponse.  # noqa: E501
        :rtype: dict(str, AccountScheduleTagsAccountScheduleTag)
        """
        return self._account_schedule_tags

    @account_schedule_tags.setter
    def account_schedule_tags(self, account_schedule_tags):
        """Sets the account_schedule_tags of this AccountScheduleTagsBatchGetAccountScheduleTagsResponse.

        A map of the AccountScheduleTag ID to the AccountScheduleTag.  # noqa: E501

        :param account_schedule_tags: The account_schedule_tags of this AccountScheduleTagsBatchGetAccountScheduleTagsResponse.  # noqa: E501
        :type: dict(str, AccountScheduleTagsAccountScheduleTag)
        """

        self._account_schedule_tags = account_schedule_tags

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
        if issubclass(AccountScheduleTagsBatchGetAccountScheduleTagsResponse, dict):
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
        if not isinstance(other, AccountScheduleTagsBatchGetAccountScheduleTagsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
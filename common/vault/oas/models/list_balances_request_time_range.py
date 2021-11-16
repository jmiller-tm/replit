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

class ListBalancesRequestTimeRange(object):
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
        'from_value_time': 'datetime',
        'to_value_time': 'datetime',
        'exclude_starting_balance': 'bool'
    }

    attribute_map = {
        'from_value_time': 'from_value_time',
        'to_value_time': 'to_value_time',
        'exclude_starting_balance': 'exclude_starting_balance'
    }

    def __init__(self, from_value_time=None, to_value_time=None, exclude_starting_balance=None):  # noqa: E501
        """ListBalancesRequestTimeRange - a model defined in Swagger"""  # noqa: E501
        self._from_value_time = None
        self._to_value_time = None
        self._exclude_starting_balance = None
        self.discriminator = None
        if from_value_time is not None:
            self.from_value_time = from_value_time
        if to_value_time is not None:
            self.to_value_time = to_value_time
        if exclude_starting_balance is not None:
            self.exclude_starting_balance = exclude_starting_balance

    @property
    def from_value_time(self):
        """Gets the from_value_time of this ListBalancesRequestTimeRange.  # noqa: E501

        The earliest time in the time range of the returned balances. Optional. If omitted, the results will start from the first available balance.  # noqa: E501

        :return: The from_value_time of this ListBalancesRequestTimeRange.  # noqa: E501
        :rtype: datetime
        """
        return self._from_value_time

    @from_value_time.setter
    def from_value_time(self, from_value_time):
        """Sets the from_value_time of this ListBalancesRequestTimeRange.

        The earliest time in the time range of the returned balances. Optional. If omitted, the results will start from the first available balance.  # noqa: E501

        :param from_value_time: The from_value_time of this ListBalancesRequestTimeRange.  # noqa: E501
        :type: datetime
        """

        self._from_value_time = from_value_time

    @property
    def to_value_time(self):
        """Gets the to_value_time of this ListBalancesRequestTimeRange.  # noqa: E501

        The latest time in the time range of the returned balances. Optional. If omitted, the results will end at the last available balance.  # noqa: E501

        :return: The to_value_time of this ListBalancesRequestTimeRange.  # noqa: E501
        :rtype: datetime
        """
        return self._to_value_time

    @to_value_time.setter
    def to_value_time(self, to_value_time):
        """Sets the to_value_time of this ListBalancesRequestTimeRange.

        The latest time in the time range of the returned balances. Optional. If omitted, the results will end at the last available balance.  # noqa: E501

        :param to_value_time: The to_value_time of this ListBalancesRequestTimeRange.  # noqa: E501
        :type: datetime
        """

        self._to_value_time = to_value_time

    @property
    def exclude_starting_balance(self):
        """Gets the exclude_starting_balance of this ListBalancesRequestTimeRange.  # noqa: E501

        True returns balances that only fall within the provided time range. False includes the latest balance entries before the provided from_value_time. Default is false.  # noqa: E501

        :return: The exclude_starting_balance of this ListBalancesRequestTimeRange.  # noqa: E501
        :rtype: bool
        """
        return self._exclude_starting_balance

    @exclude_starting_balance.setter
    def exclude_starting_balance(self, exclude_starting_balance):
        """Sets the exclude_starting_balance of this ListBalancesRequestTimeRange.

        True returns balances that only fall within the provided time range. False includes the latest balance entries before the provided from_value_time. Default is false.  # noqa: E501

        :param exclude_starting_balance: The exclude_starting_balance of this ListBalancesRequestTimeRange.  # noqa: E501
        :type: bool
        """

        self._exclude_starting_balance = exclude_starting_balance

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
        if issubclass(ListBalancesRequestTimeRange, dict):
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
        if not isinstance(other, ListBalancesRequestTimeRange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
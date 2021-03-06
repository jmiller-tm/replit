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

class SmartContractsSetFlagEvent(object):
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
        'flag_definition_id': 'str',
        'effective_timestamp': 'datetime',
        'expiry_timestamp': 'datetime'
    }

    attribute_map = {
        'flag_definition_id': 'flag_definition_id',
        'effective_timestamp': 'effective_timestamp',
        'expiry_timestamp': 'expiry_timestamp'
    }

    def __init__(self, flag_definition_id=None, effective_timestamp=None, expiry_timestamp=None):  # noqa: E501
        """SmartContractsSetFlagEvent - a model defined in Swagger"""  # noqa: E501
        self._flag_definition_id = None
        self._effective_timestamp = None
        self._expiry_timestamp = None
        self.discriminator = None
        if flag_definition_id is not None:
            self.flag_definition_id = flag_definition_id
        if effective_timestamp is not None:
            self.effective_timestamp = effective_timestamp
        if expiry_timestamp is not None:
            self.expiry_timestamp = expiry_timestamp

    @property
    def flag_definition_id(self):
        """Gets the flag_definition_id of this SmartContractsSetFlagEvent.  # noqa: E501

        ID of the flag.  # noqa: E501

        :return: The flag_definition_id of this SmartContractsSetFlagEvent.  # noqa: E501
        :rtype: str
        """
        return self._flag_definition_id

    @flag_definition_id.setter
    def flag_definition_id(self, flag_definition_id):
        """Sets the flag_definition_id of this SmartContractsSetFlagEvent.

        ID of the flag.  # noqa: E501

        :param flag_definition_id: The flag_definition_id of this SmartContractsSetFlagEvent.  # noqa: E501
        :type: str
        """

        self._flag_definition_id = flag_definition_id

    @property
    def effective_timestamp(self):
        """Gets the effective_timestamp of this SmartContractsSetFlagEvent.  # noqa: E501

        The time the flag becomes effective.  # noqa: E501

        :return: The effective_timestamp of this SmartContractsSetFlagEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_timestamp

    @effective_timestamp.setter
    def effective_timestamp(self, effective_timestamp):
        """Sets the effective_timestamp of this SmartContractsSetFlagEvent.

        The time the flag becomes effective.  # noqa: E501

        :param effective_timestamp: The effective_timestamp of this SmartContractsSetFlagEvent.  # noqa: E501
        :type: datetime
        """

        self._effective_timestamp = effective_timestamp

    @property
    def expiry_timestamp(self):
        """Gets the expiry_timestamp of this SmartContractsSetFlagEvent.  # noqa: E501

        The time the flag expires.  # noqa: E501

        :return: The expiry_timestamp of this SmartContractsSetFlagEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry_timestamp

    @expiry_timestamp.setter
    def expiry_timestamp(self, expiry_timestamp):
        """Sets the expiry_timestamp of this SmartContractsSetFlagEvent.

        The time the flag expires.  # noqa: E501

        :param expiry_timestamp: The expiry_timestamp of this SmartContractsSetFlagEvent.  # noqa: E501
        :type: datetime
        """

        self._expiry_timestamp = expiry_timestamp

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
        if issubclass(SmartContractsSetFlagEvent, dict):
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
        if not isinstance(other, SmartContractsSetFlagEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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

class PaymentOrdersParty(object):
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
        'routing_info_type': 'str',
        'identification': 'str',
        'name': 'str'
    }

    attribute_map = {
        'routing_info_type': 'routing_info_type',
        'identification': 'identification',
        'name': 'name'
    }

    def __init__(self, routing_info_type=None, identification=None, name=None):  # noqa: E501
        """PaymentOrdersParty - a model defined in Swagger"""  # noqa: E501
        self._routing_info_type = None
        self._identification = None
        self._name = None
        self.discriminator = None
        if routing_info_type is not None:
            self.routing_info_type = routing_info_type
        if identification is not None:
            self.identification = identification
        if name is not None:
            self.name = name

    @property
    def routing_info_type(self):
        """Gets the routing_info_type of this PaymentOrdersParty.  # noqa: E501

        The type of routing info (eg. \"IBAN\", \"UK.SortCodeAccountNumber\").  # noqa: E501

        :return: The routing_info_type of this PaymentOrdersParty.  # noqa: E501
        :rtype: str
        """
        return self._routing_info_type

    @routing_info_type.setter
    def routing_info_type(self, routing_info_type):
        """Sets the routing_info_type of this PaymentOrdersParty.

        The type of routing info (eg. \"IBAN\", \"UK.SortCodeAccountNumber\").  # noqa: E501

        :param routing_info_type: The routing_info_type of this PaymentOrdersParty.  # noqa: E501
        :type: str
        """

        self._routing_info_type = routing_info_type

    @property
    def identification(self):
        """Gets the identification of this PaymentOrdersParty.  # noqa: E501

        Identification of the party account under the routing info type (eg. \"08080021325698\").  # noqa: E501

        :return: The identification of this PaymentOrdersParty.  # noqa: E501
        :rtype: str
        """
        return self._identification

    @identification.setter
    def identification(self, identification):
        """Sets the identification of this PaymentOrdersParty.

        Identification of the party account under the routing info type (eg. \"08080021325698\").  # noqa: E501

        :param identification: The identification of this PaymentOrdersParty.  # noqa: E501
        :type: str
        """

        self._identification = identification

    @property
    def name(self):
        """Gets the name of this PaymentOrdersParty.  # noqa: E501

        The customer name associated with the party account.  # noqa: E501

        :return: The name of this PaymentOrdersParty.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PaymentOrdersParty.

        The customer name associated with the party account.  # noqa: E501

        :param name: The name of this PaymentOrdersParty.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(PaymentOrdersParty, dict):
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
        if not isinstance(other, PaymentOrdersParty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

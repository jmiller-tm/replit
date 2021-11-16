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

class PaymentDevicesBatchGetPaymentDeviceLinksResponse(object):
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
        'payment_device_links': 'dict(str, PaymentDevicesPaymentDeviceLink)'
    }

    attribute_map = {
        'payment_device_links': 'payment_device_links'
    }

    def __init__(self, payment_device_links=None):  # noqa: E501
        """PaymentDevicesBatchGetPaymentDeviceLinksResponse - a model defined in Swagger"""  # noqa: E501
        self._payment_device_links = None
        self.discriminator = None
        if payment_device_links is not None:
            self.payment_device_links = payment_device_links

    @property
    def payment_device_links(self):
        """Gets the payment_device_links of this PaymentDevicesBatchGetPaymentDeviceLinksResponse.  # noqa: E501

        Map of requested ids to their payment device links.  # noqa: E501

        :return: The payment_device_links of this PaymentDevicesBatchGetPaymentDeviceLinksResponse.  # noqa: E501
        :rtype: dict(str, PaymentDevicesPaymentDeviceLink)
        """
        return self._payment_device_links

    @payment_device_links.setter
    def payment_device_links(self, payment_device_links):
        """Sets the payment_device_links of this PaymentDevicesBatchGetPaymentDeviceLinksResponse.

        Map of requested ids to their payment device links.  # noqa: E501

        :param payment_device_links: The payment_device_links of this PaymentDevicesBatchGetPaymentDeviceLinksResponse.  # noqa: E501
        :type: dict(str, PaymentDevicesPaymentDeviceLink)
        """

        self._payment_device_links = payment_device_links

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
        if issubclass(PaymentDevicesBatchGetPaymentDeviceLinksResponse, dict):
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
        if not isinstance(other, PaymentDevicesBatchGetPaymentDeviceLinksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

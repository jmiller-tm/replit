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

class PaymentOrdersListPaymentOrdersResponse(object):
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
        'payment_orders': 'list[PaymentOrdersPaymentOrder]',
        'previous_page_token': 'str',
        'next_page_token': 'str'
    }

    attribute_map = {
        'payment_orders': 'payment_orders',
        'previous_page_token': 'previous_page_token',
        'next_page_token': 'next_page_token'
    }

    def __init__(self, payment_orders=None, previous_page_token=None, next_page_token=None):  # noqa: E501
        """PaymentOrdersListPaymentOrdersResponse - a model defined in Swagger"""  # noqa: E501
        self._payment_orders = None
        self._previous_page_token = None
        self._next_page_token = None
        self.discriminator = None
        if payment_orders is not None:
            self.payment_orders = payment_orders
        if previous_page_token is not None:
            self.previous_page_token = previous_page_token
        if next_page_token is not None:
            self.next_page_token = next_page_token

    @property
    def payment_orders(self):
        """Gets the payment_orders of this PaymentOrdersListPaymentOrdersResponse.  # noqa: E501

        A list of matching PaymentOrders in order of descending create_timestamp (most recent first).  # noqa: E501

        :return: The payment_orders of this PaymentOrdersListPaymentOrdersResponse.  # noqa: E501
        :rtype: list[PaymentOrdersPaymentOrder]
        """
        return self._payment_orders

    @payment_orders.setter
    def payment_orders(self, payment_orders):
        """Sets the payment_orders of this PaymentOrdersListPaymentOrdersResponse.

        A list of matching PaymentOrders in order of descending create_timestamp (most recent first).  # noqa: E501

        :param payment_orders: The payment_orders of this PaymentOrdersListPaymentOrdersResponse.  # noqa: E501
        :type: list[PaymentOrdersPaymentOrder]
        """

        self._payment_orders = payment_orders

    @property
    def previous_page_token(self):
        """Gets the previous_page_token of this PaymentOrdersListPaymentOrdersResponse.  # noqa: E501

        Token used to retrieve the previous page. If empty, returns the first page of results.  # noqa: E501

        :return: The previous_page_token of this PaymentOrdersListPaymentOrdersResponse.  # noqa: E501
        :rtype: str
        """
        return self._previous_page_token

    @previous_page_token.setter
    def previous_page_token(self, previous_page_token):
        """Sets the previous_page_token of this PaymentOrdersListPaymentOrdersResponse.

        Token used to retrieve the previous page. If empty, returns the first page of results.  # noqa: E501

        :param previous_page_token: The previous_page_token of this PaymentOrdersListPaymentOrdersResponse.  # noqa: E501
        :type: str
        """

        self._previous_page_token = previous_page_token

    @property
    def next_page_token(self):
        """Gets the next_page_token of this PaymentOrdersListPaymentOrdersResponse.  # noqa: E501

        Token used to retrieve the next page. If empty, returns the last page of results.  # noqa: E501

        :return: The next_page_token of this PaymentOrdersListPaymentOrdersResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_page_token

    @next_page_token.setter
    def next_page_token(self, next_page_token):
        """Sets the next_page_token of this PaymentOrdersListPaymentOrdersResponse.

        Token used to retrieve the next page. If empty, returns the last page of results.  # noqa: E501

        :param next_page_token: The next_page_token of this PaymentOrdersListPaymentOrdersResponse.  # noqa: E501
        :type: str
        """

        self._next_page_token = next_page_token

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
        if issubclass(PaymentOrdersListPaymentOrdersResponse, dict):
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
        if not isinstance(other, PaymentOrdersListPaymentOrdersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

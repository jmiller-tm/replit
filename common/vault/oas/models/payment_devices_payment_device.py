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

class PaymentDevicesPaymentDevice(object):
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
        'id': 'str',
        'routing_info': 'dict(str, str)',
        'status': 'PaymentDevicesPaymentDeviceStatus',
        'create_timestamp': 'datetime',
        'start_timestamp': 'datetime',
        'end_timestamp': 'datetime',
        'tags': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'routing_info': 'routing_info',
        'status': 'status',
        'create_timestamp': 'create_timestamp',
        'start_timestamp': 'start_timestamp',
        'end_timestamp': 'end_timestamp',
        'tags': 'tags'
    }

    def __init__(self, id=None, routing_info=None, status=None, create_timestamp=None, start_timestamp=None, end_timestamp=None, tags=None):  # noqa: E501
        """PaymentDevicesPaymentDevice - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._routing_info = None
        self._status = None
        self._create_timestamp = None
        self._start_timestamp = None
        self._end_timestamp = None
        self._tags = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if routing_info is not None:
            self.routing_info = routing_info
        if status is not None:
            self.status = status
        if create_timestamp is not None:
            self.create_timestamp = create_timestamp
        if start_timestamp is not None:
            self.start_timestamp = start_timestamp
        if end_timestamp is not None:
            self.end_timestamp = end_timestamp
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        """Gets the id of this PaymentDevicesPaymentDevice.  # noqa: E501

        Caller injected or Vault auto-generated unique ID for payment device. Optional. When auto-generated, this is a UUID in the canonical 8-4-4-4-12 form.  Max length: 36 characters.  # noqa: E501

        :return: The id of this PaymentDevicesPaymentDevice.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentDevicesPaymentDevice.

        Caller injected or Vault auto-generated unique ID for payment device. Optional. When auto-generated, this is a UUID in the canonical 8-4-4-4-12 form.  Max length: 36 characters.  # noqa: E501

        :param id: The id of this PaymentDevicesPaymentDevice.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def routing_info(self):
        """Gets the routing_info of this PaymentDevicesPaymentDevice.  # noqa: E501

        Key -> value map for caller to reference when receiving/originating payment. Optional.   # noqa: E501

        :return: The routing_info of this PaymentDevicesPaymentDevice.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._routing_info

    @routing_info.setter
    def routing_info(self, routing_info):
        """Sets the routing_info of this PaymentDevicesPaymentDevice.

        Key -> value map for caller to reference when receiving/originating payment. Optional.   # noqa: E501

        :param routing_info: The routing_info of this PaymentDevicesPaymentDevice.  # noqa: E501
        :type: dict(str, str)
        """

        self._routing_info = routing_info

    @property
    def status(self):
        """Gets the status of this PaymentDevicesPaymentDevice.  # noqa: E501


        :return: The status of this PaymentDevicesPaymentDevice.  # noqa: E501
        :rtype: PaymentDevicesPaymentDeviceStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PaymentDevicesPaymentDevice.


        :param status: The status of this PaymentDevicesPaymentDevice.  # noqa: E501
        :type: PaymentDevicesPaymentDeviceStatus
        """

        self._status = status

    @property
    def create_timestamp(self):
        """Gets the create_timestamp of this PaymentDevicesPaymentDevice.  # noqa: E501

        Create timestamp. Differs from effective timestamp if created in pending. Output only.  # noqa: E501

        :return: The create_timestamp of this PaymentDevicesPaymentDevice.  # noqa: E501
        :rtype: datetime
        """
        return self._create_timestamp

    @create_timestamp.setter
    def create_timestamp(self, create_timestamp):
        """Sets the create_timestamp of this PaymentDevicesPaymentDevice.

        Create timestamp. Differs from effective timestamp if created in pending. Output only.  # noqa: E501

        :param create_timestamp: The create_timestamp of this PaymentDevicesPaymentDevice.  # noqa: E501
        :type: datetime
        """

        self._create_timestamp = create_timestamp

    @property
    def start_timestamp(self):
        """Gets the start_timestamp of this PaymentDevicesPaymentDevice.  # noqa: E501

        When the payment device became active if the value is historic, or when the payment device will become active if the value is in the future. Defaults to current time when creating a payment device in `PAYMENT_DEVICE_STATUS_ACTIVE` status. Required for creating a payment device with status `PAYMENT_DEVICE_STATUS_INACTIVE`, optional for other create requests, and output only otherwise.   # noqa: E501

        :return: The start_timestamp of this PaymentDevicesPaymentDevice.  # noqa: E501
        :rtype: datetime
        """
        return self._start_timestamp

    @start_timestamp.setter
    def start_timestamp(self, start_timestamp):
        """Sets the start_timestamp of this PaymentDevicesPaymentDevice.

        When the payment device became active if the value is historic, or when the payment device will become active if the value is in the future. Defaults to current time when creating a payment device in `PAYMENT_DEVICE_STATUS_ACTIVE` status. Required for creating a payment device with status `PAYMENT_DEVICE_STATUS_INACTIVE`, optional for other create requests, and output only otherwise.   # noqa: E501

        :param start_timestamp: The start_timestamp of this PaymentDevicesPaymentDevice.  # noqa: E501
        :type: datetime
        """

        self._start_timestamp = start_timestamp

    @property
    def end_timestamp(self):
        """Gets the end_timestamp of this PaymentDevicesPaymentDevice.  # noqa: E501

        When the payment device became inactive if the value is historic, or when the payment device will become inactive if the value is in the future. Required for creating a payment device with status `PAYMENT_DEVICE_STATUS_INACTIVE`, optional for other create requests, and output only otherwise.   # noqa: E501

        :return: The end_timestamp of this PaymentDevicesPaymentDevice.  # noqa: E501
        :rtype: datetime
        """
        return self._end_timestamp

    @end_timestamp.setter
    def end_timestamp(self, end_timestamp):
        """Sets the end_timestamp of this PaymentDevicesPaymentDevice.

        When the payment device became inactive if the value is historic, or when the payment device will become inactive if the value is in the future. Required for creating a payment device with status `PAYMENT_DEVICE_STATUS_INACTIVE`, optional for other create requests, and output only otherwise.   # noqa: E501

        :param end_timestamp: The end_timestamp of this PaymentDevicesPaymentDevice.  # noqa: E501
        :type: datetime
        """

        self._end_timestamp = end_timestamp

    @property
    def tags(self):
        """Gets the tags of this PaymentDevicesPaymentDevice.  # noqa: E501

        Tags assigned to this payment device. Optional for creation; otherwise this is output only.  # noqa: E501

        :return: The tags of this PaymentDevicesPaymentDevice.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this PaymentDevicesPaymentDevice.

        Tags assigned to this payment device. Optional for creation; otherwise this is output only.  # noqa: E501

        :param tags: The tags of this PaymentDevicesPaymentDevice.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

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
        if issubclass(PaymentDevicesPaymentDevice, dict):
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
        if not isinstance(other, PaymentDevicesPaymentDevice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
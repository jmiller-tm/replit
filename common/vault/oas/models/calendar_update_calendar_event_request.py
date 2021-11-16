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

class CalendarUpdateCalendarEventRequest(object):
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
        'request_id': 'str',
        'calendar_event_id': 'str',
        'calendar_event': 'CalendarCalendarEvent',
        'update_mask': 'ProtobufFieldMask'
    }

    attribute_map = {
        'request_id': 'request_id',
        'calendar_event_id': 'calendar_event_id',
        'calendar_event': 'calendar_event',
        'update_mask': 'update_mask'
    }

    def __init__(self, request_id=None, calendar_event_id=None, calendar_event=None, update_mask=None):  # noqa: E501
        """CalendarUpdateCalendarEventRequest - a model defined in Swagger"""  # noqa: E501
        self._request_id = None
        self._calendar_event_id = None
        self._calendar_event = None
        self._update_mask = None
        self.discriminator = None
        self.request_id = request_id
        self.calendar_event_id = calendar_event_id
        self.calendar_event = calendar_event
        self.update_mask = update_mask

    @property
    def request_id(self):
        """Gets the request_id of this CalendarUpdateCalendarEventRequest.  # noqa: E501

        The ID of the request used for idempotency.  Required.  # noqa: E501

        :return: The request_id of this CalendarUpdateCalendarEventRequest.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this CalendarUpdateCalendarEventRequest.

        The ID of the request used for idempotency.  Required.  # noqa: E501

        :param request_id: The request_id of this CalendarUpdateCalendarEventRequest.  # noqa: E501
        :type: str
        """
        if request_id is None:
            raise ValueError("Invalid value for `request_id`, must not be `None`")  # noqa: E501

        self._request_id = request_id

    @property
    def calendar_event_id(self):
        """Gets the calendar_event_id of this CalendarUpdateCalendarEventRequest.  # noqa: E501

        The ID of the calendar event that is to be updated.  Required.  # noqa: E501

        :return: The calendar_event_id of this CalendarUpdateCalendarEventRequest.  # noqa: E501
        :rtype: str
        """
        return self._calendar_event_id

    @calendar_event_id.setter
    def calendar_event_id(self, calendar_event_id):
        """Sets the calendar_event_id of this CalendarUpdateCalendarEventRequest.

        The ID of the calendar event that is to be updated.  Required.  # noqa: E501

        :param calendar_event_id: The calendar_event_id of this CalendarUpdateCalendarEventRequest.  # noqa: E501
        :type: str
        """
        if calendar_event_id is None:
            raise ValueError("Invalid value for `calendar_event_id`, must not be `None`")  # noqa: E501

        self._calendar_event_id = calendar_event_id

    @property
    def calendar_event(self):
        """Gets the calendar_event of this CalendarUpdateCalendarEventRequest.  # noqa: E501


        :return: The calendar_event of this CalendarUpdateCalendarEventRequest.  # noqa: E501
        :rtype: CalendarCalendarEvent
        """
        return self._calendar_event

    @calendar_event.setter
    def calendar_event(self, calendar_event):
        """Sets the calendar_event of this CalendarUpdateCalendarEventRequest.


        :param calendar_event: The calendar_event of this CalendarUpdateCalendarEventRequest.  # noqa: E501
        :type: CalendarCalendarEvent
        """
        if calendar_event is None:
            raise ValueError("Invalid value for `calendar_event`, must not be `None`")  # noqa: E501

        self._calendar_event = calendar_event

    @property
    def update_mask(self):
        """Gets the update_mask of this CalendarUpdateCalendarEventRequest.  # noqa: E501


        :return: The update_mask of this CalendarUpdateCalendarEventRequest.  # noqa: E501
        :rtype: ProtobufFieldMask
        """
        return self._update_mask

    @update_mask.setter
    def update_mask(self, update_mask):
        """Sets the update_mask of this CalendarUpdateCalendarEventRequest.


        :param update_mask: The update_mask of this CalendarUpdateCalendarEventRequest.  # noqa: E501
        :type: ProtobufFieldMask
        """
        if update_mask is None:
            raise ValueError("Invalid value for `update_mask`, must not be `None`")  # noqa: E501

        self._update_mask = update_mask

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
        if issubclass(CalendarUpdateCalendarEventRequest, dict):
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
        if not isinstance(other, CalendarUpdateCalendarEventRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
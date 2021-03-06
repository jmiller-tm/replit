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

class CalendarCalendarEvent(object):
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
        'calendar_id': 'str',
        'name': 'str',
        'is_active': 'bool',
        'start_timestamp': 'datetime',
        'end_timestamp': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'calendar_id': 'calendar_id',
        'name': 'name',
        'is_active': 'is_active',
        'start_timestamp': 'start_timestamp',
        'end_timestamp': 'end_timestamp'
    }

    def __init__(self, id=None, calendar_id=None, name=None, is_active=None, start_timestamp=None, end_timestamp=None):  # noqa: E501
        """CalendarCalendarEvent - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._calendar_id = None
        self._name = None
        self._is_active = None
        self._start_timestamp = None
        self._end_timestamp = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if calendar_id is not None:
            self.calendar_id = calendar_id
        if name is not None:
            self.name = name
        if is_active is not None:
            self.is_active = is_active
        if start_timestamp is not None:
            self.start_timestamp = start_timestamp
        if end_timestamp is not None:
            self.end_timestamp = end_timestamp

    @property
    def id(self):
        """Gets the id of this CalendarCalendarEvent.  # noqa: E501

        The Calendar Event ID can be specified by the user when creating the Calendar Event, otherwise it will be generated by the service. Must be unique.  # noqa: E501

        :return: The id of this CalendarCalendarEvent.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CalendarCalendarEvent.

        The Calendar Event ID can be specified by the user when creating the Calendar Event, otherwise it will be generated by the service. Must be unique.  # noqa: E501

        :param id: The id of this CalendarCalendarEvent.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def calendar_id(self):
        """Gets the calendar_id of this CalendarCalendarEvent.  # noqa: E501

        The Calendar this resource belongs to. Required for create requests.  # noqa: E501

        :return: The calendar_id of this CalendarCalendarEvent.  # noqa: E501
        :rtype: str
        """
        return self._calendar_id

    @calendar_id.setter
    def calendar_id(self, calendar_id):
        """Sets the calendar_id of this CalendarCalendarEvent.

        The Calendar this resource belongs to. Required for create requests.  # noqa: E501

        :param calendar_id: The calendar_id of this CalendarCalendarEvent.  # noqa: E501
        :type: str
        """

        self._calendar_id = calendar_id

    @property
    def name(self):
        """Gets the name of this CalendarCalendarEvent.  # noqa: E501

        The name of the Calendar Event displayed on the UI.  # noqa: E501

        :return: The name of this CalendarCalendarEvent.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CalendarCalendarEvent.

        The name of the Calendar Event displayed on the UI.  # noqa: E501

        :param name: The name of this CalendarCalendarEvent.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def is_active(self):
        """Gets the is_active of this CalendarCalendarEvent.  # noqa: E501

        The current effective state of the Calendar Event.  # noqa: E501

        :return: The is_active of this CalendarCalendarEvent.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this CalendarCalendarEvent.

        The current effective state of the Calendar Event.  # noqa: E501

        :param is_active: The is_active of this CalendarCalendarEvent.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def start_timestamp(self):
        """Gets the start_timestamp of this CalendarCalendarEvent.  # noqa: E501

        The time that the Calendar Event will be effective from (inclusive). Required for create requests.  # noqa: E501

        :return: The start_timestamp of this CalendarCalendarEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._start_timestamp

    @start_timestamp.setter
    def start_timestamp(self, start_timestamp):
        """Sets the start_timestamp of this CalendarCalendarEvent.

        The time that the Calendar Event will be effective from (inclusive). Required for create requests.  # noqa: E501

        :param start_timestamp: The start_timestamp of this CalendarCalendarEvent.  # noqa: E501
        :type: datetime
        """

        self._start_timestamp = start_timestamp

    @property
    def end_timestamp(self):
        """Gets the end_timestamp of this CalendarCalendarEvent.  # noqa: E501

        The time that the Calendar Event will be effective to (exclusive). Required for create requests.  # noqa: E501

        :return: The end_timestamp of this CalendarCalendarEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._end_timestamp

    @end_timestamp.setter
    def end_timestamp(self, end_timestamp):
        """Sets the end_timestamp of this CalendarCalendarEvent.

        The time that the Calendar Event will be effective to (exclusive). Required for create requests.  # noqa: E501

        :param end_timestamp: The end_timestamp of this CalendarCalendarEvent.  # noqa: E501
        :type: datetime
        """

        self._end_timestamp = end_timestamp

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
        if issubclass(CalendarCalendarEvent, dict):
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
        if not isinstance(other, CalendarCalendarEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

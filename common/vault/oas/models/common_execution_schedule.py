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

class CommonExecutionSchedule(object):
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
        'start_date': 'str',
        'end_date': 'str',
        'day': 'str',
        'day_of_week': 'str',
        'hour': 'str',
        'minute': 'str',
        'second': 'str',
        'month': 'str',
        'year': 'str',
        'week': 'str'
    }

    attribute_map = {
        'start_date': 'start_date',
        'end_date': 'end_date',
        'day': 'day',
        'day_of_week': 'day_of_week',
        'hour': 'hour',
        'minute': 'minute',
        'second': 'second',
        'month': 'month',
        'year': 'year',
        'week': 'week'
    }

    def __init__(self, start_date=None, end_date=None, day=None, day_of_week=None, hour=None, minute=None, second=None, month=None, year=None, week=None):  # noqa: E501
        """CommonExecutionSchedule - a model defined in Swagger"""  # noqa: E501
        self._start_date = None
        self._end_date = None
        self._day = None
        self._day_of_week = None
        self._hour = None
        self._minute = None
        self._second = None
        self._month = None
        self._year = None
        self._week = None
        self.discriminator = None
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if day is not None:
            self.day = day
        if day_of_week is not None:
            self.day_of_week = day_of_week
        if hour is not None:
            self.hour = hour
        if minute is not None:
            self.minute = minute
        if second is not None:
            self.second = second
        if month is not None:
            self.month = month
        if year is not None:
            self.year = year
        if week is not None:
            self.week = week

    @property
    def start_date(self):
        """Gets the start_date of this CommonExecutionSchedule.  # noqa: E501


        :return: The start_date of this CommonExecutionSchedule.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this CommonExecutionSchedule.


        :param start_date: The start_date of this CommonExecutionSchedule.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this CommonExecutionSchedule.  # noqa: E501


        :return: The end_date of this CommonExecutionSchedule.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this CommonExecutionSchedule.


        :param end_date: The end_date of this CommonExecutionSchedule.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def day(self):
        """Gets the day of this CommonExecutionSchedule.  # noqa: E501


        :return: The day of this CommonExecutionSchedule.  # noqa: E501
        :rtype: str
        """
        return self._day

    @day.setter
    def day(self, day):
        """Sets the day of this CommonExecutionSchedule.


        :param day: The day of this CommonExecutionSchedule.  # noqa: E501
        :type: str
        """

        self._day = day

    @property
    def day_of_week(self):
        """Gets the day_of_week of this CommonExecutionSchedule.  # noqa: E501


        :return: The day_of_week of this CommonExecutionSchedule.  # noqa: E501
        :rtype: str
        """
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, day_of_week):
        """Sets the day_of_week of this CommonExecutionSchedule.


        :param day_of_week: The day_of_week of this CommonExecutionSchedule.  # noqa: E501
        :type: str
        """

        self._day_of_week = day_of_week

    @property
    def hour(self):
        """Gets the hour of this CommonExecutionSchedule.  # noqa: E501


        :return: The hour of this CommonExecutionSchedule.  # noqa: E501
        :rtype: str
        """
        return self._hour

    @hour.setter
    def hour(self, hour):
        """Sets the hour of this CommonExecutionSchedule.


        :param hour: The hour of this CommonExecutionSchedule.  # noqa: E501
        :type: str
        """

        self._hour = hour

    @property
    def minute(self):
        """Gets the minute of this CommonExecutionSchedule.  # noqa: E501


        :return: The minute of this CommonExecutionSchedule.  # noqa: E501
        :rtype: str
        """
        return self._minute

    @minute.setter
    def minute(self, minute):
        """Sets the minute of this CommonExecutionSchedule.


        :param minute: The minute of this CommonExecutionSchedule.  # noqa: E501
        :type: str
        """

        self._minute = minute

    @property
    def second(self):
        """Gets the second of this CommonExecutionSchedule.  # noqa: E501


        :return: The second of this CommonExecutionSchedule.  # noqa: E501
        :rtype: str
        """
        return self._second

    @second.setter
    def second(self, second):
        """Sets the second of this CommonExecutionSchedule.


        :param second: The second of this CommonExecutionSchedule.  # noqa: E501
        :type: str
        """

        self._second = second

    @property
    def month(self):
        """Gets the month of this CommonExecutionSchedule.  # noqa: E501


        :return: The month of this CommonExecutionSchedule.  # noqa: E501
        :rtype: str
        """
        return self._month

    @month.setter
    def month(self, month):
        """Sets the month of this CommonExecutionSchedule.


        :param month: The month of this CommonExecutionSchedule.  # noqa: E501
        :type: str
        """

        self._month = month

    @property
    def year(self):
        """Gets the year of this CommonExecutionSchedule.  # noqa: E501


        :return: The year of this CommonExecutionSchedule.  # noqa: E501
        :rtype: str
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this CommonExecutionSchedule.


        :param year: The year of this CommonExecutionSchedule.  # noqa: E501
        :type: str
        """

        self._year = year

    @property
    def week(self):
        """Gets the week of this CommonExecutionSchedule.  # noqa: E501


        :return: The week of this CommonExecutionSchedule.  # noqa: E501
        :rtype: str
        """
        return self._week

    @week.setter
    def week(self, week):
        """Sets the week of this CommonExecutionSchedule.


        :param week: The week of this CommonExecutionSchedule.  # noqa: E501
        :type: str
        """

        self._week = week

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
        if issubclass(CommonExecutionSchedule, dict):
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
        if not isinstance(other, CommonExecutionSchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
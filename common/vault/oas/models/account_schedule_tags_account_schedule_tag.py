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

class AccountScheduleTagsAccountScheduleTag(object):
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
        'description': 'str',
        'sends_scheduled_operation_reports': 'bool',
        'schedule_status_override': 'AccountScheduleTagsAccountScheduleTagScheduleStatusOverride',
        'schedule_status_override_start_timestamp': 'datetime',
        'schedule_status_override_end_timestamp': 'datetime',
        'test_pause_at_timestamp': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'description': 'description',
        'sends_scheduled_operation_reports': 'sends_scheduled_operation_reports',
        'schedule_status_override': 'schedule_status_override',
        'schedule_status_override_start_timestamp': 'schedule_status_override_start_timestamp',
        'schedule_status_override_end_timestamp': 'schedule_status_override_end_timestamp',
        'test_pause_at_timestamp': 'test_pause_at_timestamp'
    }

    def __init__(self, id=None, description=None, sends_scheduled_operation_reports=None, schedule_status_override=None, schedule_status_override_start_timestamp=None, schedule_status_override_end_timestamp=None, test_pause_at_timestamp=None):  # noqa: E501
        """AccountScheduleTagsAccountScheduleTag - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._description = None
        self._sends_scheduled_operation_reports = None
        self._schedule_status_override = None
        self._schedule_status_override_start_timestamp = None
        self._schedule_status_override_end_timestamp = None
        self._test_pause_at_timestamp = None
        self.discriminator = None
        self.id = id
        if description is not None:
            self.description = description
        if sends_scheduled_operation_reports is not None:
            self.sends_scheduled_operation_reports = sends_scheduled_operation_reports
        if schedule_status_override is not None:
            self.schedule_status_override = schedule_status_override
        if schedule_status_override_start_timestamp is not None:
            self.schedule_status_override_start_timestamp = schedule_status_override_start_timestamp
        if schedule_status_override_end_timestamp is not None:
            self.schedule_status_override_end_timestamp = schedule_status_override_end_timestamp
        if test_pause_at_timestamp is not None:
            self.test_pause_at_timestamp = test_pause_at_timestamp

    @property
    def id(self):
        """Gets the id of this AccountScheduleTagsAccountScheduleTag.  # noqa: E501

        The ID of the AccountScheduleTag; it is used to tag schedules in a Smart Contract or Supervisor Contract.  Required. Max length: 256 characters.  # noqa: E501

        :return: The id of this AccountScheduleTagsAccountScheduleTag.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AccountScheduleTagsAccountScheduleTag.

        The ID of the AccountScheduleTag; it is used to tag schedules in a Smart Contract or Supervisor Contract.  Required. Max length: 256 characters.  # noqa: E501

        :param id: The id of this AccountScheduleTagsAccountScheduleTag.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def description(self):
        """Gets the description of this AccountScheduleTagsAccountScheduleTag.  # noqa: E501

        The description of the AccountScheduleTag.   # noqa: E501

        :return: The description of this AccountScheduleTagsAccountScheduleTag.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AccountScheduleTagsAccountScheduleTag.

        The description of the AccountScheduleTag.   # noqa: E501

        :param description: The description of this AccountScheduleTagsAccountScheduleTag.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def sends_scheduled_operation_reports(self):
        """Gets the sends_scheduled_operation_reports of this AccountScheduleTagsAccountScheduleTag.  # noqa: E501

        Indicates if the AccountScheduleTag is set to produce execution notifications.  # noqa: E501

        :return: The sends_scheduled_operation_reports of this AccountScheduleTagsAccountScheduleTag.  # noqa: E501
        :rtype: bool
        """
        return self._sends_scheduled_operation_reports

    @sends_scheduled_operation_reports.setter
    def sends_scheduled_operation_reports(self, sends_scheduled_operation_reports):
        """Sets the sends_scheduled_operation_reports of this AccountScheduleTagsAccountScheduleTag.

        Indicates if the AccountScheduleTag is set to produce execution notifications.  # noqa: E501

        :param sends_scheduled_operation_reports: The sends_scheduled_operation_reports of this AccountScheduleTagsAccountScheduleTag.  # noqa: E501
        :type: bool
        """

        self._sends_scheduled_operation_reports = sends_scheduled_operation_reports

    @property
    def schedule_status_override(self):
        """Gets the schedule_status_override of this AccountScheduleTagsAccountScheduleTag.  # noqa: E501


        :return: The schedule_status_override of this AccountScheduleTagsAccountScheduleTag.  # noqa: E501
        :rtype: AccountScheduleTagsAccountScheduleTagScheduleStatusOverride
        """
        return self._schedule_status_override

    @schedule_status_override.setter
    def schedule_status_override(self, schedule_status_override):
        """Sets the schedule_status_override of this AccountScheduleTagsAccountScheduleTag.


        :param schedule_status_override: The schedule_status_override of this AccountScheduleTagsAccountScheduleTag.  # noqa: E501
        :type: AccountScheduleTagsAccountScheduleTagScheduleStatusOverride
        """

        self._schedule_status_override = schedule_status_override

    @property
    def schedule_status_override_start_timestamp(self):
        """Gets the schedule_status_override_start_timestamp of this AccountScheduleTagsAccountScheduleTag.  # noqa: E501

        A timestamp indicating when to start overriding the status on account/plan schedules with this tag.  # noqa: E501

        :return: The schedule_status_override_start_timestamp of this AccountScheduleTagsAccountScheduleTag.  # noqa: E501
        :rtype: datetime
        """
        return self._schedule_status_override_start_timestamp

    @schedule_status_override_start_timestamp.setter
    def schedule_status_override_start_timestamp(self, schedule_status_override_start_timestamp):
        """Sets the schedule_status_override_start_timestamp of this AccountScheduleTagsAccountScheduleTag.

        A timestamp indicating when to start overriding the status on account/plan schedules with this tag.  # noqa: E501

        :param schedule_status_override_start_timestamp: The schedule_status_override_start_timestamp of this AccountScheduleTagsAccountScheduleTag.  # noqa: E501
        :type: datetime
        """

        self._schedule_status_override_start_timestamp = schedule_status_override_start_timestamp

    @property
    def schedule_status_override_end_timestamp(self):
        """Gets the schedule_status_override_end_timestamp of this AccountScheduleTagsAccountScheduleTag.  # noqa: E501

        A timestamp indicating when to stop overriding the status on account/plan schedules with this tag.  # noqa: E501

        :return: The schedule_status_override_end_timestamp of this AccountScheduleTagsAccountScheduleTag.  # noqa: E501
        :rtype: datetime
        """
        return self._schedule_status_override_end_timestamp

    @schedule_status_override_end_timestamp.setter
    def schedule_status_override_end_timestamp(self, schedule_status_override_end_timestamp):
        """Sets the schedule_status_override_end_timestamp of this AccountScheduleTagsAccountScheduleTag.

        A timestamp indicating when to stop overriding the status on account/plan schedules with this tag.  # noqa: E501

        :param schedule_status_override_end_timestamp: The schedule_status_override_end_timestamp of this AccountScheduleTagsAccountScheduleTag.  # noqa: E501
        :type: datetime
        """

        self._schedule_status_override_end_timestamp = schedule_status_override_end_timestamp

    @property
    def test_pause_at_timestamp(self):
        """Gets the test_pause_at_timestamp of this AccountScheduleTagsAccountScheduleTag.  # noqa: E501

        A timestamp indicating when an account/plan schedule with this tag will pause; the pause will occur when `next_run_timestamp` is equal to or greater than `test_pause_at_timestamp`. Only for testing purposes.  # noqa: E501

        :return: The test_pause_at_timestamp of this AccountScheduleTagsAccountScheduleTag.  # noqa: E501
        :rtype: datetime
        """
        return self._test_pause_at_timestamp

    @test_pause_at_timestamp.setter
    def test_pause_at_timestamp(self, test_pause_at_timestamp):
        """Sets the test_pause_at_timestamp of this AccountScheduleTagsAccountScheduleTag.

        A timestamp indicating when an account/plan schedule with this tag will pause; the pause will occur when `next_run_timestamp` is equal to or greater than `test_pause_at_timestamp`. Only for testing purposes.  # noqa: E501

        :param test_pause_at_timestamp: The test_pause_at_timestamp of this AccountScheduleTagsAccountScheduleTag.  # noqa: E501
        :type: datetime
        """

        self._test_pause_at_timestamp = test_pause_at_timestamp

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
        if issubclass(AccountScheduleTagsAccountScheduleTag, dict):
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
        if not isinstance(other, AccountScheduleTagsAccountScheduleTag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

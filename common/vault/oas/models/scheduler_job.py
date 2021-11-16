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

class SchedulerJob(object):
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
        'status': 'SchedulerJobStatus',
        'schedule_id': 'str',
        'schedule_timestamp': 'datetime',
        'publish_timestamp': 'datetime',
        'completed_timestamp': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'schedule_id': 'schedule_id',
        'schedule_timestamp': 'schedule_timestamp',
        'publish_timestamp': 'publish_timestamp',
        'completed_timestamp': 'completed_timestamp'
    }

    def __init__(self, id=None, status=None, schedule_id=None, schedule_timestamp=None, publish_timestamp=None, completed_timestamp=None):  # noqa: E501
        """SchedulerJob - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._status = None
        self._schedule_id = None
        self._schedule_timestamp = None
        self._publish_timestamp = None
        self._completed_timestamp = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if schedule_id is not None:
            self.schedule_id = schedule_id
        if schedule_timestamp is not None:
            self.schedule_timestamp = schedule_timestamp
        if publish_timestamp is not None:
            self.publish_timestamp = publish_timestamp
        if completed_timestamp is not None:
            self.completed_timestamp = completed_timestamp

    @property
    def id(self):
        """Gets the id of this SchedulerJob.  # noqa: E501

        A Unique identifier for a Job.  # noqa: E501

        :return: The id of this SchedulerJob.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SchedulerJob.

        A Unique identifier for a Job.  # noqa: E501

        :param id: The id of this SchedulerJob.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def status(self):
        """Gets the status of this SchedulerJob.  # noqa: E501


        :return: The status of this SchedulerJob.  # noqa: E501
        :rtype: SchedulerJobStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SchedulerJob.


        :param status: The status of this SchedulerJob.  # noqa: E501
        :type: SchedulerJobStatus
        """

        self._status = status

    @property
    def schedule_id(self):
        """Gets the schedule_id of this SchedulerJob.  # noqa: E501

        The Schedule ID references the Schedule that the Job belongs to.  # noqa: E501

        :return: The schedule_id of this SchedulerJob.  # noqa: E501
        :rtype: str
        """
        return self._schedule_id

    @schedule_id.setter
    def schedule_id(self, schedule_id):
        """Sets the schedule_id of this SchedulerJob.

        The Schedule ID references the Schedule that the Job belongs to.  # noqa: E501

        :param schedule_id: The schedule_id of this SchedulerJob.  # noqa: E501
        :type: str
        """

        self._schedule_id = schedule_id

    @property
    def schedule_timestamp(self):
        """Gets the schedule_timestamp of this SchedulerJob.  # noqa: E501

        The time the job was scheduled to be triggered.  # noqa: E501

        :return: The schedule_timestamp of this SchedulerJob.  # noqa: E501
        :rtype: datetime
        """
        return self._schedule_timestamp

    @schedule_timestamp.setter
    def schedule_timestamp(self, schedule_timestamp):
        """Sets the schedule_timestamp of this SchedulerJob.

        The time the job was scheduled to be triggered.  # noqa: E501

        :param schedule_timestamp: The schedule_timestamp of this SchedulerJob.  # noqa: E501
        :type: datetime
        """

        self._schedule_timestamp = schedule_timestamp

    @property
    def publish_timestamp(self):
        """Gets the publish_timestamp of this SchedulerJob.  # noqa: E501

        The time the job was actually published by the Scheduler.  # noqa: E501

        :return: The publish_timestamp of this SchedulerJob.  # noqa: E501
        :rtype: datetime
        """
        return self._publish_timestamp

    @publish_timestamp.setter
    def publish_timestamp(self, publish_timestamp):
        """Sets the publish_timestamp of this SchedulerJob.

        The time the job was actually published by the Scheduler.  # noqa: E501

        :param publish_timestamp: The publish_timestamp of this SchedulerJob.  # noqa: E501
        :type: datetime
        """

        self._publish_timestamp = publish_timestamp

    @property
    def completed_timestamp(self):
        """Gets the completed_timestamp of this SchedulerJob.  # noqa: E501

        Indicates the time that a successful job outcome was received. This timestamp is UTC.  # noqa: E501

        :return: The completed_timestamp of this SchedulerJob.  # noqa: E501
        :rtype: datetime
        """
        return self._completed_timestamp

    @completed_timestamp.setter
    def completed_timestamp(self, completed_timestamp):
        """Sets the completed_timestamp of this SchedulerJob.

        Indicates the time that a successful job outcome was received. This timestamp is UTC.  # noqa: E501

        :param completed_timestamp: The completed_timestamp of this SchedulerJob.  # noqa: E501
        :type: datetime
        """

        self._completed_timestamp = completed_timestamp

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
        if issubclass(SchedulerJob, dict):
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
        if not isinstance(other, SchedulerJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

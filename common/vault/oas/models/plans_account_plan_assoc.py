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

class PlansAccountPlanAssoc(object):
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
        'account_id': 'str',
        'plan_id': 'str',
        'create_timestamp': 'datetime',
        'start_timestamp': 'datetime',
        'end_timestamp': 'datetime',
        'status': 'PlansAccountPlanAssocStatus'
    }

    attribute_map = {
        'id': 'id',
        'account_id': 'account_id',
        'plan_id': 'plan_id',
        'create_timestamp': 'create_timestamp',
        'start_timestamp': 'start_timestamp',
        'end_timestamp': 'end_timestamp',
        'status': 'status'
    }

    def __init__(self, id=None, account_id=None, plan_id=None, create_timestamp=None, start_timestamp=None, end_timestamp=None, status=None):  # noqa: E501
        """PlansAccountPlanAssoc - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._account_id = None
        self._plan_id = None
        self._create_timestamp = None
        self._start_timestamp = None
        self._end_timestamp = None
        self._status = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if account_id is not None:
            self.account_id = account_id
        if plan_id is not None:
            self.plan_id = plan_id
        if create_timestamp is not None:
            self.create_timestamp = create_timestamp
        if start_timestamp is not None:
            self.start_timestamp = start_timestamp
        if end_timestamp is not None:
            self.end_timestamp = end_timestamp
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this PlansAccountPlanAssoc.  # noqa: E501

        A unique ID for an account plan association.  Max length: 36 characters.  # noqa: E501

        :return: The id of this PlansAccountPlanAssoc.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PlansAccountPlanAssoc.

        A unique ID for an account plan association.  Max length: 36 characters.  # noqa: E501

        :param id: The id of this PlansAccountPlanAssoc.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def account_id(self):
        """Gets the account_id of this PlansAccountPlanAssoc.  # noqa: E501

        The account ID associated with the plan.  # noqa: E501

        :return: The account_id of this PlansAccountPlanAssoc.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this PlansAccountPlanAssoc.

        The account ID associated with the plan.  # noqa: E501

        :param account_id: The account_id of this PlansAccountPlanAssoc.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def plan_id(self):
        """Gets the plan_id of this PlansAccountPlanAssoc.  # noqa: E501

        The plan ID associated with the account.  # noqa: E501

        :return: The plan_id of this PlansAccountPlanAssoc.  # noqa: E501
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """Sets the plan_id of this PlansAccountPlanAssoc.

        The plan ID associated with the account.  # noqa: E501

        :param plan_id: The plan_id of this PlansAccountPlanAssoc.  # noqa: E501
        :type: str
        """

        self._plan_id = plan_id

    @property
    def create_timestamp(self):
        """Gets the create_timestamp of this PlansAccountPlanAssoc.  # noqa: E501

        The timestamp indicating when this account plan association was created.  # noqa: E501

        :return: The create_timestamp of this PlansAccountPlanAssoc.  # noqa: E501
        :rtype: datetime
        """
        return self._create_timestamp

    @create_timestamp.setter
    def create_timestamp(self, create_timestamp):
        """Sets the create_timestamp of this PlansAccountPlanAssoc.

        The timestamp indicating when this account plan association was created.  # noqa: E501

        :param create_timestamp: The create_timestamp of this PlansAccountPlanAssoc.  # noqa: E501
        :type: datetime
        """

        self._create_timestamp = create_timestamp

    @property
    def start_timestamp(self):
        """Gets the start_timestamp of this PlansAccountPlanAssoc.  # noqa: E501

        The timestamp indicating when this account plan association became active.  # noqa: E501

        :return: The start_timestamp of this PlansAccountPlanAssoc.  # noqa: E501
        :rtype: datetime
        """
        return self._start_timestamp

    @start_timestamp.setter
    def start_timestamp(self, start_timestamp):
        """Sets the start_timestamp of this PlansAccountPlanAssoc.

        The timestamp indicating when this account plan association became active.  # noqa: E501

        :param start_timestamp: The start_timestamp of this PlansAccountPlanAssoc.  # noqa: E501
        :type: datetime
        """

        self._start_timestamp = start_timestamp

    @property
    def end_timestamp(self):
        """Gets the end_timestamp of this PlansAccountPlanAssoc.  # noqa: E501

        The timestamp indicating when this account plan association became inactive.  # noqa: E501

        :return: The end_timestamp of this PlansAccountPlanAssoc.  # noqa: E501
        :rtype: datetime
        """
        return self._end_timestamp

    @end_timestamp.setter
    def end_timestamp(self, end_timestamp):
        """Sets the end_timestamp of this PlansAccountPlanAssoc.

        The timestamp indicating when this account plan association became inactive.  # noqa: E501

        :param end_timestamp: The end_timestamp of this PlansAccountPlanAssoc.  # noqa: E501
        :type: datetime
        """

        self._end_timestamp = end_timestamp

    @property
    def status(self):
        """Gets the status of this PlansAccountPlanAssoc.  # noqa: E501


        :return: The status of this PlansAccountPlanAssoc.  # noqa: E501
        :rtype: PlansAccountPlanAssocStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PlansAccountPlanAssoc.


        :param status: The status of this PlansAccountPlanAssoc.  # noqa: E501
        :type: PlansAccountPlanAssocStatus
        """

        self._status = status

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
        if issubclass(PlansAccountPlanAssoc, dict):
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
        if not isinstance(other, PlansAccountPlanAssoc):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

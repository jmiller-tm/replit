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

class SmartContractsExternalEvent(object):
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
        'timestamp': 'datetime',
        'update_param': 'SmartContractsUpdateParamEvent',
        'posting_instruction_batch': 'V1PostingInstructionBatch',
        'set_flag': 'SmartContractsSetFlagEvent',
        'get_derived_parameters': 'SmartContractsGetDerivedParametersEvent'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'update_param': 'update_param',
        'posting_instruction_batch': 'posting_instruction_batch',
        'set_flag': 'set_flag',
        'get_derived_parameters': 'get_derived_parameters'
    }

    def __init__(self, timestamp=None, update_param=None, posting_instruction_batch=None, set_flag=None, get_derived_parameters=None):  # noqa: E501
        """SmartContractsExternalEvent - a model defined in Swagger"""  # noqa: E501
        self._timestamp = None
        self._update_param = None
        self._posting_instruction_batch = None
        self._set_flag = None
        self._get_derived_parameters = None
        self.discriminator = None
        if timestamp is not None:
            self.timestamp = timestamp
        if update_param is not None:
            self.update_param = update_param
        if posting_instruction_batch is not None:
            self.posting_instruction_batch = posting_instruction_batch
        if set_flag is not None:
            self.set_flag = set_flag
        if get_derived_parameters is not None:
            self.get_derived_parameters = get_derived_parameters

    @property
    def timestamp(self):
        """Gets the timestamp of this SmartContractsExternalEvent.  # noqa: E501

        The simulation time the event should occur at.  # noqa: E501

        :return: The timestamp of this SmartContractsExternalEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this SmartContractsExternalEvent.

        The simulation time the event should occur at.  # noqa: E501

        :param timestamp: The timestamp of this SmartContractsExternalEvent.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def update_param(self):
        """Gets the update_param of this SmartContractsExternalEvent.  # noqa: E501


        :return: The update_param of this SmartContractsExternalEvent.  # noqa: E501
        :rtype: SmartContractsUpdateParamEvent
        """
        return self._update_param

    @update_param.setter
    def update_param(self, update_param):
        """Sets the update_param of this SmartContractsExternalEvent.


        :param update_param: The update_param of this SmartContractsExternalEvent.  # noqa: E501
        :type: SmartContractsUpdateParamEvent
        """

        self._update_param = update_param

    @property
    def posting_instruction_batch(self):
        """Gets the posting_instruction_batch of this SmartContractsExternalEvent.  # noqa: E501


        :return: The posting_instruction_batch of this SmartContractsExternalEvent.  # noqa: E501
        :rtype: V1PostingInstructionBatch
        """
        return self._posting_instruction_batch

    @posting_instruction_batch.setter
    def posting_instruction_batch(self, posting_instruction_batch):
        """Sets the posting_instruction_batch of this SmartContractsExternalEvent.


        :param posting_instruction_batch: The posting_instruction_batch of this SmartContractsExternalEvent.  # noqa: E501
        :type: V1PostingInstructionBatch
        """

        self._posting_instruction_batch = posting_instruction_batch

    @property
    def set_flag(self):
        """Gets the set_flag of this SmartContractsExternalEvent.  # noqa: E501


        :return: The set_flag of this SmartContractsExternalEvent.  # noqa: E501
        :rtype: SmartContractsSetFlagEvent
        """
        return self._set_flag

    @set_flag.setter
    def set_flag(self, set_flag):
        """Sets the set_flag of this SmartContractsExternalEvent.


        :param set_flag: The set_flag of this SmartContractsExternalEvent.  # noqa: E501
        :type: SmartContractsSetFlagEvent
        """

        self._set_flag = set_flag

    @property
    def get_derived_parameters(self):
        """Gets the get_derived_parameters of this SmartContractsExternalEvent.  # noqa: E501


        :return: The get_derived_parameters of this SmartContractsExternalEvent.  # noqa: E501
        :rtype: SmartContractsGetDerivedParametersEvent
        """
        return self._get_derived_parameters

    @get_derived_parameters.setter
    def get_derived_parameters(self, get_derived_parameters):
        """Sets the get_derived_parameters of this SmartContractsExternalEvent.


        :param get_derived_parameters: The get_derived_parameters of this SmartContractsExternalEvent.  # noqa: E501
        :type: SmartContractsGetDerivedParametersEvent
        """

        self._get_derived_parameters = get_derived_parameters

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
        if issubclass(SmartContractsExternalEvent, dict):
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
        if not isinstance(other, SmartContractsExternalEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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

class GlobalParametersGlobalParameterValue(object):
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
        'global_parameter_id': 'str',
        'value': 'str',
        'effective_timestamp': 'datetime',
        'create_timestamp': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'global_parameter_id': 'global_parameter_id',
        'value': 'value',
        'effective_timestamp': 'effective_timestamp',
        'create_timestamp': 'create_timestamp'
    }

    def __init__(self, id=None, global_parameter_id=None, value=None, effective_timestamp=None, create_timestamp=None):  # noqa: E501
        """GlobalParametersGlobalParameterValue - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._global_parameter_id = None
        self._value = None
        self._effective_timestamp = None
        self._create_timestamp = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.global_parameter_id = global_parameter_id
        self.value = value
        self.effective_timestamp = effective_timestamp
        if create_timestamp is not None:
            self.create_timestamp = create_timestamp

    @property
    def id(self):
        """Gets the id of this GlobalParametersGlobalParameterValue.  # noqa: E501

        The `GlobalParameterValue` ID.  # noqa: E501

        :return: The id of this GlobalParametersGlobalParameterValue.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GlobalParametersGlobalParameterValue.

        The `GlobalParameterValue` ID.  # noqa: E501

        :param id: The id of this GlobalParametersGlobalParameterValue.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def global_parameter_id(self):
        """Gets the global_parameter_id of this GlobalParametersGlobalParameterValue.  # noqa: E501

        The `GlobalParameter` ID this value belongs to.  Required.  # noqa: E501

        :return: The global_parameter_id of this GlobalParametersGlobalParameterValue.  # noqa: E501
        :rtype: str
        """
        return self._global_parameter_id

    @global_parameter_id.setter
    def global_parameter_id(self, global_parameter_id):
        """Sets the global_parameter_id of this GlobalParametersGlobalParameterValue.

        The `GlobalParameter` ID this value belongs to.  Required.  # noqa: E501

        :param global_parameter_id: The global_parameter_id of this GlobalParametersGlobalParameterValue.  # noqa: E501
        :type: str
        """
        if global_parameter_id is None:
            raise ValueError("Invalid value for `global_parameter_id`, must not be `None`")  # noqa: E501

        self._global_parameter_id = global_parameter_id

    @property
    def value(self):
        """Gets the value of this GlobalParametersGlobalParameterValue.  # noqa: E501

        The actual value. This is stored as a string and should be processed together with the information stored in the associated `GlobalParameter`. This will determine how the value should be parsed or displayed.  Required.  # noqa: E501

        :return: The value of this GlobalParametersGlobalParameterValue.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this GlobalParametersGlobalParameterValue.

        The actual value. This is stored as a string and should be processed together with the information stored in the associated `GlobalParameter`. This will determine how the value should be parsed or displayed.  Required.  # noqa: E501

        :param value: The value of this GlobalParametersGlobalParameterValue.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def effective_timestamp(self):
        """Gets the effective_timestamp of this GlobalParametersGlobalParameterValue.  # noqa: E501

        A timestamp indicating when the `GlobalParameterValue` is effective from.  Required.  # noqa: E501

        :return: The effective_timestamp of this GlobalParametersGlobalParameterValue.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_timestamp

    @effective_timestamp.setter
    def effective_timestamp(self, effective_timestamp):
        """Sets the effective_timestamp of this GlobalParametersGlobalParameterValue.

        A timestamp indicating when the `GlobalParameterValue` is effective from.  Required.  # noqa: E501

        :param effective_timestamp: The effective_timestamp of this GlobalParametersGlobalParameterValue.  # noqa: E501
        :type: datetime
        """
        if effective_timestamp is None:
            raise ValueError("Invalid value for `effective_timestamp`, must not be `None`")  # noqa: E501

        self._effective_timestamp = effective_timestamp

    @property
    def create_timestamp(self):
        """Gets the create_timestamp of this GlobalParametersGlobalParameterValue.  # noqa: E501

        A timestamp indicating when the `GlobalParameterValue` was created.  # noqa: E501

        :return: The create_timestamp of this GlobalParametersGlobalParameterValue.  # noqa: E501
        :rtype: datetime
        """
        return self._create_timestamp

    @create_timestamp.setter
    def create_timestamp(self, create_timestamp):
        """Sets the create_timestamp of this GlobalParametersGlobalParameterValue.

        A timestamp indicating when the `GlobalParameterValue` was created.  # noqa: E501

        :param create_timestamp: The create_timestamp of this GlobalParametersGlobalParameterValue.  # noqa: E501
        :type: datetime
        """

        self._create_timestamp = create_timestamp

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
        if issubclass(GlobalParametersGlobalParameterValue, dict):
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
        if not isinstance(other, GlobalParametersGlobalParameterValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

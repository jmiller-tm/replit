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

class FlagsFlagDefinition(object):
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
        'name': 'str',
        'description': 'str',
        'required_flag_level': 'FlagsFlagLevel',
        'create_timestamp': 'datetime',
        'flag_visibility': 'FlagsFlagVisibility',
        'is_active': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'required_flag_level': 'required_flag_level',
        'create_timestamp': 'create_timestamp',
        'flag_visibility': 'flag_visibility',
        'is_active': 'is_active'
    }

    def __init__(self, id=None, name=None, description=None, required_flag_level=None, create_timestamp=None, flag_visibility=None, is_active=None):  # noqa: E501
        """FlagsFlagDefinition - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._description = None
        self._required_flag_level = None
        self._create_timestamp = None
        self._flag_visibility = None
        self._is_active = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if required_flag_level is not None:
            self.required_flag_level = required_flag_level
        if create_timestamp is not None:
            self.create_timestamp = create_timestamp
        if flag_visibility is not None:
            self.flag_visibility = flag_visibility
        if is_active is not None:
            self.is_active = is_active

    @property
    def id(self):
        """Gets the id of this FlagsFlagDefinition.  # noqa: E501

        The ID of the flag definition. Must equal the flag definition name when creating a flag definition. Required for create requests.  # noqa: E501

        :return: The id of this FlagsFlagDefinition.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FlagsFlagDefinition.

        The ID of the flag definition. Must equal the flag definition name when creating a flag definition. Required for create requests.  # noqa: E501

        :param id: The id of this FlagsFlagDefinition.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this FlagsFlagDefinition.  # noqa: E501

        The name of the flag definition. Must be unique. Required for create requests.  # noqa: E501

        :return: The name of this FlagsFlagDefinition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FlagsFlagDefinition.

        The name of the flag definition. Must be unique. Required for create requests.  # noqa: E501

        :param name: The name of this FlagsFlagDefinition.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this FlagsFlagDefinition.  # noqa: E501

        The description of the flag definition. Optional for create requests.   # noqa: E501

        :return: The description of this FlagsFlagDefinition.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FlagsFlagDefinition.

        The description of the flag definition. Optional for create requests.   # noqa: E501

        :param description: The description of this FlagsFlagDefinition.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def required_flag_level(self):
        """Gets the required_flag_level of this FlagsFlagDefinition.  # noqa: E501


        :return: The required_flag_level of this FlagsFlagDefinition.  # noqa: E501
        :rtype: FlagsFlagLevel
        """
        return self._required_flag_level

    @required_flag_level.setter
    def required_flag_level(self, required_flag_level):
        """Sets the required_flag_level of this FlagsFlagDefinition.


        :param required_flag_level: The required_flag_level of this FlagsFlagDefinition.  # noqa: E501
        :type: FlagsFlagLevel
        """

        self._required_flag_level = required_flag_level

    @property
    def create_timestamp(self):
        """Gets the create_timestamp of this FlagsFlagDefinition.  # noqa: E501

        The time the flag definition was created. Output only.  # noqa: E501

        :return: The create_timestamp of this FlagsFlagDefinition.  # noqa: E501
        :rtype: datetime
        """
        return self._create_timestamp

    @create_timestamp.setter
    def create_timestamp(self, create_timestamp):
        """Sets the create_timestamp of this FlagsFlagDefinition.

        The time the flag definition was created. Output only.  # noqa: E501

        :param create_timestamp: The create_timestamp of this FlagsFlagDefinition.  # noqa: E501
        :type: datetime
        """

        self._create_timestamp = create_timestamp

    @property
    def flag_visibility(self):
        """Gets the flag_visibility of this FlagsFlagDefinition.  # noqa: E501


        :return: The flag_visibility of this FlagsFlagDefinition.  # noqa: E501
        :rtype: FlagsFlagVisibility
        """
        return self._flag_visibility

    @flag_visibility.setter
    def flag_visibility(self, flag_visibility):
        """Sets the flag_visibility of this FlagsFlagDefinition.


        :param flag_visibility: The flag_visibility of this FlagsFlagDefinition.  # noqa: E501
        :type: FlagsFlagVisibility
        """

        self._flag_visibility = flag_visibility

    @property
    def is_active(self):
        """Gets the is_active of this FlagsFlagDefinition.  # noqa: E501

        Indicates if the flag definition is active. Update only.  # noqa: E501

        :return: The is_active of this FlagsFlagDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this FlagsFlagDefinition.

        Indicates if the flag definition is active. Update only.  # noqa: E501

        :param is_active: The is_active of this FlagsFlagDefinition.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

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
        if issubclass(FlagsFlagDefinition, dict):
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
        if not isinstance(other, FlagsFlagDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

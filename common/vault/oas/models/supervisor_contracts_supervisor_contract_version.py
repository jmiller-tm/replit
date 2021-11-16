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

class SupervisorContractsSupervisorContractVersion(object):
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
        'create_timestamp': 'datetime',
        'supervisor_contract_id': 'str',
        'display_name': 'str',
        'description': 'str',
        'code': 'str',
        'details': 'SupervisorContractsSupervisorContractCodeDetails'
    }

    attribute_map = {
        'id': 'id',
        'create_timestamp': 'create_timestamp',
        'supervisor_contract_id': 'supervisor_contract_id',
        'display_name': 'display_name',
        'description': 'description',
        'code': 'code',
        'details': 'details'
    }

    def __init__(self, id=None, create_timestamp=None, supervisor_contract_id=None, display_name=None, description=None, code=None, details=None):  # noqa: E501
        """SupervisorContractsSupervisorContractVersion - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._create_timestamp = None
        self._supervisor_contract_id = None
        self._display_name = None
        self._description = None
        self._code = None
        self._details = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if create_timestamp is not None:
            self.create_timestamp = create_timestamp
        self.supervisor_contract_id = supervisor_contract_id
        self.display_name = display_name
        self.description = description
        self.code = code
        if details is not None:
            self.details = details

    @property
    def id(self):
        """Gets the id of this SupervisorContractsSupervisorContractVersion.  # noqa: E501

        A unique ID. Can be provided by the client, otherwise it will be a service-generated UUID.   # noqa: E501

        :return: The id of this SupervisorContractsSupervisorContractVersion.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SupervisorContractsSupervisorContractVersion.

        A unique ID. Can be provided by the client, otherwise it will be a service-generated UUID.   # noqa: E501

        :param id: The id of this SupervisorContractsSupervisorContractVersion.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def create_timestamp(self):
        """Gets the create_timestamp of this SupervisorContractsSupervisorContractVersion.  # noqa: E501

        Timestamp indicating when it was created.  # noqa: E501

        :return: The create_timestamp of this SupervisorContractsSupervisorContractVersion.  # noqa: E501
        :rtype: datetime
        """
        return self._create_timestamp

    @create_timestamp.setter
    def create_timestamp(self, create_timestamp):
        """Sets the create_timestamp of this SupervisorContractsSupervisorContractVersion.

        Timestamp indicating when it was created.  # noqa: E501

        :param create_timestamp: The create_timestamp of this SupervisorContractsSupervisorContractVersion.  # noqa: E501
        :type: datetime
        """

        self._create_timestamp = create_timestamp

    @property
    def supervisor_contract_id(self):
        """Gets the supervisor_contract_id of this SupervisorContractsSupervisorContractVersion.  # noqa: E501

        The ID of the `SupervisorContract` of which this is a version.  Required.  # noqa: E501

        :return: The supervisor_contract_id of this SupervisorContractsSupervisorContractVersion.  # noqa: E501
        :rtype: str
        """
        return self._supervisor_contract_id

    @supervisor_contract_id.setter
    def supervisor_contract_id(self, supervisor_contract_id):
        """Sets the supervisor_contract_id of this SupervisorContractsSupervisorContractVersion.

        The ID of the `SupervisorContract` of which this is a version.  Required.  # noqa: E501

        :param supervisor_contract_id: The supervisor_contract_id of this SupervisorContractsSupervisorContractVersion.  # noqa: E501
        :type: str
        """
        if supervisor_contract_id is None:
            raise ValueError("Invalid value for `supervisor_contract_id`, must not be `None`")  # noqa: E501

        self._supervisor_contract_id = supervisor_contract_id

    @property
    def display_name(self):
        """Gets the display_name of this SupervisorContractsSupervisorContractVersion.  # noqa: E501

        The human-readable name.  Required.  # noqa: E501

        :return: The display_name of this SupervisorContractsSupervisorContractVersion.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this SupervisorContractsSupervisorContractVersion.

        The human-readable name.  Required.  # noqa: E501

        :param display_name: The display_name of this SupervisorContractsSupervisorContractVersion.  # noqa: E501
        :type: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this SupervisorContractsSupervisorContractVersion.  # noqa: E501

        The human-readable description.  Required.  # noqa: E501

        :return: The description of this SupervisorContractsSupervisorContractVersion.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SupervisorContractsSupervisorContractVersion.

        The human-readable description.  Required.  # noqa: E501

        :param description: The description of this SupervisorContractsSupervisorContractVersion.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def code(self):
        """Gets the code of this SupervisorContractsSupervisorContractVersion.  # noqa: E501

        The source code.  Required.  # noqa: E501

        :return: The code of this SupervisorContractsSupervisorContractVersion.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this SupervisorContractsSupervisorContractVersion.

        The source code.  Required.  # noqa: E501

        :param code: The code of this SupervisorContractsSupervisorContractVersion.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def details(self):
        """Gets the details of this SupervisorContractsSupervisorContractVersion.  # noqa: E501


        :return: The details of this SupervisorContractsSupervisorContractVersion.  # noqa: E501
        :rtype: SupervisorContractsSupervisorContractCodeDetails
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this SupervisorContractsSupervisorContractVersion.


        :param details: The details of this SupervisorContractsSupervisorContractVersion.  # noqa: E501
        :type: SupervisorContractsSupervisorContractCodeDetails
        """

        self._details = details

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
        if issubclass(SupervisorContractsSupervisorContractVersion, dict):
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
        if not isinstance(other, SupervisorContractsSupervisorContractVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

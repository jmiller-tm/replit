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

class RestrictionsRestrictionSet(object):
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
        'restriction_set_definition_id': 'str',
        'restriction_set_definition_version_id': 'str',
        'name': 'str',
        'restrictions': 'list[RestrictionsRestriction]',
        'description': 'str',
        'restriction_set_parameters': 'dict(str, str)',
        'customer_id': 'str',
        'account_id': 'str',
        'payment_device_id': 'str',
        'effective_timestamp': 'datetime',
        'expiry_timestamp': 'datetime',
        'is_active': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'restriction_set_definition_id': 'restriction_set_definition_id',
        'restriction_set_definition_version_id': 'restriction_set_definition_version_id',
        'name': 'name',
        'restrictions': 'restrictions',
        'description': 'description',
        'restriction_set_parameters': 'restriction_set_parameters',
        'customer_id': 'customer_id',
        'account_id': 'account_id',
        'payment_device_id': 'payment_device_id',
        'effective_timestamp': 'effective_timestamp',
        'expiry_timestamp': 'expiry_timestamp',
        'is_active': 'is_active'
    }

    def __init__(self, id=None, restriction_set_definition_id=None, restriction_set_definition_version_id=None, name=None, restrictions=None, description=None, restriction_set_parameters=None, customer_id=None, account_id=None, payment_device_id=None, effective_timestamp=None, expiry_timestamp=None, is_active=None):  # noqa: E501
        """RestrictionsRestrictionSet - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._restriction_set_definition_id = None
        self._restriction_set_definition_version_id = None
        self._name = None
        self._restrictions = None
        self._description = None
        self._restriction_set_parameters = None
        self._customer_id = None
        self._account_id = None
        self._payment_device_id = None
        self._effective_timestamp = None
        self._expiry_timestamp = None
        self._is_active = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if restriction_set_definition_id is not None:
            self.restriction_set_definition_id = restriction_set_definition_id
        if restriction_set_definition_version_id is not None:
            self.restriction_set_definition_version_id = restriction_set_definition_version_id
        if name is not None:
            self.name = name
        if restrictions is not None:
            self.restrictions = restrictions
        if description is not None:
            self.description = description
        if restriction_set_parameters is not None:
            self.restriction_set_parameters = restriction_set_parameters
        if customer_id is not None:
            self.customer_id = customer_id
        if account_id is not None:
            self.account_id = account_id
        if payment_device_id is not None:
            self.payment_device_id = payment_device_id
        if effective_timestamp is not None:
            self.effective_timestamp = effective_timestamp
        if expiry_timestamp is not None:
            self.expiry_timestamp = expiry_timestamp
        if is_active is not None:
            self.is_active = is_active

    @property
    def id(self):
        """Gets the id of this RestrictionsRestrictionSet.  # noqa: E501

        The unique identifier for this restriction set. Output only.  # noqa: E501

        :return: The id of this RestrictionsRestrictionSet.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RestrictionsRestrictionSet.

        The unique identifier for this restriction set. Output only.  # noqa: E501

        :param id: The id of this RestrictionsRestrictionSet.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def restriction_set_definition_id(self):
        """Gets the restriction_set_definition_id of this RestrictionsRestrictionSet.  # noqa: E501

        The ID of a restriction set definition. Optional for create requests; if not provided for creation, a restriction set definition version ID must be provided.   # noqa: E501

        :return: The restriction_set_definition_id of this RestrictionsRestrictionSet.  # noqa: E501
        :rtype: str
        """
        return self._restriction_set_definition_id

    @restriction_set_definition_id.setter
    def restriction_set_definition_id(self, restriction_set_definition_id):
        """Sets the restriction_set_definition_id of this RestrictionsRestrictionSet.

        The ID of a restriction set definition. Optional for create requests; if not provided for creation, a restriction set definition version ID must be provided.   # noqa: E501

        :param restriction_set_definition_id: The restriction_set_definition_id of this RestrictionsRestrictionSet.  # noqa: E501
        :type: str
        """

        self._restriction_set_definition_id = restriction_set_definition_id

    @property
    def restriction_set_definition_version_id(self):
        """Gets the restriction_set_definition_version_id of this RestrictionsRestrictionSet.  # noqa: E501

        The ID of a restriction set definition version. Optional for create requests; if not provided for creation, a restriction set definition ID must be provided.   # noqa: E501

        :return: The restriction_set_definition_version_id of this RestrictionsRestrictionSet.  # noqa: E501
        :rtype: str
        """
        return self._restriction_set_definition_version_id

    @restriction_set_definition_version_id.setter
    def restriction_set_definition_version_id(self, restriction_set_definition_version_id):
        """Sets the restriction_set_definition_version_id of this RestrictionsRestrictionSet.

        The ID of a restriction set definition version. Optional for create requests; if not provided for creation, a restriction set definition ID must be provided.   # noqa: E501

        :param restriction_set_definition_version_id: The restriction_set_definition_version_id of this RestrictionsRestrictionSet.  # noqa: E501
        :type: str
        """

        self._restriction_set_definition_version_id = restriction_set_definition_version_id

    @property
    def name(self):
        """Gets the name of this RestrictionsRestrictionSet.  # noqa: E501

        The name of the restriction set. Optional.   # noqa: E501

        :return: The name of this RestrictionsRestrictionSet.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RestrictionsRestrictionSet.

        The name of the restriction set. Optional.   # noqa: E501

        :param name: The name of this RestrictionsRestrictionSet.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def restrictions(self):
        """Gets the restrictions of this RestrictionsRestrictionSet.  # noqa: E501

        The restrictions that constitute this restriction set. Output only.  # noqa: E501

        :return: The restrictions of this RestrictionsRestrictionSet.  # noqa: E501
        :rtype: list[RestrictionsRestriction]
        """
        return self._restrictions

    @restrictions.setter
    def restrictions(self, restrictions):
        """Sets the restrictions of this RestrictionsRestrictionSet.

        The restrictions that constitute this restriction set. Output only.  # noqa: E501

        :param restrictions: The restrictions of this RestrictionsRestrictionSet.  # noqa: E501
        :type: list[RestrictionsRestriction]
        """

        self._restrictions = restrictions

    @property
    def description(self):
        """Gets the description of this RestrictionsRestrictionSet.  # noqa: E501

        A description of the restriction set. Optional.   # noqa: E501

        :return: The description of this RestrictionsRestrictionSet.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RestrictionsRestrictionSet.

        A description of the restriction set. Optional.   # noqa: E501

        :param description: The description of this RestrictionsRestrictionSet.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def restriction_set_parameters(self):
        """Gets the restriction_set_parameters of this RestrictionsRestrictionSet.  # noqa: E501

        The restriction parameters for the parameterised restriction types in the restriction set definition. For example, the restriction type LIMIT_DEBITS requires `limit_debits_amount` and`limit_debits_currency` to be included here. Optional unless the restriction set definition version contains restriction types that require parameters.   # noqa: E501

        :return: The restriction_set_parameters of this RestrictionsRestrictionSet.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._restriction_set_parameters

    @restriction_set_parameters.setter
    def restriction_set_parameters(self, restriction_set_parameters):
        """Sets the restriction_set_parameters of this RestrictionsRestrictionSet.

        The restriction parameters for the parameterised restriction types in the restriction set definition. For example, the restriction type LIMIT_DEBITS requires `limit_debits_amount` and`limit_debits_currency` to be included here. Optional unless the restriction set definition version contains restriction types that require parameters.   # noqa: E501

        :param restriction_set_parameters: The restriction_set_parameters of this RestrictionsRestrictionSet.  # noqa: E501
        :type: dict(str, str)
        """

        self._restriction_set_parameters = restriction_set_parameters

    @property
    def customer_id(self):
        """Gets the customer_id of this RestrictionsRestrictionSet.  # noqa: E501

        The ID of the customer the CUSTOMER level restrictions are to be applied to. Required for create requests if there is at least one restriction definition with level CUSTOMER.   # noqa: E501

        :return: The customer_id of this RestrictionsRestrictionSet.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this RestrictionsRestrictionSet.

        The ID of the customer the CUSTOMER level restrictions are to be applied to. Required for create requests if there is at least one restriction definition with level CUSTOMER.   # noqa: E501

        :param customer_id: The customer_id of this RestrictionsRestrictionSet.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def account_id(self):
        """Gets the account_id of this RestrictionsRestrictionSet.  # noqa: E501

        The ID of the account the ACCOUNT level restrictions are to be applied to. Required for create requests if there is at least one restriction definition with level ACCOUNT.   # noqa: E501

        :return: The account_id of this RestrictionsRestrictionSet.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this RestrictionsRestrictionSet.

        The ID of the account the ACCOUNT level restrictions are to be applied to. Required for create requests if there is at least one restriction definition with level ACCOUNT.   # noqa: E501

        :param account_id: The account_id of this RestrictionsRestrictionSet.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def payment_device_id(self):
        """Gets the payment_device_id of this RestrictionsRestrictionSet.  # noqa: E501

        The ID of the payment device the PAYMENT_DEVICE level restrictions are to be applied to. Required for create requests if there is at least one restriction definition with level PAYMENT_DEVICE.   # noqa: E501

        :return: The payment_device_id of this RestrictionsRestrictionSet.  # noqa: E501
        :rtype: str
        """
        return self._payment_device_id

    @payment_device_id.setter
    def payment_device_id(self, payment_device_id):
        """Sets the payment_device_id of this RestrictionsRestrictionSet.

        The ID of the payment device the PAYMENT_DEVICE level restrictions are to be applied to. Required for create requests if there is at least one restriction definition with level PAYMENT_DEVICE.   # noqa: E501

        :param payment_device_id: The payment_device_id of this RestrictionsRestrictionSet.  # noqa: E501
        :type: str
        """

        self._payment_device_id = payment_device_id

    @property
    def effective_timestamp(self):
        """Gets the effective_timestamp of this RestrictionsRestrictionSet.  # noqa: E501

        The time the restriction set should apply from; must be in the future. Optional; default is the current time.   # noqa: E501

        :return: The effective_timestamp of this RestrictionsRestrictionSet.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_timestamp

    @effective_timestamp.setter
    def effective_timestamp(self, effective_timestamp):
        """Sets the effective_timestamp of this RestrictionsRestrictionSet.

        The time the restriction set should apply from; must be in the future. Optional; default is the current time.   # noqa: E501

        :param effective_timestamp: The effective_timestamp of this RestrictionsRestrictionSet.  # noqa: E501
        :type: datetime
        """

        self._effective_timestamp = effective_timestamp

    @property
    def expiry_timestamp(self):
        """Gets the expiry_timestamp of this RestrictionsRestrictionSet.  # noqa: E501

        The time the restriction will expire; must be after the effective_timestamp. Optional; if left empty, the restriction will not expire automatically.   # noqa: E501

        :return: The expiry_timestamp of this RestrictionsRestrictionSet.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry_timestamp

    @expiry_timestamp.setter
    def expiry_timestamp(self, expiry_timestamp):
        """Sets the expiry_timestamp of this RestrictionsRestrictionSet.

        The time the restriction will expire; must be after the effective_timestamp. Optional; if left empty, the restriction will not expire automatically.   # noqa: E501

        :param expiry_timestamp: The expiry_timestamp of this RestrictionsRestrictionSet.  # noqa: E501
        :type: datetime
        """

        self._expiry_timestamp = expiry_timestamp

    @property
    def is_active(self):
        """Gets the is_active of this RestrictionsRestrictionSet.  # noqa: E501

        Indicates if the restriction set is active at the current time or at the time provided when, for example listing restriction sets. Update only.  # noqa: E501

        :return: The is_active of this RestrictionsRestrictionSet.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this RestrictionsRestrictionSet.

        Indicates if the restriction set is active at the current time or at the time provided when, for example listing restriction sets. Update only.  # noqa: E501

        :param is_active: The is_active of this RestrictionsRestrictionSet.  # noqa: E501
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
        if issubclass(RestrictionsRestrictionSet, dict):
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
        if not isinstance(other, RestrictionsRestrictionSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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

class V1OutboundHardSettlement(object):
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
        'amount': 'str',
        'denomination': 'str',
        'target_account': 'V1TargetAccount',
        'internal_account_id': 'str',
        'advice': 'bool',
        'target_account_id': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'denomination': 'denomination',
        'target_account': 'target_account',
        'internal_account_id': 'internal_account_id',
        'advice': 'advice',
        'target_account_id': 'target_account_id'
    }

    def __init__(self, amount=None, denomination=None, target_account=None, internal_account_id=None, advice=None, target_account_id=None):  # noqa: E501
        """V1OutboundHardSettlement - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._denomination = None
        self._target_account = None
        self._internal_account_id = None
        self._advice = None
        self._target_account_id = None
        self.discriminator = None
        if amount is not None:
            self.amount = amount
        if denomination is not None:
            self.denomination = denomination
        if target_account is not None:
            self.target_account = target_account
        if internal_account_id is not None:
            self.internal_account_id = internal_account_id
        if advice is not None:
            self.advice = advice
        if target_account_id is not None:
            self.target_account_id = target_account_id

    @property
    def amount(self):
        """Gets the amount of this V1OutboundHardSettlement.  # noqa: E501

        The instruction amount.  # noqa: E501

        :return: The amount of this V1OutboundHardSettlement.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this V1OutboundHardSettlement.

        The instruction amount.  # noqa: E501

        :param amount: The amount of this V1OutboundHardSettlement.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def denomination(self):
        """Gets the denomination of this V1OutboundHardSettlement.  # noqa: E501

        The instruction denomination.  # noqa: E501

        :return: The denomination of this V1OutboundHardSettlement.  # noqa: E501
        :rtype: str
        """
        return self._denomination

    @denomination.setter
    def denomination(self, denomination):
        """Sets the denomination of this V1OutboundHardSettlement.

        The instruction denomination.  # noqa: E501

        :param denomination: The denomination of this V1OutboundHardSettlement.  # noqa: E501
        :type: str
        """

        self._denomination = denomination

    @property
    def target_account(self):
        """Gets the target_account of this V1OutboundHardSettlement.  # noqa: E501


        :return: The target_account of this V1OutboundHardSettlement.  # noqa: E501
        :rtype: V1TargetAccount
        """
        return self._target_account

    @target_account.setter
    def target_account(self, target_account):
        """Sets the target_account of this V1OutboundHardSettlement.


        :param target_account: The target_account of this V1OutboundHardSettlement.  # noqa: E501
        :type: V1TargetAccount
        """

        self._target_account = target_account

    @property
    def internal_account_id(self):
        """Gets the internal_account_id of this V1OutboundHardSettlement.  # noqa: E501

        The `internal_account_id` must be the ID of an internal account in Vault.  # noqa: E501

        :return: The internal_account_id of this V1OutboundHardSettlement.  # noqa: E501
        :rtype: str
        """
        return self._internal_account_id

    @internal_account_id.setter
    def internal_account_id(self, internal_account_id):
        """Sets the internal_account_id of this V1OutboundHardSettlement.

        The `internal_account_id` must be the ID of an internal account in Vault.  # noqa: E501

        :param internal_account_id: The internal_account_id of this V1OutboundHardSettlement.  # noqa: E501
        :type: str
        """

        self._internal_account_id = internal_account_id

    @property
    def advice(self):
        """Gets the advice of this V1OutboundHardSettlement.  # noqa: E501

        Can be set to true to ensure that funds are ringfenced regardless of the outcome of balance checks. To ensure that posting instructions with `advice` set to true are excluded from the contract balance check, the flag `exclude_advice` must also be set to true. See [Balance check](/reference/contracts/common_examples/#balance_check).  # noqa: E501

        :return: The advice of this V1OutboundHardSettlement.  # noqa: E501
        :rtype: bool
        """
        return self._advice

    @advice.setter
    def advice(self, advice):
        """Sets the advice of this V1OutboundHardSettlement.

        Can be set to true to ensure that funds are ringfenced regardless of the outcome of balance checks. To ensure that posting instructions with `advice` set to true are excluded from the contract balance check, the flag `exclude_advice` must also be set to true. See [Balance check](/reference/contracts/common_examples/#balance_check).  # noqa: E501

        :param advice: The advice of this V1OutboundHardSettlement.  # noqa: E501
        :type: bool
        """

        self._advice = advice

    @property
    def target_account_id(self):
        """Gets the target_account_id of this V1OutboundHardSettlement.  # noqa: E501

        The `account_id` of the instruction's `target_account`.  # noqa: E501

        :return: The target_account_id of this V1OutboundHardSettlement.  # noqa: E501
        :rtype: str
        """
        return self._target_account_id

    @target_account_id.setter
    def target_account_id(self, target_account_id):
        """Sets the target_account_id of this V1OutboundHardSettlement.

        The `account_id` of the instruction's `target_account`.  # noqa: E501

        :param target_account_id: The target_account_id of this V1OutboundHardSettlement.  # noqa: E501
        :type: str
        """

        self._target_account_id = target_account_id

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
        if issubclass(V1OutboundHardSettlement, dict):
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
        if not isinstance(other, V1OutboundHardSettlement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

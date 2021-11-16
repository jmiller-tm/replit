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

class V1Transfer(object):
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
        'debtor_target_account': 'V1TargetAccount',
        'debtor_target_account_id': 'str',
        'creditor_target_account': 'V1TargetAccount',
        'creditor_target_account_id': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'denomination': 'denomination',
        'debtor_target_account': 'debtor_target_account',
        'debtor_target_account_id': 'debtor_target_account_id',
        'creditor_target_account': 'creditor_target_account',
        'creditor_target_account_id': 'creditor_target_account_id'
    }

    def __init__(self, amount=None, denomination=None, debtor_target_account=None, debtor_target_account_id=None, creditor_target_account=None, creditor_target_account_id=None):  # noqa: E501
        """V1Transfer - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._denomination = None
        self._debtor_target_account = None
        self._debtor_target_account_id = None
        self._creditor_target_account = None
        self._creditor_target_account_id = None
        self.discriminator = None
        if amount is not None:
            self.amount = amount
        if denomination is not None:
            self.denomination = denomination
        if debtor_target_account is not None:
            self.debtor_target_account = debtor_target_account
        if debtor_target_account_id is not None:
            self.debtor_target_account_id = debtor_target_account_id
        if creditor_target_account is not None:
            self.creditor_target_account = creditor_target_account
        if creditor_target_account_id is not None:
            self.creditor_target_account_id = creditor_target_account_id

    @property
    def amount(self):
        """Gets the amount of this V1Transfer.  # noqa: E501

        The amount to transfer.  # noqa: E501

        :return: The amount of this V1Transfer.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this V1Transfer.

        The amount to transfer.  # noqa: E501

        :param amount: The amount of this V1Transfer.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def denomination(self):
        """Gets the denomination of this V1Transfer.  # noqa: E501

        The instruction denomination.  # noqa: E501

        :return: The denomination of this V1Transfer.  # noqa: E501
        :rtype: str
        """
        return self._denomination

    @denomination.setter
    def denomination(self, denomination):
        """Sets the denomination of this V1Transfer.

        The instruction denomination.  # noqa: E501

        :param denomination: The denomination of this V1Transfer.  # noqa: E501
        :type: str
        """

        self._denomination = denomination

    @property
    def debtor_target_account(self):
        """Gets the debtor_target_account of this V1Transfer.  # noqa: E501


        :return: The debtor_target_account of this V1Transfer.  # noqa: E501
        :rtype: V1TargetAccount
        """
        return self._debtor_target_account

    @debtor_target_account.setter
    def debtor_target_account(self, debtor_target_account):
        """Sets the debtor_target_account of this V1Transfer.


        :param debtor_target_account: The debtor_target_account of this V1Transfer.  # noqa: E501
        :type: V1TargetAccount
        """

        self._debtor_target_account = debtor_target_account

    @property
    def debtor_target_account_id(self):
        """Gets the debtor_target_account_id of this V1Transfer.  # noqa: E501

        The `account_id` of the debtor.  # noqa: E501

        :return: The debtor_target_account_id of this V1Transfer.  # noqa: E501
        :rtype: str
        """
        return self._debtor_target_account_id

    @debtor_target_account_id.setter
    def debtor_target_account_id(self, debtor_target_account_id):
        """Sets the debtor_target_account_id of this V1Transfer.

        The `account_id` of the debtor.  # noqa: E501

        :param debtor_target_account_id: The debtor_target_account_id of this V1Transfer.  # noqa: E501
        :type: str
        """

        self._debtor_target_account_id = debtor_target_account_id

    @property
    def creditor_target_account(self):
        """Gets the creditor_target_account of this V1Transfer.  # noqa: E501


        :return: The creditor_target_account of this V1Transfer.  # noqa: E501
        :rtype: V1TargetAccount
        """
        return self._creditor_target_account

    @creditor_target_account.setter
    def creditor_target_account(self, creditor_target_account):
        """Sets the creditor_target_account of this V1Transfer.


        :param creditor_target_account: The creditor_target_account of this V1Transfer.  # noqa: E501
        :type: V1TargetAccount
        """

        self._creditor_target_account = creditor_target_account

    @property
    def creditor_target_account_id(self):
        """Gets the creditor_target_account_id of this V1Transfer.  # noqa: E501

        The `account_id` of the creditor.  # noqa: E501

        :return: The creditor_target_account_id of this V1Transfer.  # noqa: E501
        :rtype: str
        """
        return self._creditor_target_account_id

    @creditor_target_account_id.setter
    def creditor_target_account_id(self, creditor_target_account_id):
        """Sets the creditor_target_account_id of this V1Transfer.

        The `account_id` of the creditor.  # noqa: E501

        :param creditor_target_account_id: The creditor_target_account_id of this V1Transfer.  # noqa: E501
        :type: str
        """

        self._creditor_target_account_id = creditor_target_account_id

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
        if issubclass(V1Transfer, dict):
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
        if not isinstance(other, V1Transfer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
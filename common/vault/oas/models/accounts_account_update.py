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

class AccountsAccountUpdate(object):
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
        'status': 'AccountsAccountUpdateStatus',
        'create_timestamp': 'datetime',
        'last_status_update_timestamp': 'datetime',
        'account_update_batch_id': 'str',
        'failure_reason': 'str',
        'instance_param_vals_update': 'AccountsInstanceParamValsUpdate',
        'product_version_update': 'AccountsProductVersionUpdate',
        'activation_update': 'V1accountsActivationUpdate',
        'closure_update': 'V1accountsClosureUpdate'
    }

    attribute_map = {
        'id': 'id',
        'account_id': 'account_id',
        'status': 'status',
        'create_timestamp': 'create_timestamp',
        'last_status_update_timestamp': 'last_status_update_timestamp',
        'account_update_batch_id': 'account_update_batch_id',
        'failure_reason': 'failure_reason',
        'instance_param_vals_update': 'instance_param_vals_update',
        'product_version_update': 'product_version_update',
        'activation_update': 'activation_update',
        'closure_update': 'closure_update'
    }

    def __init__(self, id=None, account_id=None, status=None, create_timestamp=None, last_status_update_timestamp=None, account_update_batch_id=None, failure_reason=None, instance_param_vals_update=None, product_version_update=None, activation_update=None, closure_update=None):  # noqa: E501
        """AccountsAccountUpdate - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._account_id = None
        self._status = None
        self._create_timestamp = None
        self._last_status_update_timestamp = None
        self._account_update_batch_id = None
        self._failure_reason = None
        self._instance_param_vals_update = None
        self._product_version_update = None
        self._activation_update = None
        self._closure_update = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if account_id is not None:
            self.account_id = account_id
        if status is not None:
            self.status = status
        if create_timestamp is not None:
            self.create_timestamp = create_timestamp
        if last_status_update_timestamp is not None:
            self.last_status_update_timestamp = last_status_update_timestamp
        if account_update_batch_id is not None:
            self.account_update_batch_id = account_update_batch_id
        if failure_reason is not None:
            self.failure_reason = failure_reason
        if instance_param_vals_update is not None:
            self.instance_param_vals_update = instance_param_vals_update
        if product_version_update is not None:
            self.product_version_update = product_version_update
        if activation_update is not None:
            self.activation_update = activation_update
        if closure_update is not None:
            self.closure_update = closure_update

    @property
    def id(self):
        """Gets the id of this AccountsAccountUpdate.  # noqa: E501

        A unique identifier for the account update. Optional.  # noqa: E501

        :return: The id of this AccountsAccountUpdate.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AccountsAccountUpdate.

        A unique identifier for the account update. Optional.  # noqa: E501

        :param id: The id of this AccountsAccountUpdate.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def account_id(self):
        """Gets the account_id of this AccountsAccountUpdate.  # noqa: E501

        The Account ID this update applies to. Required for create requests.  # noqa: E501

        :return: The account_id of this AccountsAccountUpdate.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AccountsAccountUpdate.

        The Account ID this update applies to. Required for create requests.  # noqa: E501

        :param account_id: The account_id of this AccountsAccountUpdate.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def status(self):
        """Gets the status of this AccountsAccountUpdate.  # noqa: E501


        :return: The status of this AccountsAccountUpdate.  # noqa: E501
        :rtype: AccountsAccountUpdateStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AccountsAccountUpdate.


        :param status: The status of this AccountsAccountUpdate.  # noqa: E501
        :type: AccountsAccountUpdateStatus
        """

        self._status = status

    @property
    def create_timestamp(self):
        """Gets the create_timestamp of this AccountsAccountUpdate.  # noqa: E501

        A timestamp indicating when the account update was created.  # noqa: E501

        :return: The create_timestamp of this AccountsAccountUpdate.  # noqa: E501
        :rtype: datetime
        """
        return self._create_timestamp

    @create_timestamp.setter
    def create_timestamp(self, create_timestamp):
        """Sets the create_timestamp of this AccountsAccountUpdate.

        A timestamp indicating when the account update was created.  # noqa: E501

        :param create_timestamp: The create_timestamp of this AccountsAccountUpdate.  # noqa: E501
        :type: datetime
        """

        self._create_timestamp = create_timestamp

    @property
    def last_status_update_timestamp(self):
        """Gets the last_status_update_timestamp of this AccountsAccountUpdate.  # noqa: E501

        A timestamp indicating when the last update was performed.  # noqa: E501

        :return: The last_status_update_timestamp of this AccountsAccountUpdate.  # noqa: E501
        :rtype: datetime
        """
        return self._last_status_update_timestamp

    @last_status_update_timestamp.setter
    def last_status_update_timestamp(self, last_status_update_timestamp):
        """Sets the last_status_update_timestamp of this AccountsAccountUpdate.

        A timestamp indicating when the last update was performed.  # noqa: E501

        :param last_status_update_timestamp: The last_status_update_timestamp of this AccountsAccountUpdate.  # noqa: E501
        :type: datetime
        """

        self._last_status_update_timestamp = last_status_update_timestamp

    @property
    def account_update_batch_id(self):
        """Gets the account_update_batch_id of this AccountsAccountUpdate.  # noqa: E501

        The ID of the AccountUpdateBatch if the AccountUpdate was created as part of a batch.  # noqa: E501

        :return: The account_update_batch_id of this AccountsAccountUpdate.  # noqa: E501
        :rtype: str
        """
        return self._account_update_batch_id

    @account_update_batch_id.setter
    def account_update_batch_id(self, account_update_batch_id):
        """Sets the account_update_batch_id of this AccountsAccountUpdate.

        The ID of the AccountUpdateBatch if the AccountUpdate was created as part of a batch.  # noqa: E501

        :param account_update_batch_id: The account_update_batch_id of this AccountsAccountUpdate.  # noqa: E501
        :type: str
        """

        self._account_update_batch_id = account_update_batch_id

    @property
    def failure_reason(self):
        """Gets the failure_reason of this AccountsAccountUpdate.  # noqa: E501

        The reason an account update was not completed successfully. This will only be populated if the account update status is either ACCOUNT_UPDATE_STATUS_REJECTED or ACCOUNT_UPDATE_STATUS_ERRORED.  # noqa: E501

        :return: The failure_reason of this AccountsAccountUpdate.  # noqa: E501
        :rtype: str
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """Sets the failure_reason of this AccountsAccountUpdate.

        The reason an account update was not completed successfully. This will only be populated if the account update status is either ACCOUNT_UPDATE_STATUS_REJECTED or ACCOUNT_UPDATE_STATUS_ERRORED.  # noqa: E501

        :param failure_reason: The failure_reason of this AccountsAccountUpdate.  # noqa: E501
        :type: str
        """

        self._failure_reason = failure_reason

    @property
    def instance_param_vals_update(self):
        """Gets the instance_param_vals_update of this AccountsAccountUpdate.  # noqa: E501


        :return: The instance_param_vals_update of this AccountsAccountUpdate.  # noqa: E501
        :rtype: AccountsInstanceParamValsUpdate
        """
        return self._instance_param_vals_update

    @instance_param_vals_update.setter
    def instance_param_vals_update(self, instance_param_vals_update):
        """Sets the instance_param_vals_update of this AccountsAccountUpdate.


        :param instance_param_vals_update: The instance_param_vals_update of this AccountsAccountUpdate.  # noqa: E501
        :type: AccountsInstanceParamValsUpdate
        """

        self._instance_param_vals_update = instance_param_vals_update

    @property
    def product_version_update(self):
        """Gets the product_version_update of this AccountsAccountUpdate.  # noqa: E501


        :return: The product_version_update of this AccountsAccountUpdate.  # noqa: E501
        :rtype: AccountsProductVersionUpdate
        """
        return self._product_version_update

    @product_version_update.setter
    def product_version_update(self, product_version_update):
        """Sets the product_version_update of this AccountsAccountUpdate.


        :param product_version_update: The product_version_update of this AccountsAccountUpdate.  # noqa: E501
        :type: AccountsProductVersionUpdate
        """

        self._product_version_update = product_version_update

    @property
    def activation_update(self):
        """Gets the activation_update of this AccountsAccountUpdate.  # noqa: E501


        :return: The activation_update of this AccountsAccountUpdate.  # noqa: E501
        :rtype: V1accountsActivationUpdate
        """
        return self._activation_update

    @activation_update.setter
    def activation_update(self, activation_update):
        """Sets the activation_update of this AccountsAccountUpdate.


        :param activation_update: The activation_update of this AccountsAccountUpdate.  # noqa: E501
        :type: V1accountsActivationUpdate
        """

        self._activation_update = activation_update

    @property
    def closure_update(self):
        """Gets the closure_update of this AccountsAccountUpdate.  # noqa: E501


        :return: The closure_update of this AccountsAccountUpdate.  # noqa: E501
        :rtype: V1accountsClosureUpdate
        """
        return self._closure_update

    @closure_update.setter
    def closure_update(self, closure_update):
        """Sets the closure_update of this AccountsAccountUpdate.


        :param closure_update: The closure_update of this AccountsAccountUpdate.  # noqa: E501
        :type: V1accountsClosureUpdate
        """

        self._closure_update = closure_update

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
        if issubclass(AccountsAccountUpdate, dict):
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
        if not isinstance(other, AccountsAccountUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

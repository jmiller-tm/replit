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

class ContractsSimulateContractsResponse(object):
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
        'logs': 'list[str]',
        'posting_instruction_batches': 'list[V1PostingInstructionBatch]',
        'balances': 'dict(str, ContractsBalances)',
        'account_notes': 'dict(str, ContractsAccountNotes)',
        'instantiate_workflow_requests': 'dict(str, ContractsInstantiateWorkflowRequests)',
        'derived_params': 'dict(str, ContractsDerivedParamsVals)'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'logs': 'logs',
        'posting_instruction_batches': 'posting_instruction_batches',
        'balances': 'balances',
        'account_notes': 'account_notes',
        'instantiate_workflow_requests': 'instantiate_workflow_requests',
        'derived_params': 'derived_params'
    }

    def __init__(self, timestamp=None, logs=None, posting_instruction_batches=None, balances=None, account_notes=None, instantiate_workflow_requests=None, derived_params=None):  # noqa: E501
        """ContractsSimulateContractsResponse - a model defined in Swagger"""  # noqa: E501
        self._timestamp = None
        self._logs = None
        self._posting_instruction_batches = None
        self._balances = None
        self._account_notes = None
        self._instantiate_workflow_requests = None
        self._derived_params = None
        self.discriminator = None
        if timestamp is not None:
            self.timestamp = timestamp
        if logs is not None:
            self.logs = logs
        if posting_instruction_batches is not None:
            self.posting_instruction_batches = posting_instruction_batches
        if balances is not None:
            self.balances = balances
        if account_notes is not None:
            self.account_notes = account_notes
        if instantiate_workflow_requests is not None:
            self.instantiate_workflow_requests = instantiate_workflow_requests
        if derived_params is not None:
            self.derived_params = derived_params

    @property
    def timestamp(self):
        """Gets the timestamp of this ContractsSimulateContractsResponse.  # noqa: E501

        Timestamp indicating when this response was generated.  # noqa: E501

        :return: The timestamp of this ContractsSimulateContractsResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ContractsSimulateContractsResponse.

        Timestamp indicating when this response was generated.  # noqa: E501

        :param timestamp: The timestamp of this ContractsSimulateContractsResponse.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def logs(self):
        """Gets the logs of this ContractsSimulateContractsResponse.  # noqa: E501

        A text log that can contain additional information about the simulation. It can include the information about schedule changes, the this response was generated, etc. The information in this log is unstructured and must not be relied upon, as it can change without notice from one Vault release to the other.  # noqa: E501

        :return: The logs of this ContractsSimulateContractsResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        """Sets the logs of this ContractsSimulateContractsResponse.

        A text log that can contain additional information about the simulation. It can include the information about schedule changes, the this response was generated, etc. The information in this log is unstructured and must not be relied upon, as it can change without notice from one Vault release to the other.  # noqa: E501

        :param logs: The logs of this ContractsSimulateContractsResponse.  # noqa: E501
        :type: list[str]
        """

        self._logs = logs

    @property
    def posting_instruction_batches(self):
        """Gets the posting_instruction_batches of this ContractsSimulateContractsResponse.  # noqa: E501

        All Posting Instruction Batches created.  # noqa: E501

        :return: The posting_instruction_batches of this ContractsSimulateContractsResponse.  # noqa: E501
        :rtype: list[V1PostingInstructionBatch]
        """
        return self._posting_instruction_batches

    @posting_instruction_batches.setter
    def posting_instruction_batches(self, posting_instruction_batches):
        """Sets the posting_instruction_batches of this ContractsSimulateContractsResponse.

        All Posting Instruction Batches created.  # noqa: E501

        :param posting_instruction_batches: The posting_instruction_batches of this ContractsSimulateContractsResponse.  # noqa: E501
        :type: list[V1PostingInstructionBatch]
        """

        self._posting_instruction_batches = posting_instruction_batches

    @property
    def balances(self):
        """Gets the balances of this ContractsSimulateContractsResponse.  # noqa: E501

        All balance changes created. Keyed on account ID.  # noqa: E501

        :return: The balances of this ContractsSimulateContractsResponse.  # noqa: E501
        :rtype: dict(str, ContractsBalances)
        """
        return self._balances

    @balances.setter
    def balances(self, balances):
        """Sets the balances of this ContractsSimulateContractsResponse.

        All balance changes created. Keyed on account ID.  # noqa: E501

        :param balances: The balances of this ContractsSimulateContractsResponse.  # noqa: E501
        :type: dict(str, ContractsBalances)
        """

        self._balances = balances

    @property
    def account_notes(self):
        """Gets the account_notes of this ContractsSimulateContractsResponse.  # noqa: E501

        All account notes created. Keyed on account ID.  # noqa: E501

        :return: The account_notes of this ContractsSimulateContractsResponse.  # noqa: E501
        :rtype: dict(str, ContractsAccountNotes)
        """
        return self._account_notes

    @account_notes.setter
    def account_notes(self, account_notes):
        """Sets the account_notes of this ContractsSimulateContractsResponse.

        All account notes created. Keyed on account ID.  # noqa: E501

        :param account_notes: The account_notes of this ContractsSimulateContractsResponse.  # noqa: E501
        :type: dict(str, ContractsAccountNotes)
        """

        self._account_notes = account_notes

    @property
    def instantiate_workflow_requests(self):
        """Gets the instantiate_workflow_requests of this ContractsSimulateContractsResponse.  # noqa: E501

        All Workflow instantiation requests created. Keyed on account ID.  # noqa: E501

        :return: The instantiate_workflow_requests of this ContractsSimulateContractsResponse.  # noqa: E501
        :rtype: dict(str, ContractsInstantiateWorkflowRequests)
        """
        return self._instantiate_workflow_requests

    @instantiate_workflow_requests.setter
    def instantiate_workflow_requests(self, instantiate_workflow_requests):
        """Sets the instantiate_workflow_requests of this ContractsSimulateContractsResponse.

        All Workflow instantiation requests created. Keyed on account ID.  # noqa: E501

        :param instantiate_workflow_requests: The instantiate_workflow_requests of this ContractsSimulateContractsResponse.  # noqa: E501
        :type: dict(str, ContractsInstantiateWorkflowRequests)
        """

        self._instantiate_workflow_requests = instantiate_workflow_requests

    @property
    def derived_params(self):
        """Gets the derived_params of this ContractsSimulateContractsResponse.  # noqa: E501

        All derived parameters. Keyed on account ID.  # noqa: E501

        :return: The derived_params of this ContractsSimulateContractsResponse.  # noqa: E501
        :rtype: dict(str, ContractsDerivedParamsVals)
        """
        return self._derived_params

    @derived_params.setter
    def derived_params(self, derived_params):
        """Sets the derived_params of this ContractsSimulateContractsResponse.

        All derived parameters. Keyed on account ID.  # noqa: E501

        :param derived_params: The derived_params of this ContractsSimulateContractsResponse.  # noqa: E501
        :type: dict(str, ContractsDerivedParamsVals)
        """

        self._derived_params = derived_params

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
        if issubclass(ContractsSimulateContractsResponse, dict):
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
        if not isinstance(other, ContractsSimulateContractsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
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

class V1PostingInstruction(object):
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
        'client_transaction_id': 'str',
        'pics': 'list[str]',
        'instruction_details': 'dict(str, str)',
        'committed_postings': 'list[V1Posting]',
        'posting_violations': 'list[V1PostingViolation]',
        'account_violations': 'list[V1AccountViolation]',
        'restriction_violations': 'list[V1RestrictionViolation]',
        'contract_violations': 'list[V1ContractViolation]',
        'override': 'V1Override',
        'transaction_code': 'V1TransactionCode',
        'outbound_authorisation': 'V1OutboundAuthorisation',
        'inbound_authorisation': 'V1InboundAuthorisation',
        'authorisation_adjustment': 'V1AuthorisationAdjustment',
        'settlement': 'V1Settlement',
        'release': 'V1Release',
        'inbound_hard_settlement': 'V1InboundHardSettlement',
        'outbound_hard_settlement': 'V1OutboundHardSettlement',
        'transfer': 'V1Transfer',
        'custom_instruction': 'V1CustomInstruction'
    }

    attribute_map = {
        'id': 'id',
        'client_transaction_id': 'client_transaction_id',
        'pics': 'pics',
        'instruction_details': 'instruction_details',
        'committed_postings': 'committed_postings',
        'posting_violations': 'posting_violations',
        'account_violations': 'account_violations',
        'restriction_violations': 'restriction_violations',
        'contract_violations': 'contract_violations',
        'override': 'override',
        'transaction_code': 'transaction_code',
        'outbound_authorisation': 'outbound_authorisation',
        'inbound_authorisation': 'inbound_authorisation',
        'authorisation_adjustment': 'authorisation_adjustment',
        'settlement': 'settlement',
        'release': 'release',
        'inbound_hard_settlement': 'inbound_hard_settlement',
        'outbound_hard_settlement': 'outbound_hard_settlement',
        'transfer': 'transfer',
        'custom_instruction': 'custom_instruction'
    }

    def __init__(self, id=None, client_transaction_id=None, pics=None, instruction_details=None, committed_postings=None, posting_violations=None, account_violations=None, restriction_violations=None, contract_violations=None, override=None, transaction_code=None, outbound_authorisation=None, inbound_authorisation=None, authorisation_adjustment=None, settlement=None, release=None, inbound_hard_settlement=None, outbound_hard_settlement=None, transfer=None, custom_instruction=None):  # noqa: E501
        """V1PostingInstruction - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._client_transaction_id = None
        self._pics = None
        self._instruction_details = None
        self._committed_postings = None
        self._posting_violations = None
        self._account_violations = None
        self._restriction_violations = None
        self._contract_violations = None
        self._override = None
        self._transaction_code = None
        self._outbound_authorisation = None
        self._inbound_authorisation = None
        self._authorisation_adjustment = None
        self._settlement = None
        self._release = None
        self._inbound_hard_settlement = None
        self._outbound_hard_settlement = None
        self._transfer = None
        self._custom_instruction = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if client_transaction_id is not None:
            self.client_transaction_id = client_transaction_id
        if pics is not None:
            self.pics = pics
        if instruction_details is not None:
            self.instruction_details = instruction_details
        if committed_postings is not None:
            self.committed_postings = committed_postings
        if posting_violations is not None:
            self.posting_violations = posting_violations
        if account_violations is not None:
            self.account_violations = account_violations
        if restriction_violations is not None:
            self.restriction_violations = restriction_violations
        if contract_violations is not None:
            self.contract_violations = contract_violations
        if override is not None:
            self.override = override
        if transaction_code is not None:
            self.transaction_code = transaction_code
        if outbound_authorisation is not None:
            self.outbound_authorisation = outbound_authorisation
        if inbound_authorisation is not None:
            self.inbound_authorisation = inbound_authorisation
        if authorisation_adjustment is not None:
            self.authorisation_adjustment = authorisation_adjustment
        if settlement is not None:
            self.settlement = settlement
        if release is not None:
            self.release = release
        if inbound_hard_settlement is not None:
            self.inbound_hard_settlement = inbound_hard_settlement
        if outbound_hard_settlement is not None:
            self.outbound_hard_settlement = outbound_hard_settlement
        if transfer is not None:
            self.transfer = transfer
        if custom_instruction is not None:
            self.custom_instruction = custom_instruction

    @property
    def id(self):
        """Gets the id of this V1PostingInstruction.  # noqa: E501

        Created by Vault. This uniquely identifies the posting instruction in Vault.  # noqa: E501

        :return: The id of this V1PostingInstruction.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V1PostingInstruction.

        Created by Vault. This uniquely identifies the posting instruction in Vault.  # noqa: E501

        :param id: The id of this V1PostingInstruction.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def client_transaction_id(self):
        """Gets the client_transaction_id of this V1PostingInstruction.  # noqa: E501

        Set by the client. This is the ID of the client transaction this posting instruction is creating or mutating. Required.  # noqa: E501

        :return: The client_transaction_id of this V1PostingInstruction.  # noqa: E501
        :rtype: str
        """
        return self._client_transaction_id

    @client_transaction_id.setter
    def client_transaction_id(self, client_transaction_id):
        """Sets the client_transaction_id of this V1PostingInstruction.

        Set by the client. This is the ID of the client transaction this posting instruction is creating or mutating. Required.  # noqa: E501

        :param client_transaction_id: The client_transaction_id of this V1PostingInstruction.  # noqa: E501
        :type: str
        """

        self._client_transaction_id = client_transaction_id

    @property
    def pics(self):
        """Gets the pics of this V1PostingInstruction.  # noqa: E501

        Posting Identification Codes that can be associated to posting instruction, and consumed by downstream processes.  # noqa: E501

        :return: The pics of this V1PostingInstruction.  # noqa: E501
        :rtype: list[str]
        """
        return self._pics

    @pics.setter
    def pics(self, pics):
        """Sets the pics of this V1PostingInstruction.

        Posting Identification Codes that can be associated to posting instruction, and consumed by downstream processes.  # noqa: E501

        :param pics: The pics of this V1PostingInstruction.  # noqa: E501
        :type: list[str]
        """

        self._pics = pics

    @property
    def instruction_details(self):
        """Gets the instruction_details of this V1PostingInstruction.  # noqa: E501

        Stores metadata related to the posting instruction. Contract execution will have access to these. If a restriction has exemption conditions and all the exemption conditions are present as key-value pairs, the restriction will not be applied to this posting instruction.  # noqa: E501

        :return: The instruction_details of this V1PostingInstruction.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._instruction_details

    @instruction_details.setter
    def instruction_details(self, instruction_details):
        """Sets the instruction_details of this V1PostingInstruction.

        Stores metadata related to the posting instruction. Contract execution will have access to these. If a restriction has exemption conditions and all the exemption conditions are present as key-value pairs, the restriction will not be applied to this posting instruction.  # noqa: E501

        :param instruction_details: The instruction_details of this V1PostingInstruction.  # noqa: E501
        :type: dict(str, str)
        """

        self._instruction_details = instruction_details

    @property
    def committed_postings(self):
        """Gets the committed_postings of this V1PostingInstruction.  # noqa: E501

        Contains the list of Postings written to the Posting ledger if the posting instruction was accepted.  # noqa: E501

        :return: The committed_postings of this V1PostingInstruction.  # noqa: E501
        :rtype: list[V1Posting]
        """
        return self._committed_postings

    @committed_postings.setter
    def committed_postings(self, committed_postings):
        """Sets the committed_postings of this V1PostingInstruction.

        Contains the list of Postings written to the Posting ledger if the posting instruction was accepted.  # noqa: E501

        :param committed_postings: The committed_postings of this V1PostingInstruction.  # noqa: E501
        :type: list[V1Posting]
        """

        self._committed_postings = committed_postings

    @property
    def posting_violations(self):
        """Gets the posting_violations of this V1PostingInstruction.  # noqa: E501

        Captures rejection reasons caused by posting logic validity checks. For example: Cannot adjust an authorisation that has already been settled.  # noqa: E501

        :return: The posting_violations of this V1PostingInstruction.  # noqa: E501
        :rtype: list[V1PostingViolation]
        """
        return self._posting_violations

    @posting_violations.setter
    def posting_violations(self, posting_violations):
        """Sets the posting_violations of this V1PostingInstruction.

        Captures rejection reasons caused by posting logic validity checks. For example: Cannot adjust an authorisation that has already been settled.  # noqa: E501

        :param posting_violations: The posting_violations of this V1PostingInstruction.  # noqa: E501
        :type: list[V1PostingViolation]
        """

        self._posting_violations = posting_violations

    @property
    def account_violations(self):
        """Gets the account_violations of this V1PostingInstruction.  # noqa: E501

        Captures rejection reasons and details caused by account checks. For example: Account closed.  # noqa: E501

        :return: The account_violations of this V1PostingInstruction.  # noqa: E501
        :rtype: list[V1AccountViolation]
        """
        return self._account_violations

    @account_violations.setter
    def account_violations(self, account_violations):
        """Sets the account_violations of this V1PostingInstruction.

        Captures rejection reasons and details caused by account checks. For example: Account closed.  # noqa: E501

        :param account_violations: The account_violations of this V1PostingInstruction.  # noqa: E501
        :type: list[V1AccountViolation]
        """

        self._account_violations = account_violations

    @property
    def restriction_violations(self):
        """Gets the restriction_violations of this V1PostingInstruction.  # noqa: E501

        Captures rejection reasons and rejection details caused by restrictions. For example: Restriction with ID 'xyz123' prevented this instruction.  # noqa: E501

        :return: The restriction_violations of this V1PostingInstruction.  # noqa: E501
        :rtype: list[V1RestrictionViolation]
        """
        return self._restriction_violations

    @restriction_violations.setter
    def restriction_violations(self, restriction_violations):
        """Sets the restriction_violations of this V1PostingInstruction.

        Captures rejection reasons and rejection details caused by restrictions. For example: Restriction with ID 'xyz123' prevented this instruction.  # noqa: E501

        :param restriction_violations: The restriction_violations of this V1PostingInstruction.  # noqa: E501
        :type: list[V1RestrictionViolation]
        """

        self._restriction_violations = restriction_violations

    @property
    def contract_violations(self):
        """Gets the contract_violations of this V1PostingInstruction.  # noqa: E501

        Captures rejection reasons and rejection details caused by contract execution. For example: Insufficient funds.  # noqa: E501

        :return: The contract_violations of this V1PostingInstruction.  # noqa: E501
        :rtype: list[V1ContractViolation]
        """
        return self._contract_violations

    @contract_violations.setter
    def contract_violations(self, contract_violations):
        """Sets the contract_violations of this V1PostingInstruction.

        Captures rejection reasons and rejection details caused by contract execution. For example: Insufficient funds.  # noqa: E501

        :param contract_violations: The contract_violations of this V1PostingInstruction.  # noqa: E501
        :type: list[V1ContractViolation]
        """

        self._contract_violations = contract_violations

    @property
    def override(self):
        """Gets the override of this V1PostingInstruction.  # noqa: E501


        :return: The override of this V1PostingInstruction.  # noqa: E501
        :rtype: V1Override
        """
        return self._override

    @override.setter
    def override(self, override):
        """Sets the override of this V1PostingInstruction.


        :param override: The override of this V1PostingInstruction.  # noqa: E501
        :type: V1Override
        """

        self._override = override

    @property
    def transaction_code(self):
        """Gets the transaction_code of this V1PostingInstruction.  # noqa: E501


        :return: The transaction_code of this V1PostingInstruction.  # noqa: E501
        :rtype: V1TransactionCode
        """
        return self._transaction_code

    @transaction_code.setter
    def transaction_code(self, transaction_code):
        """Sets the transaction_code of this V1PostingInstruction.


        :param transaction_code: The transaction_code of this V1PostingInstruction.  # noqa: E501
        :type: V1TransactionCode
        """

        self._transaction_code = transaction_code

    @property
    def outbound_authorisation(self):
        """Gets the outbound_authorisation of this V1PostingInstruction.  # noqa: E501


        :return: The outbound_authorisation of this V1PostingInstruction.  # noqa: E501
        :rtype: V1OutboundAuthorisation
        """
        return self._outbound_authorisation

    @outbound_authorisation.setter
    def outbound_authorisation(self, outbound_authorisation):
        """Sets the outbound_authorisation of this V1PostingInstruction.


        :param outbound_authorisation: The outbound_authorisation of this V1PostingInstruction.  # noqa: E501
        :type: V1OutboundAuthorisation
        """

        self._outbound_authorisation = outbound_authorisation

    @property
    def inbound_authorisation(self):
        """Gets the inbound_authorisation of this V1PostingInstruction.  # noqa: E501


        :return: The inbound_authorisation of this V1PostingInstruction.  # noqa: E501
        :rtype: V1InboundAuthorisation
        """
        return self._inbound_authorisation

    @inbound_authorisation.setter
    def inbound_authorisation(self, inbound_authorisation):
        """Sets the inbound_authorisation of this V1PostingInstruction.


        :param inbound_authorisation: The inbound_authorisation of this V1PostingInstruction.  # noqa: E501
        :type: V1InboundAuthorisation
        """

        self._inbound_authorisation = inbound_authorisation

    @property
    def authorisation_adjustment(self):
        """Gets the authorisation_adjustment of this V1PostingInstruction.  # noqa: E501


        :return: The authorisation_adjustment of this V1PostingInstruction.  # noqa: E501
        :rtype: V1AuthorisationAdjustment
        """
        return self._authorisation_adjustment

    @authorisation_adjustment.setter
    def authorisation_adjustment(self, authorisation_adjustment):
        """Sets the authorisation_adjustment of this V1PostingInstruction.


        :param authorisation_adjustment: The authorisation_adjustment of this V1PostingInstruction.  # noqa: E501
        :type: V1AuthorisationAdjustment
        """

        self._authorisation_adjustment = authorisation_adjustment

    @property
    def settlement(self):
        """Gets the settlement of this V1PostingInstruction.  # noqa: E501


        :return: The settlement of this V1PostingInstruction.  # noqa: E501
        :rtype: V1Settlement
        """
        return self._settlement

    @settlement.setter
    def settlement(self, settlement):
        """Sets the settlement of this V1PostingInstruction.


        :param settlement: The settlement of this V1PostingInstruction.  # noqa: E501
        :type: V1Settlement
        """

        self._settlement = settlement

    @property
    def release(self):
        """Gets the release of this V1PostingInstruction.  # noqa: E501


        :return: The release of this V1PostingInstruction.  # noqa: E501
        :rtype: V1Release
        """
        return self._release

    @release.setter
    def release(self, release):
        """Sets the release of this V1PostingInstruction.


        :param release: The release of this V1PostingInstruction.  # noqa: E501
        :type: V1Release
        """

        self._release = release

    @property
    def inbound_hard_settlement(self):
        """Gets the inbound_hard_settlement of this V1PostingInstruction.  # noqa: E501


        :return: The inbound_hard_settlement of this V1PostingInstruction.  # noqa: E501
        :rtype: V1InboundHardSettlement
        """
        return self._inbound_hard_settlement

    @inbound_hard_settlement.setter
    def inbound_hard_settlement(self, inbound_hard_settlement):
        """Sets the inbound_hard_settlement of this V1PostingInstruction.


        :param inbound_hard_settlement: The inbound_hard_settlement of this V1PostingInstruction.  # noqa: E501
        :type: V1InboundHardSettlement
        """

        self._inbound_hard_settlement = inbound_hard_settlement

    @property
    def outbound_hard_settlement(self):
        """Gets the outbound_hard_settlement of this V1PostingInstruction.  # noqa: E501


        :return: The outbound_hard_settlement of this V1PostingInstruction.  # noqa: E501
        :rtype: V1OutboundHardSettlement
        """
        return self._outbound_hard_settlement

    @outbound_hard_settlement.setter
    def outbound_hard_settlement(self, outbound_hard_settlement):
        """Sets the outbound_hard_settlement of this V1PostingInstruction.


        :param outbound_hard_settlement: The outbound_hard_settlement of this V1PostingInstruction.  # noqa: E501
        :type: V1OutboundHardSettlement
        """

        self._outbound_hard_settlement = outbound_hard_settlement

    @property
    def transfer(self):
        """Gets the transfer of this V1PostingInstruction.  # noqa: E501


        :return: The transfer of this V1PostingInstruction.  # noqa: E501
        :rtype: V1Transfer
        """
        return self._transfer

    @transfer.setter
    def transfer(self, transfer):
        """Sets the transfer of this V1PostingInstruction.


        :param transfer: The transfer of this V1PostingInstruction.  # noqa: E501
        :type: V1Transfer
        """

        self._transfer = transfer

    @property
    def custom_instruction(self):
        """Gets the custom_instruction of this V1PostingInstruction.  # noqa: E501


        :return: The custom_instruction of this V1PostingInstruction.  # noqa: E501
        :rtype: V1CustomInstruction
        """
        return self._custom_instruction

    @custom_instruction.setter
    def custom_instruction(self, custom_instruction):
        """Sets the custom_instruction of this V1PostingInstruction.


        :param custom_instruction: The custom_instruction of this V1PostingInstruction.  # noqa: E501
        :type: V1CustomInstruction
        """

        self._custom_instruction = custom_instruction

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
        if issubclass(V1PostingInstruction, dict):
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
        if not isinstance(other, V1PostingInstruction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
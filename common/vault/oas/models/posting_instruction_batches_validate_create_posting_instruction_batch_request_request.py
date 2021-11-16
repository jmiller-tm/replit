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

class PostingInstructionBatchesValidateCreatePostingInstructionBatchRequestRequest(object):
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
        'request_id': 'str',
        'posting_instruction_batch': 'V1PostingInstructionBatch'
    }

    attribute_map = {
        'request_id': 'request_id',
        'posting_instruction_batch': 'posting_instruction_batch'
    }

    def __init__(self, request_id=None, posting_instruction_batch=None):  # noqa: E501
        """PostingInstructionBatchesValidateCreatePostingInstructionBatchRequestRequest - a model defined in Swagger"""  # noqa: E501
        self._request_id = None
        self._posting_instruction_batch = None
        self.discriminator = None
        if request_id is not None:
            self.request_id = request_id
        if posting_instruction_batch is not None:
            self.posting_instruction_batch = posting_instruction_batch

    @property
    def request_id(self):
        """Gets the request_id of this PostingInstructionBatchesValidateCreatePostingInstructionBatchRequestRequest.  # noqa: E501

        A unique ID generated by the client (payment processor) that is used for idempotency. The client must ensure a unique `request_id` is passed within their namespace (determined by `client_id`). Multiple requests with the same <`client_id` - `request_id`> will receive the same response. Required.  # noqa: E501

        :return: The request_id of this PostingInstructionBatchesValidateCreatePostingInstructionBatchRequestRequest.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this PostingInstructionBatchesValidateCreatePostingInstructionBatchRequestRequest.

        A unique ID generated by the client (payment processor) that is used for idempotency. The client must ensure a unique `request_id` is passed within their namespace (determined by `client_id`). Multiple requests with the same <`client_id` - `request_id`> will receive the same response. Required.  # noqa: E501

        :param request_id: The request_id of this PostingInstructionBatchesValidateCreatePostingInstructionBatchRequestRequest.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def posting_instruction_batch(self):
        """Gets the posting_instruction_batch of this PostingInstructionBatchesValidateCreatePostingInstructionBatchRequestRequest.  # noqa: E501


        :return: The posting_instruction_batch of this PostingInstructionBatchesValidateCreatePostingInstructionBatchRequestRequest.  # noqa: E501
        :rtype: V1PostingInstructionBatch
        """
        return self._posting_instruction_batch

    @posting_instruction_batch.setter
    def posting_instruction_batch(self, posting_instruction_batch):
        """Sets the posting_instruction_batch of this PostingInstructionBatchesValidateCreatePostingInstructionBatchRequestRequest.


        :param posting_instruction_batch: The posting_instruction_batch of this PostingInstructionBatchesValidateCreatePostingInstructionBatchRequestRequest.  # noqa: E501
        :type: V1PostingInstructionBatch
        """

        self._posting_instruction_batch = posting_instruction_batch

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
        if issubclass(PostingInstructionBatchesValidateCreatePostingInstructionBatchRequestRequest, dict):
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
        if not isinstance(other, PostingInstructionBatchesValidateCreatePostingInstructionBatchRequestRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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

class PostingInstructionBatchesValidateCreatePostingInstructionBatchRequestResponse(object):
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
        'is_valid': 'bool',
        'failure_reason': 'str'
    }

    attribute_map = {
        'is_valid': 'is_valid',
        'failure_reason': 'failure_reason'
    }

    def __init__(self, is_valid=None, failure_reason=None):  # noqa: E501
        """PostingInstructionBatchesValidateCreatePostingInstructionBatchRequestResponse - a model defined in Swagger"""  # noqa: E501
        self._is_valid = None
        self._failure_reason = None
        self.discriminator = None
        if is_valid is not None:
            self.is_valid = is_valid
        if failure_reason is not None:
            self.failure_reason = failure_reason

    @property
    def is_valid(self):
        """Gets the is_valid of this PostingInstructionBatchesValidateCreatePostingInstructionBatchRequestResponse.  # noqa: E501

        Indicates whether the syntax of the `create-posting-instruction-batch` request is valid.  # noqa: E501

        :return: The is_valid of this PostingInstructionBatchesValidateCreatePostingInstructionBatchRequestResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        """Sets the is_valid of this PostingInstructionBatchesValidateCreatePostingInstructionBatchRequestResponse.

        Indicates whether the syntax of the `create-posting-instruction-batch` request is valid.  # noqa: E501

        :param is_valid: The is_valid of this PostingInstructionBatchesValidateCreatePostingInstructionBatchRequestResponse.  # noqa: E501
        :type: bool
        """

        self._is_valid = is_valid

    @property
    def failure_reason(self):
        """Gets the failure_reason of this PostingInstructionBatchesValidateCreatePostingInstructionBatchRequestResponse.  # noqa: E501

        A string that communicates the reason why the `create-posting-instruction-batch` request failed validation. Optional.  # noqa: E501

        :return: The failure_reason of this PostingInstructionBatchesValidateCreatePostingInstructionBatchRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """Sets the failure_reason of this PostingInstructionBatchesValidateCreatePostingInstructionBatchRequestResponse.

        A string that communicates the reason why the `create-posting-instruction-batch` request failed validation. Optional.  # noqa: E501

        :param failure_reason: The failure_reason of this PostingInstructionBatchesValidateCreatePostingInstructionBatchRequestResponse.  # noqa: E501
        :type: str
        """

        self._failure_reason = failure_reason

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
        if issubclass(PostingInstructionBatchesValidateCreatePostingInstructionBatchRequestResponse, dict):
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
        if not isinstance(other, PostingInstructionBatchesValidateCreatePostingInstructionBatchRequestResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

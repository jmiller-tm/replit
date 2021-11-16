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

class AuthServiceAccountTokenUpdateOptions(object):
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
        'refresh_token': 'bool'
    }

    attribute_map = {
        'refresh_token': 'refresh_token'
    }

    def __init__(self, refresh_token=None):  # noqa: E501
        """AuthServiceAccountTokenUpdateOptions - a model defined in Swagger"""  # noqa: E501
        self._refresh_token = None
        self.discriminator = None
        if refresh_token is not None:
            self.refresh_token = refresh_token

    @property
    def refresh_token(self):
        """Gets the refresh_token of this AuthServiceAccountTokenUpdateOptions.  # noqa: E501

        Replaces the existing service account token with a new service account token. A service account token can only be refreshed for an active service account. Token refresh cannot be performed at the same time as a status change.  # noqa: E501

        :return: The refresh_token of this AuthServiceAccountTokenUpdateOptions.  # noqa: E501
        :rtype: bool
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """Sets the refresh_token of this AuthServiceAccountTokenUpdateOptions.

        Replaces the existing service account token with a new service account token. A service account token can only be refreshed for an active service account. Token refresh cannot be performed at the same time as a status change.  # noqa: E501

        :param refresh_token: The refresh_token of this AuthServiceAccountTokenUpdateOptions.  # noqa: E501
        :type: bool
        """

        self._refresh_token = refresh_token

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
        if issubclass(AuthServiceAccountTokenUpdateOptions, dict):
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
        if not isinstance(other, AuthServiceAccountTokenUpdateOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
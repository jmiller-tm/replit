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

class RestrictionsUpdateRestrictionSetRequest(object):
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
        'restriction_set': 'RestrictionsRestrictionSet',
        'request_id': 'str',
        'update_mask': 'ProtobufFieldMask'
    }

    attribute_map = {
        'restriction_set': 'restriction_set',
        'request_id': 'request_id',
        'update_mask': 'update_mask'
    }

    def __init__(self, restriction_set=None, request_id=None, update_mask=None):  # noqa: E501
        """RestrictionsUpdateRestrictionSetRequest - a model defined in Swagger"""  # noqa: E501
        self._restriction_set = None
        self._request_id = None
        self._update_mask = None
        self.discriminator = None
        if restriction_set is not None:
            self.restriction_set = restriction_set
        self.request_id = request_id
        if update_mask is not None:
            self.update_mask = update_mask

    @property
    def restriction_set(self):
        """Gets the restriction_set of this RestrictionsUpdateRestrictionSetRequest.  # noqa: E501


        :return: The restriction_set of this RestrictionsUpdateRestrictionSetRequest.  # noqa: E501
        :rtype: RestrictionsRestrictionSet
        """
        return self._restriction_set

    @restriction_set.setter
    def restriction_set(self, restriction_set):
        """Sets the restriction_set of this RestrictionsUpdateRestrictionSetRequest.


        :param restriction_set: The restriction_set of this RestrictionsUpdateRestrictionSetRequest.  # noqa: E501
        :type: RestrictionsRestrictionSet
        """

        self._restriction_set = restriction_set

    @property
    def request_id(self):
        """Gets the request_id of this RestrictionsUpdateRestrictionSetRequest.  # noqa: E501

        The unique string ID used to ensure this request is idempotent. Required.  Required. Max length: 256 characters.  # noqa: E501

        :return: The request_id of this RestrictionsUpdateRestrictionSetRequest.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this RestrictionsUpdateRestrictionSetRequest.

        The unique string ID used to ensure this request is idempotent. Required.  Required. Max length: 256 characters.  # noqa: E501

        :param request_id: The request_id of this RestrictionsUpdateRestrictionSetRequest.  # noqa: E501
        :type: str
        """
        if request_id is None:
            raise ValueError("Invalid value for `request_id`, must not be `None`")  # noqa: E501

        self._request_id = request_id

    @property
    def update_mask(self):
        """Gets the update_mask of this RestrictionsUpdateRestrictionSetRequest.  # noqa: E501


        :return: The update_mask of this RestrictionsUpdateRestrictionSetRequest.  # noqa: E501
        :rtype: ProtobufFieldMask
        """
        return self._update_mask

    @update_mask.setter
    def update_mask(self, update_mask):
        """Sets the update_mask of this RestrictionsUpdateRestrictionSetRequest.


        :param update_mask: The update_mask of this RestrictionsUpdateRestrictionSetRequest.  # noqa: E501
        :type: ProtobufFieldMask
        """

        self._update_mask = update_mask

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
        if issubclass(RestrictionsUpdateRestrictionSetRequest, dict):
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
        if not isinstance(other, RestrictionsUpdateRestrictionSetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

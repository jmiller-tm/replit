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

class ProductsListProductVersionParametersTimeseriesResponse(object):
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
        'product_version_param_timeseries': 'list[ProductsParameterTimeseries]'
    }

    attribute_map = {
        'product_version_param_timeseries': 'product_version_param_timeseries'
    }

    def __init__(self, product_version_param_timeseries=None):  # noqa: E501
        """ProductsListProductVersionParametersTimeseriesResponse - a model defined in Swagger"""  # noqa: E501
        self._product_version_param_timeseries = None
        self.discriminator = None
        if product_version_param_timeseries is not None:
            self.product_version_param_timeseries = product_version_param_timeseries

    @property
    def product_version_param_timeseries(self):
        """Gets the product_version_param_timeseries of this ProductsListProductVersionParametersTimeseriesResponse.  # noqa: E501

        The product version parameter timeseries that is retrieved for the specified product version ID.  # noqa: E501

        :return: The product_version_param_timeseries of this ProductsListProductVersionParametersTimeseriesResponse.  # noqa: E501
        :rtype: list[ProductsParameterTimeseries]
        """
        return self._product_version_param_timeseries

    @product_version_param_timeseries.setter
    def product_version_param_timeseries(self, product_version_param_timeseries):
        """Sets the product_version_param_timeseries of this ProductsListProductVersionParametersTimeseriesResponse.

        The product version parameter timeseries that is retrieved for the specified product version ID.  # noqa: E501

        :param product_version_param_timeseries: The product_version_param_timeseries of this ProductsListProductVersionParametersTimeseriesResponse.  # noqa: E501
        :type: list[ProductsParameterTimeseries]
        """

        self._product_version_param_timeseries = product_version_param_timeseries

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
        if issubclass(ProductsListProductVersionParametersTimeseriesResponse, dict):
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
        if not isinstance(other, ProductsListProductVersionParametersTimeseriesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

"""
    Codat API

    [What's changed in our Swagger](https://docs.codat.io/docs/new-swagger-ui)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CodatDataContractsDatasetsCommerceProductVariantPrice(object):
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
        'currency': 'str',
        'unit_price': 'float'
    }

    attribute_map = {
        'currency': 'currency',
        'unit_price': 'unitPrice'
    }

    def __init__(self, currency=None, unit_price=None):  # noqa: E501
        """CodatDataContractsDatasetsCommerceProductVariantPrice - a model defined in Swagger"""  # noqa: E501
        self._currency = None
        self._unit_price = None
        self.discriminator = None
        if currency is not None:
            self.currency = currency
        if unit_price is not None:
            self.unit_price = unit_price

    @property
    def currency(self):
        """Gets the currency of this CodatDataContractsDatasetsCommerceProductVariantPrice.  # noqa: E501


        :return: The currency of this CodatDataContractsDatasetsCommerceProductVariantPrice.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this CodatDataContractsDatasetsCommerceProductVariantPrice.


        :param currency: The currency of this CodatDataContractsDatasetsCommerceProductVariantPrice.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def unit_price(self):
        """Gets the unit_price of this CodatDataContractsDatasetsCommerceProductVariantPrice.  # noqa: E501


        :return: The unit_price of this CodatDataContractsDatasetsCommerceProductVariantPrice.  # noqa: E501
        :rtype: float
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this CodatDataContractsDatasetsCommerceProductVariantPrice.


        :param unit_price: The unit_price of this CodatDataContractsDatasetsCommerceProductVariantPrice.  # noqa: E501
        :type: float
        """

        self._unit_price = unit_price

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
        if issubclass(CodatDataContractsDatasetsCommerceProductVariantPrice, dict):
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
        if not isinstance(other, CodatDataContractsDatasetsCommerceProductVariantPrice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

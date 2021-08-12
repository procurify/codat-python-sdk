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

class CodatDataContractsDatasetsCommerceServiceCharge(object):
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
        'description': 'str',
        'total_amount': 'float',
        'tax_percentage': 'float',
        'tax_amount': 'float',
        'quantity': 'int',
        'type': 'CodatDataContractsDatasetsCommerceServiceChargeType'
    }

    attribute_map = {
        'description': 'description',
        'total_amount': 'totalAmount',
        'tax_percentage': 'taxPercentage',
        'tax_amount': 'taxAmount',
        'quantity': 'quantity',
        'type': 'type'
    }

    def __init__(self, description=None, total_amount=None, tax_percentage=None, tax_amount=None, quantity=None, type=None):  # noqa: E501
        """CodatDataContractsDatasetsCommerceServiceCharge - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._total_amount = None
        self._tax_percentage = None
        self._tax_amount = None
        self._quantity = None
        self._type = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if total_amount is not None:
            self.total_amount = total_amount
        if tax_percentage is not None:
            self.tax_percentage = tax_percentage
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if quantity is not None:
            self.quantity = quantity
        if type is not None:
            self.type = type

    @property
    def description(self):
        """Gets the description of this CodatDataContractsDatasetsCommerceServiceCharge.  # noqa: E501


        :return: The description of this CodatDataContractsDatasetsCommerceServiceCharge.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CodatDataContractsDatasetsCommerceServiceCharge.


        :param description: The description of this CodatDataContractsDatasetsCommerceServiceCharge.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def total_amount(self):
        """Gets the total_amount of this CodatDataContractsDatasetsCommerceServiceCharge.  # noqa: E501


        :return: The total_amount of this CodatDataContractsDatasetsCommerceServiceCharge.  # noqa: E501
        :rtype: float
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this CodatDataContractsDatasetsCommerceServiceCharge.


        :param total_amount: The total_amount of this CodatDataContractsDatasetsCommerceServiceCharge.  # noqa: E501
        :type: float
        """

        self._total_amount = total_amount

    @property
    def tax_percentage(self):
        """Gets the tax_percentage of this CodatDataContractsDatasetsCommerceServiceCharge.  # noqa: E501


        :return: The tax_percentage of this CodatDataContractsDatasetsCommerceServiceCharge.  # noqa: E501
        :rtype: float
        """
        return self._tax_percentage

    @tax_percentage.setter
    def tax_percentage(self, tax_percentage):
        """Sets the tax_percentage of this CodatDataContractsDatasetsCommerceServiceCharge.


        :param tax_percentage: The tax_percentage of this CodatDataContractsDatasetsCommerceServiceCharge.  # noqa: E501
        :type: float
        """

        self._tax_percentage = tax_percentage

    @property
    def tax_amount(self):
        """Gets the tax_amount of this CodatDataContractsDatasetsCommerceServiceCharge.  # noqa: E501


        :return: The tax_amount of this CodatDataContractsDatasetsCommerceServiceCharge.  # noqa: E501
        :rtype: float
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this CodatDataContractsDatasetsCommerceServiceCharge.


        :param tax_amount: The tax_amount of this CodatDataContractsDatasetsCommerceServiceCharge.  # noqa: E501
        :type: float
        """

        self._tax_amount = tax_amount

    @property
    def quantity(self):
        """Gets the quantity of this CodatDataContractsDatasetsCommerceServiceCharge.  # noqa: E501


        :return: The quantity of this CodatDataContractsDatasetsCommerceServiceCharge.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this CodatDataContractsDatasetsCommerceServiceCharge.


        :param quantity: The quantity of this CodatDataContractsDatasetsCommerceServiceCharge.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def type(self):
        """Gets the type of this CodatDataContractsDatasetsCommerceServiceCharge.  # noqa: E501


        :return: The type of this CodatDataContractsDatasetsCommerceServiceCharge.  # noqa: E501
        :rtype: CodatDataContractsDatasetsCommerceServiceChargeType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CodatDataContractsDatasetsCommerceServiceCharge.


        :param type: The type of this CodatDataContractsDatasetsCommerceServiceCharge.  # noqa: E501
        :type: CodatDataContractsDatasetsCommerceServiceChargeType
        """

        self._type = type

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
        if issubclass(CodatDataContractsDatasetsCommerceServiceCharge, dict):
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
        if not isinstance(other, CodatDataContractsDatasetsCommerceServiceCharge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

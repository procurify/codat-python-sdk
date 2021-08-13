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

class CodatDataContractsDatasetsPaymentLine(object):
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
        'amount': 'float',
        'links': 'list[CodatDataContractsDatasetsPaymentLineLink]',
        'allocated_on_date': 'datetime'
    }

    attribute_map = {
        'amount': 'amount',
        'links': 'links',
        'allocated_on_date': 'allocatedOnDate'
    }

    def __init__(self, amount=None, links=None, allocated_on_date=None):  # noqa: E501
        """CodatDataContractsDatasetsPaymentLine - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._links = None
        self._allocated_on_date = None
        self.discriminator = None
        self.amount = amount
        if links is not None:
            self.links = links
        if allocated_on_date is not None:
            self.allocated_on_date = allocated_on_date

    @property
    def amount(self):
        """Gets the amount of this CodatDataContractsDatasetsPaymentLine.  # noqa: E501


        :return: The amount of this CodatDataContractsDatasetsPaymentLine.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CodatDataContractsDatasetsPaymentLine.


        :param amount: The amount of this CodatDataContractsDatasetsPaymentLine.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def links(self):
        """Gets the links of this CodatDataContractsDatasetsPaymentLine.  # noqa: E501


        :return: The links of this CodatDataContractsDatasetsPaymentLine.  # noqa: E501
        :rtype: list[CodatDataContractsDatasetsPaymentLineLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CodatDataContractsDatasetsPaymentLine.


        :param links: The links of this CodatDataContractsDatasetsPaymentLine.  # noqa: E501
        :type: list[CodatDataContractsDatasetsPaymentLineLink]
        """

        self._links = links

    @property
    def allocated_on_date(self):
        """Gets the allocated_on_date of this CodatDataContractsDatasetsPaymentLine.  # noqa: E501


        :return: The allocated_on_date of this CodatDataContractsDatasetsPaymentLine.  # noqa: E501
        :rtype: datetime
        """
        return self._allocated_on_date

    @allocated_on_date.setter
    def allocated_on_date(self, allocated_on_date):
        """Sets the allocated_on_date of this CodatDataContractsDatasetsPaymentLine.


        :param allocated_on_date: The allocated_on_date of this CodatDataContractsDatasetsPaymentLine.  # noqa: E501
        :type: datetime
        """

        self._allocated_on_date = allocated_on_date

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
        if issubclass(CodatDataContractsDatasetsPaymentLine, dict):
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
        if not isinstance(other, CodatDataContractsDatasetsPaymentLine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
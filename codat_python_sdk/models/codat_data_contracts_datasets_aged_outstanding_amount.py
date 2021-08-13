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

class CodatDataContractsDatasetsAgedOutstandingAmount(object):
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
        'from_date': 'datetime',
        'to_date': 'datetime',
        'amount': 'float',
        'details': 'list[CodatDataContractsDatasetsAgedOutstandingAmountDetail]'
    }

    attribute_map = {
        'from_date': 'fromDate',
        'to_date': 'toDate',
        'amount': 'amount',
        'details': 'details'
    }

    def __init__(self, from_date=None, to_date=None, amount=None, details=None):  # noqa: E501
        """CodatDataContractsDatasetsAgedOutstandingAmount - a model defined in Swagger"""  # noqa: E501
        self._from_date = None
        self._to_date = None
        self._amount = None
        self._details = None
        self.discriminator = None
        if from_date is not None:
            self.from_date = from_date
        if to_date is not None:
            self.to_date = to_date
        if amount is not None:
            self.amount = amount
        if details is not None:
            self.details = details

    @property
    def from_date(self):
        """Gets the from_date of this CodatDataContractsDatasetsAgedOutstandingAmount.  # noqa: E501


        :return: The from_date of this CodatDataContractsDatasetsAgedOutstandingAmount.  # noqa: E501
        :rtype: datetime
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """Sets the from_date of this CodatDataContractsDatasetsAgedOutstandingAmount.


        :param from_date: The from_date of this CodatDataContractsDatasetsAgedOutstandingAmount.  # noqa: E501
        :type: datetime
        """

        self._from_date = from_date

    @property
    def to_date(self):
        """Gets the to_date of this CodatDataContractsDatasetsAgedOutstandingAmount.  # noqa: E501


        :return: The to_date of this CodatDataContractsDatasetsAgedOutstandingAmount.  # noqa: E501
        :rtype: datetime
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        """Sets the to_date of this CodatDataContractsDatasetsAgedOutstandingAmount.


        :param to_date: The to_date of this CodatDataContractsDatasetsAgedOutstandingAmount.  # noqa: E501
        :type: datetime
        """

        self._to_date = to_date

    @property
    def amount(self):
        """Gets the amount of this CodatDataContractsDatasetsAgedOutstandingAmount.  # noqa: E501


        :return: The amount of this CodatDataContractsDatasetsAgedOutstandingAmount.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CodatDataContractsDatasetsAgedOutstandingAmount.


        :param amount: The amount of this CodatDataContractsDatasetsAgedOutstandingAmount.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def details(self):
        """Gets the details of this CodatDataContractsDatasetsAgedOutstandingAmount.  # noqa: E501


        :return: The details of this CodatDataContractsDatasetsAgedOutstandingAmount.  # noqa: E501
        :rtype: list[CodatDataContractsDatasetsAgedOutstandingAmountDetail]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this CodatDataContractsDatasetsAgedOutstandingAmount.


        :param details: The details of this CodatDataContractsDatasetsAgedOutstandingAmount.  # noqa: E501
        :type: list[CodatDataContractsDatasetsAgedOutstandingAmountDetail]
        """

        self._details = details

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
        if issubclass(CodatDataContractsDatasetsAgedOutstandingAmount, dict):
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
        if not isinstance(other, CodatDataContractsDatasetsAgedOutstandingAmount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

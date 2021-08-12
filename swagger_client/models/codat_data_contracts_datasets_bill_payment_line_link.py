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

class CodatDataContractsDatasetsBillPaymentLineLink(object):
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
        'type': 'CodatDataContractsDatasetsBillPaymentLinkType',
        'id': 'str',
        'amount': 'float',
        'currency_rate': 'float'
    }

    attribute_map = {
        'type': 'type',
        'id': 'id',
        'amount': 'amount',
        'currency_rate': 'currencyRate'
    }

    def __init__(self, type=None, id=None, amount=None, currency_rate=None):  # noqa: E501
        """CodatDataContractsDatasetsBillPaymentLineLink - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._id = None
        self._amount = None
        self._currency_rate = None
        self.discriminator = None
        self.type = type
        if id is not None:
            self.id = id
        if amount is not None:
            self.amount = amount
        if currency_rate is not None:
            self.currency_rate = currency_rate

    @property
    def type(self):
        """Gets the type of this CodatDataContractsDatasetsBillPaymentLineLink.  # noqa: E501


        :return: The type of this CodatDataContractsDatasetsBillPaymentLineLink.  # noqa: E501
        :rtype: CodatDataContractsDatasetsBillPaymentLinkType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CodatDataContractsDatasetsBillPaymentLineLink.


        :param type: The type of this CodatDataContractsDatasetsBillPaymentLineLink.  # noqa: E501
        :type: CodatDataContractsDatasetsBillPaymentLinkType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def id(self):
        """Gets the id of this CodatDataContractsDatasetsBillPaymentLineLink.  # noqa: E501


        :return: The id of this CodatDataContractsDatasetsBillPaymentLineLink.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CodatDataContractsDatasetsBillPaymentLineLink.


        :param id: The id of this CodatDataContractsDatasetsBillPaymentLineLink.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def amount(self):
        """Gets the amount of this CodatDataContractsDatasetsBillPaymentLineLink.  # noqa: E501


        :return: The amount of this CodatDataContractsDatasetsBillPaymentLineLink.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CodatDataContractsDatasetsBillPaymentLineLink.


        :param amount: The amount of this CodatDataContractsDatasetsBillPaymentLineLink.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def currency_rate(self):
        """Gets the currency_rate of this CodatDataContractsDatasetsBillPaymentLineLink.  # noqa: E501


        :return: The currency_rate of this CodatDataContractsDatasetsBillPaymentLineLink.  # noqa: E501
        :rtype: float
        """
        return self._currency_rate

    @currency_rate.setter
    def currency_rate(self, currency_rate):
        """Sets the currency_rate of this CodatDataContractsDatasetsBillPaymentLineLink.


        :param currency_rate: The currency_rate of this CodatDataContractsDatasetsBillPaymentLineLink.  # noqa: E501
        :type: float
        """

        self._currency_rate = currency_rate

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
        if issubclass(CodatDataContractsDatasetsBillPaymentLineLink, dict):
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
        if not isinstance(other, CodatDataContractsDatasetsBillPaymentLineLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

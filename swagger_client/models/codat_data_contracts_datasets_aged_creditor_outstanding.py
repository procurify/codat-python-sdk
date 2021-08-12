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

class CodatDataContractsDatasetsAgedCreditorOutstanding(object):
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
        'supplier_id': 'str',
        'supplier_name': 'str',
        'aged_currency_outstanding': 'list[CodatDataContractsDatasetsAgedCurrencyOutstanding]'
    }

    attribute_map = {
        'supplier_id': 'supplierId',
        'supplier_name': 'supplierName',
        'aged_currency_outstanding': 'agedCurrencyOutstanding'
    }

    def __init__(self, supplier_id=None, supplier_name=None, aged_currency_outstanding=None):  # noqa: E501
        """CodatDataContractsDatasetsAgedCreditorOutstanding - a model defined in Swagger"""  # noqa: E501
        self._supplier_id = None
        self._supplier_name = None
        self._aged_currency_outstanding = None
        self.discriminator = None
        if supplier_id is not None:
            self.supplier_id = supplier_id
        if supplier_name is not None:
            self.supplier_name = supplier_name
        if aged_currency_outstanding is not None:
            self.aged_currency_outstanding = aged_currency_outstanding

    @property
    def supplier_id(self):
        """Gets the supplier_id of this CodatDataContractsDatasetsAgedCreditorOutstanding.  # noqa: E501


        :return: The supplier_id of this CodatDataContractsDatasetsAgedCreditorOutstanding.  # noqa: E501
        :rtype: str
        """
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, supplier_id):
        """Sets the supplier_id of this CodatDataContractsDatasetsAgedCreditorOutstanding.


        :param supplier_id: The supplier_id of this CodatDataContractsDatasetsAgedCreditorOutstanding.  # noqa: E501
        :type: str
        """

        self._supplier_id = supplier_id

    @property
    def supplier_name(self):
        """Gets the supplier_name of this CodatDataContractsDatasetsAgedCreditorOutstanding.  # noqa: E501


        :return: The supplier_name of this CodatDataContractsDatasetsAgedCreditorOutstanding.  # noqa: E501
        :rtype: str
        """
        return self._supplier_name

    @supplier_name.setter
    def supplier_name(self, supplier_name):
        """Sets the supplier_name of this CodatDataContractsDatasetsAgedCreditorOutstanding.


        :param supplier_name: The supplier_name of this CodatDataContractsDatasetsAgedCreditorOutstanding.  # noqa: E501
        :type: str
        """

        self._supplier_name = supplier_name

    @property
    def aged_currency_outstanding(self):
        """Gets the aged_currency_outstanding of this CodatDataContractsDatasetsAgedCreditorOutstanding.  # noqa: E501


        :return: The aged_currency_outstanding of this CodatDataContractsDatasetsAgedCreditorOutstanding.  # noqa: E501
        :rtype: list[CodatDataContractsDatasetsAgedCurrencyOutstanding]
        """
        return self._aged_currency_outstanding

    @aged_currency_outstanding.setter
    def aged_currency_outstanding(self, aged_currency_outstanding):
        """Sets the aged_currency_outstanding of this CodatDataContractsDatasetsAgedCreditorOutstanding.


        :param aged_currency_outstanding: The aged_currency_outstanding of this CodatDataContractsDatasetsAgedCreditorOutstanding.  # noqa: E501
        :type: list[CodatDataContractsDatasetsAgedCurrencyOutstanding]
        """

        self._aged_currency_outstanding = aged_currency_outstanding

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
        if issubclass(CodatDataContractsDatasetsAgedCreditorOutstanding, dict):
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
        if not isinstance(other, CodatDataContractsDatasetsAgedCreditorOutstanding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

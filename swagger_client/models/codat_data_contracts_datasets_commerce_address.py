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

class CodatDataContractsDatasetsCommerceAddress(object):
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
        'type': 'CodatDataContractsDatasetsCommerceAddressType',
        'line1': 'str',
        'line2': 'str',
        'city': 'str',
        'region': 'str',
        'country': 'str',
        'postal_code': 'str'
    }

    attribute_map = {
        'type': 'type',
        'line1': 'line1',
        'line2': 'line2',
        'city': 'city',
        'region': 'region',
        'country': 'country',
        'postal_code': 'postalCode'
    }

    def __init__(self, type=None, line1=None, line2=None, city=None, region=None, country=None, postal_code=None):  # noqa: E501
        """CodatDataContractsDatasetsCommerceAddress - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._line1 = None
        self._line2 = None
        self._city = None
        self._region = None
        self._country = None
        self._postal_code = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if line1 is not None:
            self.line1 = line1
        if line2 is not None:
            self.line2 = line2
        if city is not None:
            self.city = city
        if region is not None:
            self.region = region
        if country is not None:
            self.country = country
        if postal_code is not None:
            self.postal_code = postal_code

    @property
    def type(self):
        """Gets the type of this CodatDataContractsDatasetsCommerceAddress.  # noqa: E501


        :return: The type of this CodatDataContractsDatasetsCommerceAddress.  # noqa: E501
        :rtype: CodatDataContractsDatasetsCommerceAddressType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CodatDataContractsDatasetsCommerceAddress.


        :param type: The type of this CodatDataContractsDatasetsCommerceAddress.  # noqa: E501
        :type: CodatDataContractsDatasetsCommerceAddressType
        """

        self._type = type

    @property
    def line1(self):
        """Gets the line1 of this CodatDataContractsDatasetsCommerceAddress.  # noqa: E501


        :return: The line1 of this CodatDataContractsDatasetsCommerceAddress.  # noqa: E501
        :rtype: str
        """
        return self._line1

    @line1.setter
    def line1(self, line1):
        """Sets the line1 of this CodatDataContractsDatasetsCommerceAddress.


        :param line1: The line1 of this CodatDataContractsDatasetsCommerceAddress.  # noqa: E501
        :type: str
        """

        self._line1 = line1

    @property
    def line2(self):
        """Gets the line2 of this CodatDataContractsDatasetsCommerceAddress.  # noqa: E501


        :return: The line2 of this CodatDataContractsDatasetsCommerceAddress.  # noqa: E501
        :rtype: str
        """
        return self._line2

    @line2.setter
    def line2(self, line2):
        """Sets the line2 of this CodatDataContractsDatasetsCommerceAddress.


        :param line2: The line2 of this CodatDataContractsDatasetsCommerceAddress.  # noqa: E501
        :type: str
        """

        self._line2 = line2

    @property
    def city(self):
        """Gets the city of this CodatDataContractsDatasetsCommerceAddress.  # noqa: E501


        :return: The city of this CodatDataContractsDatasetsCommerceAddress.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this CodatDataContractsDatasetsCommerceAddress.


        :param city: The city of this CodatDataContractsDatasetsCommerceAddress.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def region(self):
        """Gets the region of this CodatDataContractsDatasetsCommerceAddress.  # noqa: E501


        :return: The region of this CodatDataContractsDatasetsCommerceAddress.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this CodatDataContractsDatasetsCommerceAddress.


        :param region: The region of this CodatDataContractsDatasetsCommerceAddress.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def country(self):
        """Gets the country of this CodatDataContractsDatasetsCommerceAddress.  # noqa: E501


        :return: The country of this CodatDataContractsDatasetsCommerceAddress.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this CodatDataContractsDatasetsCommerceAddress.


        :param country: The country of this CodatDataContractsDatasetsCommerceAddress.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def postal_code(self):
        """Gets the postal_code of this CodatDataContractsDatasetsCommerceAddress.  # noqa: E501


        :return: The postal_code of this CodatDataContractsDatasetsCommerceAddress.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this CodatDataContractsDatasetsCommerceAddress.


        :param postal_code: The postal_code of this CodatDataContractsDatasetsCommerceAddress.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

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
        if issubclass(CodatDataContractsDatasetsCommerceAddress, dict):
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
        if not isinstance(other, CodatDataContractsDatasetsCommerceAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

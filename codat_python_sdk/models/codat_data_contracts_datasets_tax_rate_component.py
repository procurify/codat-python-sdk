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

class CodatDataContractsDatasetsTaxRateComponent(object):
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
        'name': 'str',
        'rate': 'float',
        'is_compound': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'rate': 'rate',
        'is_compound': 'isCompound'
    }

    def __init__(self, name=None, rate=None, is_compound=None):  # noqa: E501
        """CodatDataContractsDatasetsTaxRateComponent - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._rate = None
        self._is_compound = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if rate is not None:
            self.rate = rate
        self.is_compound = is_compound

    @property
    def name(self):
        """Gets the name of this CodatDataContractsDatasetsTaxRateComponent.  # noqa: E501


        :return: The name of this CodatDataContractsDatasetsTaxRateComponent.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CodatDataContractsDatasetsTaxRateComponent.


        :param name: The name of this CodatDataContractsDatasetsTaxRateComponent.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def rate(self):
        """Gets the rate of this CodatDataContractsDatasetsTaxRateComponent.  # noqa: E501


        :return: The rate of this CodatDataContractsDatasetsTaxRateComponent.  # noqa: E501
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this CodatDataContractsDatasetsTaxRateComponent.


        :param rate: The rate of this CodatDataContractsDatasetsTaxRateComponent.  # noqa: E501
        :type: float
        """

        self._rate = rate

    @property
    def is_compound(self):
        """Gets the is_compound of this CodatDataContractsDatasetsTaxRateComponent.  # noqa: E501


        :return: The is_compound of this CodatDataContractsDatasetsTaxRateComponent.  # noqa: E501
        :rtype: bool
        """
        return self._is_compound

    @is_compound.setter
    def is_compound(self, is_compound):
        """Sets the is_compound of this CodatDataContractsDatasetsTaxRateComponent.


        :param is_compound: The is_compound of this CodatDataContractsDatasetsTaxRateComponent.  # noqa: E501
        :type: bool
        """
        if is_compound is None:
            raise ValueError("Invalid value for `is_compound`, must not be `None`")  # noqa: E501

        self._is_compound = is_compound

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
        if issubclass(CodatDataContractsDatasetsTaxRateComponent, dict):
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
        if not isinstance(other, CodatDataContractsDatasetsTaxRateComponent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
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

class CodatClientsApiClientContractDatatypeFeatures(object):
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
        'datatype': 'str',
        'supported_features': 'list[CodatClientsApiClientContractSupportedFeatureState]'
    }

    attribute_map = {
        'datatype': 'datatype',
        'supported_features': 'supportedFeatures'
    }

    def __init__(self, datatype=None, supported_features=None):  # noqa: E501
        """CodatClientsApiClientContractDatatypeFeatures - a model defined in Swagger"""  # noqa: E501
        self._datatype = None
        self._supported_features = None
        self.discriminator = None
        if datatype is not None:
            self.datatype = datatype
        if supported_features is not None:
            self.supported_features = supported_features

    @property
    def datatype(self):
        """Gets the datatype of this CodatClientsApiClientContractDatatypeFeatures.  # noqa: E501


        :return: The datatype of this CodatClientsApiClientContractDatatypeFeatures.  # noqa: E501
        :rtype: str
        """
        return self._datatype

    @datatype.setter
    def datatype(self, datatype):
        """Sets the datatype of this CodatClientsApiClientContractDatatypeFeatures.


        :param datatype: The datatype of this CodatClientsApiClientContractDatatypeFeatures.  # noqa: E501
        :type: str
        """

        self._datatype = datatype

    @property
    def supported_features(self):
        """Gets the supported_features of this CodatClientsApiClientContractDatatypeFeatures.  # noqa: E501


        :return: The supported_features of this CodatClientsApiClientContractDatatypeFeatures.  # noqa: E501
        :rtype: list[CodatClientsApiClientContractSupportedFeatureState]
        """
        return self._supported_features

    @supported_features.setter
    def supported_features(self, supported_features):
        """Sets the supported_features of this CodatClientsApiClientContractDatatypeFeatures.


        :param supported_features: The supported_features of this CodatClientsApiClientContractDatatypeFeatures.  # noqa: E501
        :type: list[CodatClientsApiClientContractSupportedFeatureState]
        """

        self._supported_features = supported_features

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
        if issubclass(CodatClientsApiClientContractDatatypeFeatures, dict):
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
        if not isinstance(other, CodatClientsApiClientContractDatatypeFeatures):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
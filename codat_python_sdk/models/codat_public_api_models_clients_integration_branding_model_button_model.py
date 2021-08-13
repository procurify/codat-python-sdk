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

class CodatPublicApiModelsClientsIntegrationBrandingModelButtonModel(object):
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
        'default': 'CodatPublicApiModelsClientsIntegrationBrandingModelDefaultModel',
        'hover': 'CodatPublicApiModelsClientsIntegrationBrandingModelHoverModel'
    }

    attribute_map = {
        'default': 'default',
        'hover': 'hover'
    }

    def __init__(self, default=None, hover=None):  # noqa: E501
        """CodatPublicApiModelsClientsIntegrationBrandingModelButtonModel - a model defined in Swagger"""  # noqa: E501
        self._default = None
        self._hover = None
        self.discriminator = None
        if default is not None:
            self.default = default
        if hover is not None:
            self.hover = hover

    @property
    def default(self):
        """Gets the default of this CodatPublicApiModelsClientsIntegrationBrandingModelButtonModel.  # noqa: E501


        :return: The default of this CodatPublicApiModelsClientsIntegrationBrandingModelButtonModel.  # noqa: E501
        :rtype: CodatPublicApiModelsClientsIntegrationBrandingModelDefaultModel
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this CodatPublicApiModelsClientsIntegrationBrandingModelButtonModel.


        :param default: The default of this CodatPublicApiModelsClientsIntegrationBrandingModelButtonModel.  # noqa: E501
        :type: CodatPublicApiModelsClientsIntegrationBrandingModelDefaultModel
        """

        self._default = default

    @property
    def hover(self):
        """Gets the hover of this CodatPublicApiModelsClientsIntegrationBrandingModelButtonModel.  # noqa: E501


        :return: The hover of this CodatPublicApiModelsClientsIntegrationBrandingModelButtonModel.  # noqa: E501
        :rtype: CodatPublicApiModelsClientsIntegrationBrandingModelHoverModel
        """
        return self._hover

    @hover.setter
    def hover(self, hover):
        """Sets the hover of this CodatPublicApiModelsClientsIntegrationBrandingModelButtonModel.


        :param hover: The hover of this CodatPublicApiModelsClientsIntegrationBrandingModelButtonModel.  # noqa: E501
        :type: CodatPublicApiModelsClientsIntegrationBrandingModelHoverModel
        """

        self._hover = hover

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
        if issubclass(CodatPublicApiModelsClientsIntegrationBrandingModelButtonModel, dict):
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
        if not isinstance(other, CodatPublicApiModelsClientsIntegrationBrandingModelButtonModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
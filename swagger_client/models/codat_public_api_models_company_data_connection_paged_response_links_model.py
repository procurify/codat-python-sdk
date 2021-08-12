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

class CodatPublicApiModelsCompanyDataConnectionPagedResponseLinksModel(object):
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
        '_self': 'CodatPublicApiModelsCompanyDataConnectionPagedResponseHrefModel',
        'current': 'CodatPublicApiModelsCompanyDataConnectionPagedResponseHrefModel',
        'next': 'CodatPublicApiModelsCompanyDataConnectionPagedResponseHrefModel',
        'previous': 'CodatPublicApiModelsCompanyDataConnectionPagedResponseHrefModel'
    }

    attribute_map = {
        '_self': 'self',
        'current': 'current',
        'next': 'next',
        'previous': 'previous'
    }

    def __init__(self, _self=None, current=None, next=None, previous=None):  # noqa: E501
        """CodatPublicApiModelsCompanyDataConnectionPagedResponseLinksModel - a model defined in Swagger"""  # noqa: E501
        self.__self = None
        self._current = None
        self._next = None
        self._previous = None
        self.discriminator = None
        if _self is not None:
            self._self = _self
        if current is not None:
            self.current = current
        if next is not None:
            self.next = next
        if previous is not None:
            self.previous = previous

    @property
    def _self(self):
        """Gets the _self of this CodatPublicApiModelsCompanyDataConnectionPagedResponseLinksModel.  # noqa: E501


        :return: The _self of this CodatPublicApiModelsCompanyDataConnectionPagedResponseLinksModel.  # noqa: E501
        :rtype: CodatPublicApiModelsCompanyDataConnectionPagedResponseHrefModel
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this CodatPublicApiModelsCompanyDataConnectionPagedResponseLinksModel.


        :param _self: The _self of this CodatPublicApiModelsCompanyDataConnectionPagedResponseLinksModel.  # noqa: E501
        :type: CodatPublicApiModelsCompanyDataConnectionPagedResponseHrefModel
        """

        self.__self = _self

    @property
    def current(self):
        """Gets the current of this CodatPublicApiModelsCompanyDataConnectionPagedResponseLinksModel.  # noqa: E501


        :return: The current of this CodatPublicApiModelsCompanyDataConnectionPagedResponseLinksModel.  # noqa: E501
        :rtype: CodatPublicApiModelsCompanyDataConnectionPagedResponseHrefModel
        """
        return self._current

    @current.setter
    def current(self, current):
        """Sets the current of this CodatPublicApiModelsCompanyDataConnectionPagedResponseLinksModel.


        :param current: The current of this CodatPublicApiModelsCompanyDataConnectionPagedResponseLinksModel.  # noqa: E501
        :type: CodatPublicApiModelsCompanyDataConnectionPagedResponseHrefModel
        """

        self._current = current

    @property
    def next(self):
        """Gets the next of this CodatPublicApiModelsCompanyDataConnectionPagedResponseLinksModel.  # noqa: E501


        :return: The next of this CodatPublicApiModelsCompanyDataConnectionPagedResponseLinksModel.  # noqa: E501
        :rtype: CodatPublicApiModelsCompanyDataConnectionPagedResponseHrefModel
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this CodatPublicApiModelsCompanyDataConnectionPagedResponseLinksModel.


        :param next: The next of this CodatPublicApiModelsCompanyDataConnectionPagedResponseLinksModel.  # noqa: E501
        :type: CodatPublicApiModelsCompanyDataConnectionPagedResponseHrefModel
        """

        self._next = next

    @property
    def previous(self):
        """Gets the previous of this CodatPublicApiModelsCompanyDataConnectionPagedResponseLinksModel.  # noqa: E501


        :return: The previous of this CodatPublicApiModelsCompanyDataConnectionPagedResponseLinksModel.  # noqa: E501
        :rtype: CodatPublicApiModelsCompanyDataConnectionPagedResponseHrefModel
        """
        return self._previous

    @previous.setter
    def previous(self, previous):
        """Sets the previous of this CodatPublicApiModelsCompanyDataConnectionPagedResponseLinksModel.


        :param previous: The previous of this CodatPublicApiModelsCompanyDataConnectionPagedResponseLinksModel.  # noqa: E501
        :type: CodatPublicApiModelsCompanyDataConnectionPagedResponseHrefModel
        """

        self._previous = previous

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
        if issubclass(CodatPublicApiModelsCompanyDataConnectionPagedResponseLinksModel, dict):
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
        if not isinstance(other, CodatPublicApiModelsCompanyDataConnectionPagedResponseLinksModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

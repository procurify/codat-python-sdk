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

class CodatPublicApiModelsCompanyCompanyEventStream(object):
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
        'company_id': 'str',
        '_from': 'datetime',
        'to': 'datetime',
        'data': 'list[CodatPublicApiModelsCompanyCompanyEventStreamItem]'
    }

    attribute_map = {
        'company_id': 'companyId',
        '_from': 'from',
        'to': 'to',
        'data': 'data'
    }

    def __init__(self, company_id=None, _from=None, to=None, data=None):  # noqa: E501
        """CodatPublicApiModelsCompanyCompanyEventStream - a model defined in Swagger"""  # noqa: E501
        self._company_id = None
        self.__from = None
        self._to = None
        self._data = None
        self.discriminator = None
        self.company_id = company_id
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        self.data = data

    @property
    def company_id(self):
        """Gets the company_id of this CodatPublicApiModelsCompanyCompanyEventStream.  # noqa: E501


        :return: The company_id of this CodatPublicApiModelsCompanyCompanyEventStream.  # noqa: E501
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this CodatPublicApiModelsCompanyCompanyEventStream.


        :param company_id: The company_id of this CodatPublicApiModelsCompanyCompanyEventStream.  # noqa: E501
        :type: str
        """
        if company_id is None:
            raise ValueError("Invalid value for `company_id`, must not be `None`")  # noqa: E501

        self._company_id = company_id

    @property
    def _from(self):
        """Gets the _from of this CodatPublicApiModelsCompanyCompanyEventStream.  # noqa: E501


        :return: The _from of this CodatPublicApiModelsCompanyCompanyEventStream.  # noqa: E501
        :rtype: datetime
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this CodatPublicApiModelsCompanyCompanyEventStream.


        :param _from: The _from of this CodatPublicApiModelsCompanyCompanyEventStream.  # noqa: E501
        :type: datetime
        """

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this CodatPublicApiModelsCompanyCompanyEventStream.  # noqa: E501


        :return: The to of this CodatPublicApiModelsCompanyCompanyEventStream.  # noqa: E501
        :rtype: datetime
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this CodatPublicApiModelsCompanyCompanyEventStream.


        :param to: The to of this CodatPublicApiModelsCompanyCompanyEventStream.  # noqa: E501
        :type: datetime
        """

        self._to = to

    @property
    def data(self):
        """Gets the data of this CodatPublicApiModelsCompanyCompanyEventStream.  # noqa: E501


        :return: The data of this CodatPublicApiModelsCompanyCompanyEventStream.  # noqa: E501
        :rtype: list[CodatPublicApiModelsCompanyCompanyEventStreamItem]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CodatPublicApiModelsCompanyCompanyEventStream.


        :param data: The data of this CodatPublicApiModelsCompanyCompanyEventStream.  # noqa: E501
        :type: list[CodatPublicApiModelsCompanyCompanyEventStreamItem]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

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
        if issubclass(CodatPublicApiModelsCompanyCompanyEventStream, dict):
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
        if not isinstance(other, CodatPublicApiModelsCompanyCompanyEventStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
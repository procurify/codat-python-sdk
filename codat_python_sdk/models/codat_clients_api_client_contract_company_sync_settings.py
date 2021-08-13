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

class CodatClientsApiClientContractCompanySyncSettings(object):
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
        'settings': 'list[CodatClientsApiClientContractSyncSetting]',
        'overrides_defaults': 'bool'
    }

    attribute_map = {
        'company_id': 'companyId',
        'settings': 'settings',
        'overrides_defaults': 'overridesDefaults'
    }

    def __init__(self, company_id=None, settings=None, overrides_defaults=None):  # noqa: E501
        """CodatClientsApiClientContractCompanySyncSettings - a model defined in Swagger"""  # noqa: E501
        self._company_id = None
        self._settings = None
        self._overrides_defaults = None
        self.discriminator = None
        if company_id is not None:
            self.company_id = company_id
        if settings is not None:
            self.settings = settings
        if overrides_defaults is not None:
            self.overrides_defaults = overrides_defaults

    @property
    def company_id(self):
        """Gets the company_id of this CodatClientsApiClientContractCompanySyncSettings.  # noqa: E501


        :return: The company_id of this CodatClientsApiClientContractCompanySyncSettings.  # noqa: E501
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this CodatClientsApiClientContractCompanySyncSettings.


        :param company_id: The company_id of this CodatClientsApiClientContractCompanySyncSettings.  # noqa: E501
        :type: str
        """

        self._company_id = company_id

    @property
    def settings(self):
        """Gets the settings of this CodatClientsApiClientContractCompanySyncSettings.  # noqa: E501


        :return: The settings of this CodatClientsApiClientContractCompanySyncSettings.  # noqa: E501
        :rtype: list[CodatClientsApiClientContractSyncSetting]
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this CodatClientsApiClientContractCompanySyncSettings.


        :param settings: The settings of this CodatClientsApiClientContractCompanySyncSettings.  # noqa: E501
        :type: list[CodatClientsApiClientContractSyncSetting]
        """

        self._settings = settings

    @property
    def overrides_defaults(self):
        """Gets the overrides_defaults of this CodatClientsApiClientContractCompanySyncSettings.  # noqa: E501


        :return: The overrides_defaults of this CodatClientsApiClientContractCompanySyncSettings.  # noqa: E501
        :rtype: bool
        """
        return self._overrides_defaults

    @overrides_defaults.setter
    def overrides_defaults(self, overrides_defaults):
        """Sets the overrides_defaults of this CodatClientsApiClientContractCompanySyncSettings.


        :param overrides_defaults: The overrides_defaults of this CodatClientsApiClientContractCompanySyncSettings.  # noqa: E501
        :type: bool
        """

        self._overrides_defaults = overrides_defaults

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
        if issubclass(CodatClientsApiClientContractCompanySyncSettings, dict):
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
        if not isinstance(other, CodatClientsApiClientContractCompanySyncSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

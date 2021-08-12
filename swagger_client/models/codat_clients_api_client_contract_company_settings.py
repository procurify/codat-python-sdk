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

class CodatClientsApiClientContractCompanySettings(object):
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
        'offline_connector_install': 'bool',
        'one_time_sync': 'str'
    }

    attribute_map = {
        'company_id': 'companyId',
        'offline_connector_install': 'offlineConnectorInstall',
        'one_time_sync': 'oneTimeSync'
    }

    def __init__(self, company_id=None, offline_connector_install=None, one_time_sync=None):  # noqa: E501
        """CodatClientsApiClientContractCompanySettings - a model defined in Swagger"""  # noqa: E501
        self._company_id = None
        self._offline_connector_install = None
        self._one_time_sync = None
        self.discriminator = None
        if company_id is not None:
            self.company_id = company_id
        if offline_connector_install is not None:
            self.offline_connector_install = offline_connector_install
        if one_time_sync is not None:
            self.one_time_sync = one_time_sync

    @property
    def company_id(self):
        """Gets the company_id of this CodatClientsApiClientContractCompanySettings.  # noqa: E501


        :return: The company_id of this CodatClientsApiClientContractCompanySettings.  # noqa: E501
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this CodatClientsApiClientContractCompanySettings.


        :param company_id: The company_id of this CodatClientsApiClientContractCompanySettings.  # noqa: E501
        :type: str
        """

        self._company_id = company_id

    @property
    def offline_connector_install(self):
        """Gets the offline_connector_install of this CodatClientsApiClientContractCompanySettings.  # noqa: E501


        :return: The offline_connector_install of this CodatClientsApiClientContractCompanySettings.  # noqa: E501
        :rtype: bool
        """
        return self._offline_connector_install

    @offline_connector_install.setter
    def offline_connector_install(self, offline_connector_install):
        """Sets the offline_connector_install of this CodatClientsApiClientContractCompanySettings.


        :param offline_connector_install: The offline_connector_install of this CodatClientsApiClientContractCompanySettings.  # noqa: E501
        :type: bool
        """

        self._offline_connector_install = offline_connector_install

    @property
    def one_time_sync(self):
        """Gets the one_time_sync of this CodatClientsApiClientContractCompanySettings.  # noqa: E501


        :return: The one_time_sync of this CodatClientsApiClientContractCompanySettings.  # noqa: E501
        :rtype: str
        """
        return self._one_time_sync

    @one_time_sync.setter
    def one_time_sync(self, one_time_sync):
        """Sets the one_time_sync of this CodatClientsApiClientContractCompanySettings.


        :param one_time_sync: The one_time_sync of this CodatClientsApiClientContractCompanySettings.  # noqa: E501
        :type: str
        """

        self._one_time_sync = one_time_sync

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
        if issubclass(CodatClientsApiClientContractCompanySettings, dict):
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
        if not isinstance(other, CodatClientsApiClientContractCompanySettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

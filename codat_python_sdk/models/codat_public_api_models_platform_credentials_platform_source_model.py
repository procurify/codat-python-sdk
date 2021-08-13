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

class CodatPublicApiModelsPlatformCredentialsPlatformSourceModel(object):
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
        'key': 'str',
        'logo_url': 'str',
        'name': 'str',
        'enabled': 'bool',
        'source_id': 'str',
        'integration_id': 'str',
        'source_type': 'CodatClientsApiClientContractSourceType',
        'is_offline_connector': 'bool',
        'is_beta': 'bool',
        'supported_environments': 'CodatClientsApiClientContractIntegrationSupportedEnvironments',
        'datatype_features': 'list[CodatClientsApiClientContractDatatypeFeatures]'
    }

    attribute_map = {
        'key': 'key',
        'logo_url': 'logoUrl',
        'name': 'name',
        'enabled': 'enabled',
        'source_id': 'sourceId',
        'integration_id': 'integrationId',
        'source_type': 'sourceType',
        'is_offline_connector': 'isOfflineConnector',
        'is_beta': 'isBeta',
        'supported_environments': 'supportedEnvironments',
        'datatype_features': 'datatypeFeatures'
    }

    def __init__(self, key=None, logo_url=None, name=None, enabled=None, source_id=None, integration_id=None, source_type=None, is_offline_connector=None, is_beta=None, supported_environments=None, datatype_features=None):  # noqa: E501
        """CodatPublicApiModelsPlatformCredentialsPlatformSourceModel - a model defined in Swagger"""  # noqa: E501
        self._key = None
        self._logo_url = None
        self._name = None
        self._enabled = None
        self._source_id = None
        self._integration_id = None
        self._source_type = None
        self._is_offline_connector = None
        self._is_beta = None
        self._supported_environments = None
        self._datatype_features = None
        self.discriminator = None
        if key is not None:
            self.key = key
        if logo_url is not None:
            self.logo_url = logo_url
        if name is not None:
            self.name = name
        if enabled is not None:
            self.enabled = enabled
        if source_id is not None:
            self.source_id = source_id
        if integration_id is not None:
            self.integration_id = integration_id
        if source_type is not None:
            self.source_type = source_type
        if is_offline_connector is not None:
            self.is_offline_connector = is_offline_connector
        if is_beta is not None:
            self.is_beta = is_beta
        if supported_environments is not None:
            self.supported_environments = supported_environments
        if datatype_features is not None:
            self.datatype_features = datatype_features

    @property
    def key(self):
        """Gets the key of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.  # noqa: E501


        :return: The key of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.


        :param key: The key of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def logo_url(self):
        """Gets the logo_url of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.  # noqa: E501


        :return: The logo_url of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.  # noqa: E501
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """Sets the logo_url of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.


        :param logo_url: The logo_url of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.  # noqa: E501
        :type: str
        """

        self._logo_url = logo_url

    @property
    def name(self):
        """Gets the name of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.  # noqa: E501


        :return: The name of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.


        :param name: The name of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def enabled(self):
        """Gets the enabled of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.  # noqa: E501


        :return: The enabled of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.


        :param enabled: The enabled of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def source_id(self):
        """Gets the source_id of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.  # noqa: E501


        :return: The source_id of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.  # noqa: E501
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.


        :param source_id: The source_id of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.  # noqa: E501
        :type: str
        """

        self._source_id = source_id

    @property
    def integration_id(self):
        """Gets the integration_id of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.  # noqa: E501


        :return: The integration_id of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.  # noqa: E501
        :rtype: str
        """
        return self._integration_id

    @integration_id.setter
    def integration_id(self, integration_id):
        """Sets the integration_id of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.


        :param integration_id: The integration_id of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.  # noqa: E501
        :type: str
        """

        self._integration_id = integration_id

    @property
    def source_type(self):
        """Gets the source_type of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.  # noqa: E501


        :return: The source_type of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.  # noqa: E501
        :rtype: CodatClientsApiClientContractSourceType
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.


        :param source_type: The source_type of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.  # noqa: E501
        :type: CodatClientsApiClientContractSourceType
        """

        self._source_type = source_type

    @property
    def is_offline_connector(self):
        """Gets the is_offline_connector of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.  # noqa: E501


        :return: The is_offline_connector of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_offline_connector

    @is_offline_connector.setter
    def is_offline_connector(self, is_offline_connector):
        """Sets the is_offline_connector of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.


        :param is_offline_connector: The is_offline_connector of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.  # noqa: E501
        :type: bool
        """

        self._is_offline_connector = is_offline_connector

    @property
    def is_beta(self):
        """Gets the is_beta of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.  # noqa: E501


        :return: The is_beta of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_beta

    @is_beta.setter
    def is_beta(self, is_beta):
        """Sets the is_beta of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.


        :param is_beta: The is_beta of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.  # noqa: E501
        :type: bool
        """

        self._is_beta = is_beta

    @property
    def supported_environments(self):
        """Gets the supported_environments of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.  # noqa: E501


        :return: The supported_environments of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.  # noqa: E501
        :rtype: CodatClientsApiClientContractIntegrationSupportedEnvironments
        """
        return self._supported_environments

    @supported_environments.setter
    def supported_environments(self, supported_environments):
        """Sets the supported_environments of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.


        :param supported_environments: The supported_environments of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.  # noqa: E501
        :type: CodatClientsApiClientContractIntegrationSupportedEnvironments
        """

        self._supported_environments = supported_environments

    @property
    def datatype_features(self):
        """Gets the datatype_features of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.  # noqa: E501


        :return: The datatype_features of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.  # noqa: E501
        :rtype: list[CodatClientsApiClientContractDatatypeFeatures]
        """
        return self._datatype_features

    @datatype_features.setter
    def datatype_features(self, datatype_features):
        """Sets the datatype_features of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.


        :param datatype_features: The datatype_features of this CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.  # noqa: E501
        :type: list[CodatClientsApiClientContractDatatypeFeatures]
        """

        self._datatype_features = datatype_features

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
        if issubclass(CodatPublicApiModelsPlatformCredentialsPlatformSourceModel, dict):
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
        if not isinstance(other, CodatPublicApiModelsPlatformCredentialsPlatformSourceModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
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

class CodatClientsApiClientContractDataConnection(object):
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
        'id': 'str',
        'company_id': 'str',
        'client_id': 'str',
        'status': 'str',
        'supported_data_path': 'CodatClientsApiClientContractSupportedDataPath',
        'redirect_url': 'str',
        'created_on_utc': 'datetime',
        'last_sync': 'datetime',
        'delete_requested': 'bool',
        'deleted': 'bool',
        'deleted_utc': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'company_id': 'companyId',
        'client_id': 'clientId',
        'status': 'status',
        'supported_data_path': 'supportedDataPath',
        'redirect_url': 'redirectUrl',
        'created_on_utc': 'createdOnUtc',
        'last_sync': 'lastSync',
        'delete_requested': 'deleteRequested',
        'deleted': 'deleted',
        'deleted_utc': 'deletedUtc'
    }

    def __init__(self, id=None, company_id=None, client_id=None, status=None, supported_data_path=None, redirect_url=None, created_on_utc=None, last_sync=None, delete_requested=None, deleted=None, deleted_utc=None):  # noqa: E501
        """CodatClientsApiClientContractDataConnection - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._company_id = None
        self._client_id = None
        self._status = None
        self._supported_data_path = None
        self._redirect_url = None
        self._created_on_utc = None
        self._last_sync = None
        self._delete_requested = None
        self._deleted = None
        self._deleted_utc = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if company_id is not None:
            self.company_id = company_id
        if client_id is not None:
            self.client_id = client_id
        if status is not None:
            self.status = status
        if supported_data_path is not None:
            self.supported_data_path = supported_data_path
        if redirect_url is not None:
            self.redirect_url = redirect_url
        if created_on_utc is not None:
            self.created_on_utc = created_on_utc
        if last_sync is not None:
            self.last_sync = last_sync
        if delete_requested is not None:
            self.delete_requested = delete_requested
        if deleted is not None:
            self.deleted = deleted
        if deleted_utc is not None:
            self.deleted_utc = deleted_utc

    @property
    def id(self):
        """Gets the id of this CodatClientsApiClientContractDataConnection.  # noqa: E501


        :return: The id of this CodatClientsApiClientContractDataConnection.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CodatClientsApiClientContractDataConnection.


        :param id: The id of this CodatClientsApiClientContractDataConnection.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def company_id(self):
        """Gets the company_id of this CodatClientsApiClientContractDataConnection.  # noqa: E501


        :return: The company_id of this CodatClientsApiClientContractDataConnection.  # noqa: E501
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this CodatClientsApiClientContractDataConnection.


        :param company_id: The company_id of this CodatClientsApiClientContractDataConnection.  # noqa: E501
        :type: str
        """

        self._company_id = company_id

    @property
    def client_id(self):
        """Gets the client_id of this CodatClientsApiClientContractDataConnection.  # noqa: E501


        :return: The client_id of this CodatClientsApiClientContractDataConnection.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this CodatClientsApiClientContractDataConnection.


        :param client_id: The client_id of this CodatClientsApiClientContractDataConnection.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def status(self):
        """Gets the status of this CodatClientsApiClientContractDataConnection.  # noqa: E501


        :return: The status of this CodatClientsApiClientContractDataConnection.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CodatClientsApiClientContractDataConnection.


        :param status: The status of this CodatClientsApiClientContractDataConnection.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def supported_data_path(self):
        """Gets the supported_data_path of this CodatClientsApiClientContractDataConnection.  # noqa: E501


        :return: The supported_data_path of this CodatClientsApiClientContractDataConnection.  # noqa: E501
        :rtype: CodatClientsApiClientContractSupportedDataPath
        """
        return self._supported_data_path

    @supported_data_path.setter
    def supported_data_path(self, supported_data_path):
        """Sets the supported_data_path of this CodatClientsApiClientContractDataConnection.


        :param supported_data_path: The supported_data_path of this CodatClientsApiClientContractDataConnection.  # noqa: E501
        :type: CodatClientsApiClientContractSupportedDataPath
        """

        self._supported_data_path = supported_data_path

    @property
    def redirect_url(self):
        """Gets the redirect_url of this CodatClientsApiClientContractDataConnection.  # noqa: E501


        :return: The redirect_url of this CodatClientsApiClientContractDataConnection.  # noqa: E501
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """Sets the redirect_url of this CodatClientsApiClientContractDataConnection.


        :param redirect_url: The redirect_url of this CodatClientsApiClientContractDataConnection.  # noqa: E501
        :type: str
        """

        self._redirect_url = redirect_url

    @property
    def created_on_utc(self):
        """Gets the created_on_utc of this CodatClientsApiClientContractDataConnection.  # noqa: E501


        :return: The created_on_utc of this CodatClientsApiClientContractDataConnection.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on_utc

    @created_on_utc.setter
    def created_on_utc(self, created_on_utc):
        """Sets the created_on_utc of this CodatClientsApiClientContractDataConnection.


        :param created_on_utc: The created_on_utc of this CodatClientsApiClientContractDataConnection.  # noqa: E501
        :type: datetime
        """

        self._created_on_utc = created_on_utc

    @property
    def last_sync(self):
        """Gets the last_sync of this CodatClientsApiClientContractDataConnection.  # noqa: E501


        :return: The last_sync of this CodatClientsApiClientContractDataConnection.  # noqa: E501
        :rtype: datetime
        """
        return self._last_sync

    @last_sync.setter
    def last_sync(self, last_sync):
        """Sets the last_sync of this CodatClientsApiClientContractDataConnection.


        :param last_sync: The last_sync of this CodatClientsApiClientContractDataConnection.  # noqa: E501
        :type: datetime
        """

        self._last_sync = last_sync

    @property
    def delete_requested(self):
        """Gets the delete_requested of this CodatClientsApiClientContractDataConnection.  # noqa: E501


        :return: The delete_requested of this CodatClientsApiClientContractDataConnection.  # noqa: E501
        :rtype: bool
        """
        return self._delete_requested

    @delete_requested.setter
    def delete_requested(self, delete_requested):
        """Sets the delete_requested of this CodatClientsApiClientContractDataConnection.


        :param delete_requested: The delete_requested of this CodatClientsApiClientContractDataConnection.  # noqa: E501
        :type: bool
        """

        self._delete_requested = delete_requested

    @property
    def deleted(self):
        """Gets the deleted of this CodatClientsApiClientContractDataConnection.  # noqa: E501


        :return: The deleted of this CodatClientsApiClientContractDataConnection.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this CodatClientsApiClientContractDataConnection.


        :param deleted: The deleted of this CodatClientsApiClientContractDataConnection.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def deleted_utc(self):
        """Gets the deleted_utc of this CodatClientsApiClientContractDataConnection.  # noqa: E501


        :return: The deleted_utc of this CodatClientsApiClientContractDataConnection.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted_utc

    @deleted_utc.setter
    def deleted_utc(self, deleted_utc):
        """Sets the deleted_utc of this CodatClientsApiClientContractDataConnection.


        :param deleted_utc: The deleted_utc of this CodatClientsApiClientContractDataConnection.  # noqa: E501
        :type: datetime
        """

        self._deleted_utc = deleted_utc

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
        if issubclass(CodatClientsApiClientContractDataConnection, dict):
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
        if not isinstance(other, CodatClientsApiClientContractDataConnection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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

class CodatPublicApiModelsCompanyProfileModel(object):
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
        'logo_url': 'str',
        'icon_url': 'str',
        'redirect_url': 'str',
        'white_list_urls': 'list[str]',
        'api_key': 'str',
        'alert_auth_header': 'str',
        'confirm_company_name': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'logo_url': 'logoUrl',
        'icon_url': 'iconUrl',
        'redirect_url': 'redirectUrl',
        'white_list_urls': 'whiteListUrls',
        'api_key': 'apiKey',
        'alert_auth_header': 'alertAuthHeader',
        'confirm_company_name': 'confirmCompanyName'
    }

    def __init__(self, name=None, logo_url=None, icon_url=None, redirect_url=None, white_list_urls=None, api_key=None, alert_auth_header=None, confirm_company_name=None):  # noqa: E501
        """CodatPublicApiModelsCompanyProfileModel - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._logo_url = None
        self._icon_url = None
        self._redirect_url = None
        self._white_list_urls = None
        self._api_key = None
        self._alert_auth_header = None
        self._confirm_company_name = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if logo_url is not None:
            self.logo_url = logo_url
        if icon_url is not None:
            self.icon_url = icon_url
        if redirect_url is not None:
            self.redirect_url = redirect_url
        if white_list_urls is not None:
            self.white_list_urls = white_list_urls
        if api_key is not None:
            self.api_key = api_key
        if alert_auth_header is not None:
            self.alert_auth_header = alert_auth_header
        if confirm_company_name is not None:
            self.confirm_company_name = confirm_company_name

    @property
    def name(self):
        """Gets the name of this CodatPublicApiModelsCompanyProfileModel.  # noqa: E501


        :return: The name of this CodatPublicApiModelsCompanyProfileModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CodatPublicApiModelsCompanyProfileModel.


        :param name: The name of this CodatPublicApiModelsCompanyProfileModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def logo_url(self):
        """Gets the logo_url of this CodatPublicApiModelsCompanyProfileModel.  # noqa: E501


        :return: The logo_url of this CodatPublicApiModelsCompanyProfileModel.  # noqa: E501
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """Sets the logo_url of this CodatPublicApiModelsCompanyProfileModel.


        :param logo_url: The logo_url of this CodatPublicApiModelsCompanyProfileModel.  # noqa: E501
        :type: str
        """

        self._logo_url = logo_url

    @property
    def icon_url(self):
        """Gets the icon_url of this CodatPublicApiModelsCompanyProfileModel.  # noqa: E501


        :return: The icon_url of this CodatPublicApiModelsCompanyProfileModel.  # noqa: E501
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """Sets the icon_url of this CodatPublicApiModelsCompanyProfileModel.


        :param icon_url: The icon_url of this CodatPublicApiModelsCompanyProfileModel.  # noqa: E501
        :type: str
        """

        self._icon_url = icon_url

    @property
    def redirect_url(self):
        """Gets the redirect_url of this CodatPublicApiModelsCompanyProfileModel.  # noqa: E501


        :return: The redirect_url of this CodatPublicApiModelsCompanyProfileModel.  # noqa: E501
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """Sets the redirect_url of this CodatPublicApiModelsCompanyProfileModel.


        :param redirect_url: The redirect_url of this CodatPublicApiModelsCompanyProfileModel.  # noqa: E501
        :type: str
        """

        self._redirect_url = redirect_url

    @property
    def white_list_urls(self):
        """Gets the white_list_urls of this CodatPublicApiModelsCompanyProfileModel.  # noqa: E501


        :return: The white_list_urls of this CodatPublicApiModelsCompanyProfileModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._white_list_urls

    @white_list_urls.setter
    def white_list_urls(self, white_list_urls):
        """Sets the white_list_urls of this CodatPublicApiModelsCompanyProfileModel.


        :param white_list_urls: The white_list_urls of this CodatPublicApiModelsCompanyProfileModel.  # noqa: E501
        :type: list[str]
        """

        self._white_list_urls = white_list_urls

    @property
    def api_key(self):
        """Gets the api_key of this CodatPublicApiModelsCompanyProfileModel.  # noqa: E501


        :return: The api_key of this CodatPublicApiModelsCompanyProfileModel.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this CodatPublicApiModelsCompanyProfileModel.


        :param api_key: The api_key of this CodatPublicApiModelsCompanyProfileModel.  # noqa: E501
        :type: str
        """

        self._api_key = api_key

    @property
    def alert_auth_header(self):
        """Gets the alert_auth_header of this CodatPublicApiModelsCompanyProfileModel.  # noqa: E501


        :return: The alert_auth_header of this CodatPublicApiModelsCompanyProfileModel.  # noqa: E501
        :rtype: str
        """
        return self._alert_auth_header

    @alert_auth_header.setter
    def alert_auth_header(self, alert_auth_header):
        """Sets the alert_auth_header of this CodatPublicApiModelsCompanyProfileModel.


        :param alert_auth_header: The alert_auth_header of this CodatPublicApiModelsCompanyProfileModel.  # noqa: E501
        :type: str
        """

        self._alert_auth_header = alert_auth_header

    @property
    def confirm_company_name(self):
        """Gets the confirm_company_name of this CodatPublicApiModelsCompanyProfileModel.  # noqa: E501


        :return: The confirm_company_name of this CodatPublicApiModelsCompanyProfileModel.  # noqa: E501
        :rtype: bool
        """
        return self._confirm_company_name

    @confirm_company_name.setter
    def confirm_company_name(self, confirm_company_name):
        """Sets the confirm_company_name of this CodatPublicApiModelsCompanyProfileModel.


        :param confirm_company_name: The confirm_company_name of this CodatPublicApiModelsCompanyProfileModel.  # noqa: E501
        :type: bool
        """

        self._confirm_company_name = confirm_company_name

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
        if issubclass(CodatPublicApiModelsCompanyProfileModel, dict):
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
        if not isinstance(other, CodatPublicApiModelsCompanyProfileModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
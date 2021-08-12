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

class CodatPublicApiModelsCompanyCompanyPagedResponseModel(object):
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
        'results': 'list[CodatPublicApiModelsCompanyCompany]',
        'page_number': 'int',
        'page_size': 'int',
        'total_results': 'int',
        'links': 'CodatPublicApiModelsCompanyCompanyPagedResponseLinksModel'
    }

    attribute_map = {
        'results': 'results',
        'page_number': 'pageNumber',
        'page_size': 'pageSize',
        'total_results': 'totalResults',
        'links': '_links'
    }

    def __init__(self, results=None, page_number=None, page_size=None, total_results=None, links=None):  # noqa: E501
        """CodatPublicApiModelsCompanyCompanyPagedResponseModel - a model defined in Swagger"""  # noqa: E501
        self._results = None
        self._page_number = None
        self._page_size = None
        self._total_results = None
        self._links = None
        self.discriminator = None
        if results is not None:
            self.results = results
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if total_results is not None:
            self.total_results = total_results
        if links is not None:
            self.links = links

    @property
    def results(self):
        """Gets the results of this CodatPublicApiModelsCompanyCompanyPagedResponseModel.  # noqa: E501


        :return: The results of this CodatPublicApiModelsCompanyCompanyPagedResponseModel.  # noqa: E501
        :rtype: list[CodatPublicApiModelsCompanyCompany]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this CodatPublicApiModelsCompanyCompanyPagedResponseModel.


        :param results: The results of this CodatPublicApiModelsCompanyCompanyPagedResponseModel.  # noqa: E501
        :type: list[CodatPublicApiModelsCompanyCompany]
        """

        self._results = results

    @property
    def page_number(self):
        """Gets the page_number of this CodatPublicApiModelsCompanyCompanyPagedResponseModel.  # noqa: E501


        :return: The page_number of this CodatPublicApiModelsCompanyCompanyPagedResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this CodatPublicApiModelsCompanyCompanyPagedResponseModel.


        :param page_number: The page_number of this CodatPublicApiModelsCompanyCompanyPagedResponseModel.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this CodatPublicApiModelsCompanyCompanyPagedResponseModel.  # noqa: E501


        :return: The page_size of this CodatPublicApiModelsCompanyCompanyPagedResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this CodatPublicApiModelsCompanyCompanyPagedResponseModel.


        :param page_size: The page_size of this CodatPublicApiModelsCompanyCompanyPagedResponseModel.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def total_results(self):
        """Gets the total_results of this CodatPublicApiModelsCompanyCompanyPagedResponseModel.  # noqa: E501


        :return: The total_results of this CodatPublicApiModelsCompanyCompanyPagedResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._total_results

    @total_results.setter
    def total_results(self, total_results):
        """Sets the total_results of this CodatPublicApiModelsCompanyCompanyPagedResponseModel.


        :param total_results: The total_results of this CodatPublicApiModelsCompanyCompanyPagedResponseModel.  # noqa: E501
        :type: int
        """

        self._total_results = total_results

    @property
    def links(self):
        """Gets the links of this CodatPublicApiModelsCompanyCompanyPagedResponseModel.  # noqa: E501


        :return: The links of this CodatPublicApiModelsCompanyCompanyPagedResponseModel.  # noqa: E501
        :rtype: CodatPublicApiModelsCompanyCompanyPagedResponseLinksModel
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CodatPublicApiModelsCompanyCompanyPagedResponseModel.


        :param links: The links of this CodatPublicApiModelsCompanyCompanyPagedResponseModel.  # noqa: E501
        :type: CodatPublicApiModelsCompanyCompanyPagedResponseLinksModel
        """

        self._links = links

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
        if issubclass(CodatPublicApiModelsCompanyCompanyPagedResponseModel, dict):
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
        if not isinstance(other, CodatPublicApiModelsCompanyCompanyPagedResponseModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

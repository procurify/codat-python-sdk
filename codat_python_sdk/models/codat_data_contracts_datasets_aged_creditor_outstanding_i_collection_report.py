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

class CodatDataContractsDatasetsAgedCreditorOutstandingICollectionReport(object):
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
        'generated': 'datetime',
        'report_date': 'datetime',
        'data': 'list[CodatDataContractsDatasetsAgedCreditorOutstanding]'
    }

    attribute_map = {
        'generated': 'generated',
        'report_date': 'reportDate',
        'data': 'data'
    }

    def __init__(self, generated=None, report_date=None, data=None):  # noqa: E501
        """CodatDataContractsDatasetsAgedCreditorOutstandingICollectionReport - a model defined in Swagger"""  # noqa: E501
        self._generated = None
        self._report_date = None
        self._data = None
        self.discriminator = None
        self.generated = generated
        self.report_date = report_date
        self.data = data

    @property
    def generated(self):
        """Gets the generated of this CodatDataContractsDatasetsAgedCreditorOutstandingICollectionReport.  # noqa: E501


        :return: The generated of this CodatDataContractsDatasetsAgedCreditorOutstandingICollectionReport.  # noqa: E501
        :rtype: datetime
        """
        return self._generated

    @generated.setter
    def generated(self, generated):
        """Sets the generated of this CodatDataContractsDatasetsAgedCreditorOutstandingICollectionReport.


        :param generated: The generated of this CodatDataContractsDatasetsAgedCreditorOutstandingICollectionReport.  # noqa: E501
        :type: datetime
        """
        if generated is None:
            raise ValueError("Invalid value for `generated`, must not be `None`")  # noqa: E501

        self._generated = generated

    @property
    def report_date(self):
        """Gets the report_date of this CodatDataContractsDatasetsAgedCreditorOutstandingICollectionReport.  # noqa: E501


        :return: The report_date of this CodatDataContractsDatasetsAgedCreditorOutstandingICollectionReport.  # noqa: E501
        :rtype: datetime
        """
        return self._report_date

    @report_date.setter
    def report_date(self, report_date):
        """Sets the report_date of this CodatDataContractsDatasetsAgedCreditorOutstandingICollectionReport.


        :param report_date: The report_date of this CodatDataContractsDatasetsAgedCreditorOutstandingICollectionReport.  # noqa: E501
        :type: datetime
        """
        if report_date is None:
            raise ValueError("Invalid value for `report_date`, must not be `None`")  # noqa: E501

        self._report_date = report_date

    @property
    def data(self):
        """Gets the data of this CodatDataContractsDatasetsAgedCreditorOutstandingICollectionReport.  # noqa: E501


        :return: The data of this CodatDataContractsDatasetsAgedCreditorOutstandingICollectionReport.  # noqa: E501
        :rtype: list[CodatDataContractsDatasetsAgedCreditorOutstanding]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CodatDataContractsDatasetsAgedCreditorOutstandingICollectionReport.


        :param data: The data of this CodatDataContractsDatasetsAgedCreditorOutstandingICollectionReport.  # noqa: E501
        :type: list[CodatDataContractsDatasetsAgedCreditorOutstanding]
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
        if issubclass(CodatDataContractsDatasetsAgedCreditorOutstandingICollectionReport, dict):
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
        if not isinstance(other, CodatDataContractsDatasetsAgedCreditorOutstandingICollectionReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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

class CodatRulesContractsResponsesAlert(object):
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
        'rule_id': 'str',
        'company_id': 'str',
        'raised_on_utc': 'datetime',
        'resolved_on_utc': 'datetime',
        'data': 'Object'
    }

    attribute_map = {
        'id': 'id',
        'rule_id': 'ruleId',
        'company_id': 'companyId',
        'raised_on_utc': 'raisedOnUtc',
        'resolved_on_utc': 'resolvedOnUtc',
        'data': 'data'
    }

    def __init__(self, id=None, rule_id=None, company_id=None, raised_on_utc=None, resolved_on_utc=None, data=None):  # noqa: E501
        """CodatRulesContractsResponsesAlert - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._rule_id = None
        self._company_id = None
        self._raised_on_utc = None
        self._resolved_on_utc = None
        self._data = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if rule_id is not None:
            self.rule_id = rule_id
        if company_id is not None:
            self.company_id = company_id
        if raised_on_utc is not None:
            self.raised_on_utc = raised_on_utc
        if resolved_on_utc is not None:
            self.resolved_on_utc = resolved_on_utc
        if data is not None:
            self.data = data

    @property
    def id(self):
        """Gets the id of this CodatRulesContractsResponsesAlert.  # noqa: E501


        :return: The id of this CodatRulesContractsResponsesAlert.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CodatRulesContractsResponsesAlert.


        :param id: The id of this CodatRulesContractsResponsesAlert.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def rule_id(self):
        """Gets the rule_id of this CodatRulesContractsResponsesAlert.  # noqa: E501


        :return: The rule_id of this CodatRulesContractsResponsesAlert.  # noqa: E501
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this CodatRulesContractsResponsesAlert.


        :param rule_id: The rule_id of this CodatRulesContractsResponsesAlert.  # noqa: E501
        :type: str
        """

        self._rule_id = rule_id

    @property
    def company_id(self):
        """Gets the company_id of this CodatRulesContractsResponsesAlert.  # noqa: E501


        :return: The company_id of this CodatRulesContractsResponsesAlert.  # noqa: E501
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this CodatRulesContractsResponsesAlert.


        :param company_id: The company_id of this CodatRulesContractsResponsesAlert.  # noqa: E501
        :type: str
        """

        self._company_id = company_id

    @property
    def raised_on_utc(self):
        """Gets the raised_on_utc of this CodatRulesContractsResponsesAlert.  # noqa: E501


        :return: The raised_on_utc of this CodatRulesContractsResponsesAlert.  # noqa: E501
        :rtype: datetime
        """
        return self._raised_on_utc

    @raised_on_utc.setter
    def raised_on_utc(self, raised_on_utc):
        """Sets the raised_on_utc of this CodatRulesContractsResponsesAlert.


        :param raised_on_utc: The raised_on_utc of this CodatRulesContractsResponsesAlert.  # noqa: E501
        :type: datetime
        """

        self._raised_on_utc = raised_on_utc

    @property
    def resolved_on_utc(self):
        """Gets the resolved_on_utc of this CodatRulesContractsResponsesAlert.  # noqa: E501


        :return: The resolved_on_utc of this CodatRulesContractsResponsesAlert.  # noqa: E501
        :rtype: datetime
        """
        return self._resolved_on_utc

    @resolved_on_utc.setter
    def resolved_on_utc(self, resolved_on_utc):
        """Sets the resolved_on_utc of this CodatRulesContractsResponsesAlert.


        :param resolved_on_utc: The resolved_on_utc of this CodatRulesContractsResponsesAlert.  # noqa: E501
        :type: datetime
        """

        self._resolved_on_utc = resolved_on_utc

    @property
    def data(self):
        """Gets the data of this CodatRulesContractsResponsesAlert.  # noqa: E501


        :return: The data of this CodatRulesContractsResponsesAlert.  # noqa: E501
        :rtype: Object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CodatRulesContractsResponsesAlert.


        :param data: The data of this CodatRulesContractsResponsesAlert.  # noqa: E501
        :type: Object
        """

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
        if issubclass(CodatRulesContractsResponsesAlert, dict):
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
        if not isinstance(other, CodatRulesContractsResponsesAlert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
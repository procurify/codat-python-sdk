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

class CodatPublicApiModelsRulesAddRuleModel(object):
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
        'type': 'str',
        'notifiers': 'CodatPublicApiModelsRulesNotifiers'
    }

    attribute_map = {
        'company_id': 'companyId',
        'type': 'type',
        'notifiers': 'notifiers'
    }

    def __init__(self, company_id=None, type=None, notifiers=None):  # noqa: E501
        """CodatPublicApiModelsRulesAddRuleModel - a model defined in Swagger"""  # noqa: E501
        self._company_id = None
        self._type = None
        self._notifiers = None
        self.discriminator = None
        self.company_id = company_id
        self.type = type
        if notifiers is not None:
            self.notifiers = notifiers

    @property
    def company_id(self):
        """Gets the company_id of this CodatPublicApiModelsRulesAddRuleModel.  # noqa: E501

        Leave the companyID blank to create a rule that applies to all companies  # noqa: E501

        :return: The company_id of this CodatPublicApiModelsRulesAddRuleModel.  # noqa: E501
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this CodatPublicApiModelsRulesAddRuleModel.

        Leave the companyID blank to create a rule that applies to all companies  # noqa: E501

        :param company_id: The company_id of this CodatPublicApiModelsRulesAddRuleModel.  # noqa: E501
        :type: str
        """
        if company_id is None:
            raise ValueError("Invalid value for `company_id`, must not be `None`")  # noqa: E501

        self._company_id = company_id

    @property
    def type(self):
        """Gets the type of this CodatPublicApiModelsRulesAddRuleModel.  # noqa: E501


        :return: The type of this CodatPublicApiModelsRulesAddRuleModel.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CodatPublicApiModelsRulesAddRuleModel.


        :param type: The type of this CodatPublicApiModelsRulesAddRuleModel.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def notifiers(self):
        """Gets the notifiers of this CodatPublicApiModelsRulesAddRuleModel.  # noqa: E501


        :return: The notifiers of this CodatPublicApiModelsRulesAddRuleModel.  # noqa: E501
        :rtype: CodatPublicApiModelsRulesNotifiers
        """
        return self._notifiers

    @notifiers.setter
    def notifiers(self, notifiers):
        """Sets the notifiers of this CodatPublicApiModelsRulesAddRuleModel.


        :param notifiers: The notifiers of this CodatPublicApiModelsRulesAddRuleModel.  # noqa: E501
        :type: CodatPublicApiModelsRulesNotifiers
        """

        self._notifiers = notifiers

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
        if issubclass(CodatPublicApiModelsRulesAddRuleModel, dict):
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
        if not isinstance(other, CodatPublicApiModelsRulesAddRuleModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
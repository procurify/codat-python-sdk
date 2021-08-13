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

class CodatDataContractsDatasetsAccountsPayableTracking(object):
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
        'category_refs': 'list[CodatDataContractsDatasetsTrackingCategoryRef]',
        'project_ref': 'CodatDataContractsDatasetsProjectRef',
        'customer_ref': 'CodatDataContractsDatasetsCustomerRef',
        'is_billed_to': 'CodatDataContractsDatasetsAccountsPayableIsBilledToType'
    }

    attribute_map = {
        'category_refs': 'categoryRefs',
        'project_ref': 'projectRef',
        'customer_ref': 'customerRef',
        'is_billed_to': 'isBilledTo'
    }

    def __init__(self, category_refs=None, project_ref=None, customer_ref=None, is_billed_to=None):  # noqa: E501
        """CodatDataContractsDatasetsAccountsPayableTracking - a model defined in Swagger"""  # noqa: E501
        self._category_refs = None
        self._project_ref = None
        self._customer_ref = None
        self._is_billed_to = None
        self.discriminator = None
        self.category_refs = category_refs
        if project_ref is not None:
            self.project_ref = project_ref
        if customer_ref is not None:
            self.customer_ref = customer_ref
        self.is_billed_to = is_billed_to

    @property
    def category_refs(self):
        """Gets the category_refs of this CodatDataContractsDatasetsAccountsPayableTracking.  # noqa: E501


        :return: The category_refs of this CodatDataContractsDatasetsAccountsPayableTracking.  # noqa: E501
        :rtype: list[CodatDataContractsDatasetsTrackingCategoryRef]
        """
        return self._category_refs

    @category_refs.setter
    def category_refs(self, category_refs):
        """Sets the category_refs of this CodatDataContractsDatasetsAccountsPayableTracking.


        :param category_refs: The category_refs of this CodatDataContractsDatasetsAccountsPayableTracking.  # noqa: E501
        :type: list[CodatDataContractsDatasetsTrackingCategoryRef]
        """
        if category_refs is None:
            raise ValueError("Invalid value for `category_refs`, must not be `None`")  # noqa: E501

        self._category_refs = category_refs

    @property
    def project_ref(self):
        """Gets the project_ref of this CodatDataContractsDatasetsAccountsPayableTracking.  # noqa: E501


        :return: The project_ref of this CodatDataContractsDatasetsAccountsPayableTracking.  # noqa: E501
        :rtype: CodatDataContractsDatasetsProjectRef
        """
        return self._project_ref

    @project_ref.setter
    def project_ref(self, project_ref):
        """Sets the project_ref of this CodatDataContractsDatasetsAccountsPayableTracking.


        :param project_ref: The project_ref of this CodatDataContractsDatasetsAccountsPayableTracking.  # noqa: E501
        :type: CodatDataContractsDatasetsProjectRef
        """

        self._project_ref = project_ref

    @property
    def customer_ref(self):
        """Gets the customer_ref of this CodatDataContractsDatasetsAccountsPayableTracking.  # noqa: E501


        :return: The customer_ref of this CodatDataContractsDatasetsAccountsPayableTracking.  # noqa: E501
        :rtype: CodatDataContractsDatasetsCustomerRef
        """
        return self._customer_ref

    @customer_ref.setter
    def customer_ref(self, customer_ref):
        """Sets the customer_ref of this CodatDataContractsDatasetsAccountsPayableTracking.


        :param customer_ref: The customer_ref of this CodatDataContractsDatasetsAccountsPayableTracking.  # noqa: E501
        :type: CodatDataContractsDatasetsCustomerRef
        """

        self._customer_ref = customer_ref

    @property
    def is_billed_to(self):
        """Gets the is_billed_to of this CodatDataContractsDatasetsAccountsPayableTracking.  # noqa: E501


        :return: The is_billed_to of this CodatDataContractsDatasetsAccountsPayableTracking.  # noqa: E501
        :rtype: CodatDataContractsDatasetsAccountsPayableIsBilledToType
        """
        return self._is_billed_to

    @is_billed_to.setter
    def is_billed_to(self, is_billed_to):
        """Sets the is_billed_to of this CodatDataContractsDatasetsAccountsPayableTracking.


        :param is_billed_to: The is_billed_to of this CodatDataContractsDatasetsAccountsPayableTracking.  # noqa: E501
        :type: CodatDataContractsDatasetsAccountsPayableIsBilledToType
        """
        if is_billed_to is None:
            raise ValueError("Invalid value for `is_billed_to`, must not be `None`")  # noqa: E501

        self._is_billed_to = is_billed_to

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
        if issubclass(CodatDataContractsDatasetsAccountsPayableTracking, dict):
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
        if not isinstance(other, CodatDataContractsDatasetsAccountsPayableTracking):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

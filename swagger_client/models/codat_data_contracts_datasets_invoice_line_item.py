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

class CodatDataContractsDatasetsInvoiceLineItem(object):
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
        'description': 'str',
        'unit_amount': 'float',
        'quantity': 'float',
        'discount_amount': 'float',
        'sub_total': 'float',
        'tax_amount': 'float',
        'total_amount': 'float',
        'account_ref': 'CodatDataContractsDatasetsAccountRef',
        'discount_percentage': 'float',
        'tax_rate_ref': 'CodatDataContractsDatasetsTaxRateRef',
        'item_ref': 'CodatDataContractsDatasetsItemRef',
        'tracking_category_refs': 'list[CodatDataContractsDatasetsTrackingCategoryRef]',
        'tracking': 'CodatDataContractsDatasetsAccountsReceivableTracking'
    }

    attribute_map = {
        'description': 'description',
        'unit_amount': 'unitAmount',
        'quantity': 'quantity',
        'discount_amount': 'discountAmount',
        'sub_total': 'subTotal',
        'tax_amount': 'taxAmount',
        'total_amount': 'totalAmount',
        'account_ref': 'accountRef',
        'discount_percentage': 'discountPercentage',
        'tax_rate_ref': 'taxRateRef',
        'item_ref': 'itemRef',
        'tracking_category_refs': 'trackingCategoryRefs',
        'tracking': 'tracking'
    }

    def __init__(self, description=None, unit_amount=None, quantity=None, discount_amount=None, sub_total=None, tax_amount=None, total_amount=None, account_ref=None, discount_percentage=None, tax_rate_ref=None, item_ref=None, tracking_category_refs=None, tracking=None):  # noqa: E501
        """CodatDataContractsDatasetsInvoiceLineItem - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._unit_amount = None
        self._quantity = None
        self._discount_amount = None
        self._sub_total = None
        self._tax_amount = None
        self._total_amount = None
        self._account_ref = None
        self._discount_percentage = None
        self._tax_rate_ref = None
        self._item_ref = None
        self._tracking_category_refs = None
        self._tracking = None
        self.discriminator = None
        if description is not None:
            self.description = description
        self.unit_amount = unit_amount
        self.quantity = quantity
        if discount_amount is not None:
            self.discount_amount = discount_amount
        if sub_total is not None:
            self.sub_total = sub_total
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if total_amount is not None:
            self.total_amount = total_amount
        if account_ref is not None:
            self.account_ref = account_ref
        if discount_percentage is not None:
            self.discount_percentage = discount_percentage
        if tax_rate_ref is not None:
            self.tax_rate_ref = tax_rate_ref
        if item_ref is not None:
            self.item_ref = item_ref
        if tracking_category_refs is not None:
            self.tracking_category_refs = tracking_category_refs
        if tracking is not None:
            self.tracking = tracking

    @property
    def description(self):
        """Gets the description of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501


        :return: The description of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CodatDataContractsDatasetsInvoiceLineItem.


        :param description: The description of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def unit_amount(self):
        """Gets the unit_amount of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501


        :return: The unit_amount of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501
        :rtype: float
        """
        return self._unit_amount

    @unit_amount.setter
    def unit_amount(self, unit_amount):
        """Sets the unit_amount of this CodatDataContractsDatasetsInvoiceLineItem.


        :param unit_amount: The unit_amount of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501
        :type: float
        """
        if unit_amount is None:
            raise ValueError("Invalid value for `unit_amount`, must not be `None`")  # noqa: E501

        self._unit_amount = unit_amount

    @property
    def quantity(self):
        """Gets the quantity of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501


        :return: The quantity of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this CodatDataContractsDatasetsInvoiceLineItem.


        :param quantity: The quantity of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501
        :type: float
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def discount_amount(self):
        """Gets the discount_amount of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501


        :return: The discount_amount of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501
        :rtype: float
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """Sets the discount_amount of this CodatDataContractsDatasetsInvoiceLineItem.


        :param discount_amount: The discount_amount of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501
        :type: float
        """

        self._discount_amount = discount_amount

    @property
    def sub_total(self):
        """Gets the sub_total of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501


        :return: The sub_total of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501
        :rtype: float
        """
        return self._sub_total

    @sub_total.setter
    def sub_total(self, sub_total):
        """Sets the sub_total of this CodatDataContractsDatasetsInvoiceLineItem.


        :param sub_total: The sub_total of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501
        :type: float
        """

        self._sub_total = sub_total

    @property
    def tax_amount(self):
        """Gets the tax_amount of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501


        :return: The tax_amount of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501
        :rtype: float
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this CodatDataContractsDatasetsInvoiceLineItem.


        :param tax_amount: The tax_amount of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501
        :type: float
        """

        self._tax_amount = tax_amount

    @property
    def total_amount(self):
        """Gets the total_amount of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501


        :return: The total_amount of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501
        :rtype: float
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this CodatDataContractsDatasetsInvoiceLineItem.


        :param total_amount: The total_amount of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501
        :type: float
        """

        self._total_amount = total_amount

    @property
    def account_ref(self):
        """Gets the account_ref of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501


        :return: The account_ref of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501
        :rtype: CodatDataContractsDatasetsAccountRef
        """
        return self._account_ref

    @account_ref.setter
    def account_ref(self, account_ref):
        """Sets the account_ref of this CodatDataContractsDatasetsInvoiceLineItem.


        :param account_ref: The account_ref of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501
        :type: CodatDataContractsDatasetsAccountRef
        """

        self._account_ref = account_ref

    @property
    def discount_percentage(self):
        """Gets the discount_percentage of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501


        :return: The discount_percentage of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501
        :rtype: float
        """
        return self._discount_percentage

    @discount_percentage.setter
    def discount_percentage(self, discount_percentage):
        """Sets the discount_percentage of this CodatDataContractsDatasetsInvoiceLineItem.


        :param discount_percentage: The discount_percentage of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501
        :type: float
        """

        self._discount_percentage = discount_percentage

    @property
    def tax_rate_ref(self):
        """Gets the tax_rate_ref of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501


        :return: The tax_rate_ref of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501
        :rtype: CodatDataContractsDatasetsTaxRateRef
        """
        return self._tax_rate_ref

    @tax_rate_ref.setter
    def tax_rate_ref(self, tax_rate_ref):
        """Sets the tax_rate_ref of this CodatDataContractsDatasetsInvoiceLineItem.


        :param tax_rate_ref: The tax_rate_ref of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501
        :type: CodatDataContractsDatasetsTaxRateRef
        """

        self._tax_rate_ref = tax_rate_ref

    @property
    def item_ref(self):
        """Gets the item_ref of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501


        :return: The item_ref of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501
        :rtype: CodatDataContractsDatasetsItemRef
        """
        return self._item_ref

    @item_ref.setter
    def item_ref(self, item_ref):
        """Sets the item_ref of this CodatDataContractsDatasetsInvoiceLineItem.


        :param item_ref: The item_ref of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501
        :type: CodatDataContractsDatasetsItemRef
        """

        self._item_ref = item_ref

    @property
    def tracking_category_refs(self):
        """Gets the tracking_category_refs of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501


        :return: The tracking_category_refs of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501
        :rtype: list[CodatDataContractsDatasetsTrackingCategoryRef]
        """
        return self._tracking_category_refs

    @tracking_category_refs.setter
    def tracking_category_refs(self, tracking_category_refs):
        """Sets the tracking_category_refs of this CodatDataContractsDatasetsInvoiceLineItem.


        :param tracking_category_refs: The tracking_category_refs of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501
        :type: list[CodatDataContractsDatasetsTrackingCategoryRef]
        """

        self._tracking_category_refs = tracking_category_refs

    @property
    def tracking(self):
        """Gets the tracking of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501


        :return: The tracking of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501
        :rtype: CodatDataContractsDatasetsAccountsReceivableTracking
        """
        return self._tracking

    @tracking.setter
    def tracking(self, tracking):
        """Sets the tracking of this CodatDataContractsDatasetsInvoiceLineItem.


        :param tracking: The tracking of this CodatDataContractsDatasetsInvoiceLineItem.  # noqa: E501
        :type: CodatDataContractsDatasetsAccountsReceivableTracking
        """

        self._tracking = tracking

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
        if issubclass(CodatDataContractsDatasetsInvoiceLineItem, dict):
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
        if not isinstance(other, CodatDataContractsDatasetsInvoiceLineItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

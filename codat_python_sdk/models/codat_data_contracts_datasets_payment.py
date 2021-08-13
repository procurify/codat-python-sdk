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

class CodatDataContractsDatasetsPayment(object):
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
        'customer_ref': 'CodatDataContractsDatasetsCustomerRef',
        'account_ref': 'CodatDataContractsDatasetsAccountRef',
        'total_amount': 'float',
        'currency': 'str',
        'currency_rate': 'float',
        '_date': 'datetime',
        'note': 'str',
        'lines': 'list[CodatDataContractsDatasetsPaymentLine]',
        'modified_date': 'datetime',
        'source_modified_date': 'datetime',
        'reference': 'str'
    }

    attribute_map = {
        'id': 'id',
        'customer_ref': 'customerRef',
        'account_ref': 'accountRef',
        'total_amount': 'totalAmount',
        'currency': 'currency',
        'currency_rate': 'currencyRate',
        '_date': 'date',
        'note': 'note',
        'lines': 'lines',
        'modified_date': 'modifiedDate',
        'source_modified_date': 'sourceModifiedDate',
        'reference': 'reference'
    }

    def __init__(self, id=None, customer_ref=None, account_ref=None, total_amount=None, currency=None, currency_rate=None, _date=None, note=None, lines=None, modified_date=None, source_modified_date=None, reference=None):  # noqa: E501
        """CodatDataContractsDatasetsPayment - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._customer_ref = None
        self._account_ref = None
        self._total_amount = None
        self._currency = None
        self._currency_rate = None
        self.__date = None
        self._note = None
        self._lines = None
        self._modified_date = None
        self._source_modified_date = None
        self._reference = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if customer_ref is not None:
            self.customer_ref = customer_ref
        if account_ref is not None:
            self.account_ref = account_ref
        if total_amount is not None:
            self.total_amount = total_amount
        if currency is not None:
            self.currency = currency
        if currency_rate is not None:
            self.currency_rate = currency_rate
        self._date = _date
        if note is not None:
            self.note = note
        if lines is not None:
            self.lines = lines
        if modified_date is not None:
            self.modified_date = modified_date
        if source_modified_date is not None:
            self.source_modified_date = source_modified_date
        if reference is not None:
            self.reference = reference

    @property
    def id(self):
        """Gets the id of this CodatDataContractsDatasetsPayment.  # noqa: E501


        :return: The id of this CodatDataContractsDatasetsPayment.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CodatDataContractsDatasetsPayment.


        :param id: The id of this CodatDataContractsDatasetsPayment.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def customer_ref(self):
        """Gets the customer_ref of this CodatDataContractsDatasetsPayment.  # noqa: E501


        :return: The customer_ref of this CodatDataContractsDatasetsPayment.  # noqa: E501
        :rtype: CodatDataContractsDatasetsCustomerRef
        """
        return self._customer_ref

    @customer_ref.setter
    def customer_ref(self, customer_ref):
        """Sets the customer_ref of this CodatDataContractsDatasetsPayment.


        :param customer_ref: The customer_ref of this CodatDataContractsDatasetsPayment.  # noqa: E501
        :type: CodatDataContractsDatasetsCustomerRef
        """

        self._customer_ref = customer_ref

    @property
    def account_ref(self):
        """Gets the account_ref of this CodatDataContractsDatasetsPayment.  # noqa: E501


        :return: The account_ref of this CodatDataContractsDatasetsPayment.  # noqa: E501
        :rtype: CodatDataContractsDatasetsAccountRef
        """
        return self._account_ref

    @account_ref.setter
    def account_ref(self, account_ref):
        """Sets the account_ref of this CodatDataContractsDatasetsPayment.


        :param account_ref: The account_ref of this CodatDataContractsDatasetsPayment.  # noqa: E501
        :type: CodatDataContractsDatasetsAccountRef
        """

        self._account_ref = account_ref

    @property
    def total_amount(self):
        """Gets the total_amount of this CodatDataContractsDatasetsPayment.  # noqa: E501


        :return: The total_amount of this CodatDataContractsDatasetsPayment.  # noqa: E501
        :rtype: float
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this CodatDataContractsDatasetsPayment.


        :param total_amount: The total_amount of this CodatDataContractsDatasetsPayment.  # noqa: E501
        :type: float
        """

        self._total_amount = total_amount

    @property
    def currency(self):
        """Gets the currency of this CodatDataContractsDatasetsPayment.  # noqa: E501


        :return: The currency of this CodatDataContractsDatasetsPayment.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this CodatDataContractsDatasetsPayment.


        :param currency: The currency of this CodatDataContractsDatasetsPayment.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def currency_rate(self):
        """Gets the currency_rate of this CodatDataContractsDatasetsPayment.  # noqa: E501


        :return: The currency_rate of this CodatDataContractsDatasetsPayment.  # noqa: E501
        :rtype: float
        """
        return self._currency_rate

    @currency_rate.setter
    def currency_rate(self, currency_rate):
        """Sets the currency_rate of this CodatDataContractsDatasetsPayment.


        :param currency_rate: The currency_rate of this CodatDataContractsDatasetsPayment.  # noqa: E501
        :type: float
        """

        self._currency_rate = currency_rate

    @property
    def _date(self):
        """Gets the _date of this CodatDataContractsDatasetsPayment.  # noqa: E501


        :return: The _date of this CodatDataContractsDatasetsPayment.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this CodatDataContractsDatasetsPayment.


        :param _date: The _date of this CodatDataContractsDatasetsPayment.  # noqa: E501
        :type: datetime
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def note(self):
        """Gets the note of this CodatDataContractsDatasetsPayment.  # noqa: E501


        :return: The note of this CodatDataContractsDatasetsPayment.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this CodatDataContractsDatasetsPayment.


        :param note: The note of this CodatDataContractsDatasetsPayment.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def lines(self):
        """Gets the lines of this CodatDataContractsDatasetsPayment.  # noqa: E501


        :return: The lines of this CodatDataContractsDatasetsPayment.  # noqa: E501
        :rtype: list[CodatDataContractsDatasetsPaymentLine]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """Sets the lines of this CodatDataContractsDatasetsPayment.


        :param lines: The lines of this CodatDataContractsDatasetsPayment.  # noqa: E501
        :type: list[CodatDataContractsDatasetsPaymentLine]
        """

        self._lines = lines

    @property
    def modified_date(self):
        """Gets the modified_date of this CodatDataContractsDatasetsPayment.  # noqa: E501


        :return: The modified_date of this CodatDataContractsDatasetsPayment.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """Sets the modified_date of this CodatDataContractsDatasetsPayment.


        :param modified_date: The modified_date of this CodatDataContractsDatasetsPayment.  # noqa: E501
        :type: datetime
        """

        self._modified_date = modified_date

    @property
    def source_modified_date(self):
        """Gets the source_modified_date of this CodatDataContractsDatasetsPayment.  # noqa: E501


        :return: The source_modified_date of this CodatDataContractsDatasetsPayment.  # noqa: E501
        :rtype: datetime
        """
        return self._source_modified_date

    @source_modified_date.setter
    def source_modified_date(self, source_modified_date):
        """Sets the source_modified_date of this CodatDataContractsDatasetsPayment.


        :param source_modified_date: The source_modified_date of this CodatDataContractsDatasetsPayment.  # noqa: E501
        :type: datetime
        """

        self._source_modified_date = source_modified_date

    @property
    def reference(self):
        """Gets the reference of this CodatDataContractsDatasetsPayment.  # noqa: E501


        :return: The reference of this CodatDataContractsDatasetsPayment.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this CodatDataContractsDatasetsPayment.


        :param reference: The reference of this CodatDataContractsDatasetsPayment.  # noqa: E501
        :type: str
        """

        self._reference = reference

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
        if issubclass(CodatDataContractsDatasetsPayment, dict):
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
        if not isinstance(other, CodatDataContractsDatasetsPayment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
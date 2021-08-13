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

class CodatDataContractsDatasetsCommerceDispute(object):
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
        'disputed_transactions': 'list[CodatDataContractsDatasetsCommerceTransactionSourceRef]',
        'total_amount': 'float',
        'currency': 'str',
        'status': 'CodatDataContractsDatasetsCommerceDisputeStatus',
        'reason': 'str',
        'due_date': 'datetime',
        'created_date': 'datetime',
        'modified_date': 'datetime',
        'source_modified_date': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'disputed_transactions': 'disputedTransactions',
        'total_amount': 'totalAmount',
        'currency': 'currency',
        'status': 'status',
        'reason': 'reason',
        'due_date': 'dueDate',
        'created_date': 'createdDate',
        'modified_date': 'modifiedDate',
        'source_modified_date': 'sourceModifiedDate'
    }

    def __init__(self, id=None, disputed_transactions=None, total_amount=None, currency=None, status=None, reason=None, due_date=None, created_date=None, modified_date=None, source_modified_date=None):  # noqa: E501
        """CodatDataContractsDatasetsCommerceDispute - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._disputed_transactions = None
        self._total_amount = None
        self._currency = None
        self._status = None
        self._reason = None
        self._due_date = None
        self._created_date = None
        self._modified_date = None
        self._source_modified_date = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if disputed_transactions is not None:
            self.disputed_transactions = disputed_transactions
        if total_amount is not None:
            self.total_amount = total_amount
        if currency is not None:
            self.currency = currency
        if status is not None:
            self.status = status
        if reason is not None:
            self.reason = reason
        if due_date is not None:
            self.due_date = due_date
        if created_date is not None:
            self.created_date = created_date
        if modified_date is not None:
            self.modified_date = modified_date
        if source_modified_date is not None:
            self.source_modified_date = source_modified_date

    @property
    def id(self):
        """Gets the id of this CodatDataContractsDatasetsCommerceDispute.  # noqa: E501


        :return: The id of this CodatDataContractsDatasetsCommerceDispute.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CodatDataContractsDatasetsCommerceDispute.


        :param id: The id of this CodatDataContractsDatasetsCommerceDispute.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def disputed_transactions(self):
        """Gets the disputed_transactions of this CodatDataContractsDatasetsCommerceDispute.  # noqa: E501


        :return: The disputed_transactions of this CodatDataContractsDatasetsCommerceDispute.  # noqa: E501
        :rtype: list[CodatDataContractsDatasetsCommerceTransactionSourceRef]
        """
        return self._disputed_transactions

    @disputed_transactions.setter
    def disputed_transactions(self, disputed_transactions):
        """Sets the disputed_transactions of this CodatDataContractsDatasetsCommerceDispute.


        :param disputed_transactions: The disputed_transactions of this CodatDataContractsDatasetsCommerceDispute.  # noqa: E501
        :type: list[CodatDataContractsDatasetsCommerceTransactionSourceRef]
        """

        self._disputed_transactions = disputed_transactions

    @property
    def total_amount(self):
        """Gets the total_amount of this CodatDataContractsDatasetsCommerceDispute.  # noqa: E501


        :return: The total_amount of this CodatDataContractsDatasetsCommerceDispute.  # noqa: E501
        :rtype: float
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this CodatDataContractsDatasetsCommerceDispute.


        :param total_amount: The total_amount of this CodatDataContractsDatasetsCommerceDispute.  # noqa: E501
        :type: float
        """

        self._total_amount = total_amount

    @property
    def currency(self):
        """Gets the currency of this CodatDataContractsDatasetsCommerceDispute.  # noqa: E501


        :return: The currency of this CodatDataContractsDatasetsCommerceDispute.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this CodatDataContractsDatasetsCommerceDispute.


        :param currency: The currency of this CodatDataContractsDatasetsCommerceDispute.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def status(self):
        """Gets the status of this CodatDataContractsDatasetsCommerceDispute.  # noqa: E501


        :return: The status of this CodatDataContractsDatasetsCommerceDispute.  # noqa: E501
        :rtype: CodatDataContractsDatasetsCommerceDisputeStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CodatDataContractsDatasetsCommerceDispute.


        :param status: The status of this CodatDataContractsDatasetsCommerceDispute.  # noqa: E501
        :type: CodatDataContractsDatasetsCommerceDisputeStatus
        """

        self._status = status

    @property
    def reason(self):
        """Gets the reason of this CodatDataContractsDatasetsCommerceDispute.  # noqa: E501


        :return: The reason of this CodatDataContractsDatasetsCommerceDispute.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this CodatDataContractsDatasetsCommerceDispute.


        :param reason: The reason of this CodatDataContractsDatasetsCommerceDispute.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def due_date(self):
        """Gets the due_date of this CodatDataContractsDatasetsCommerceDispute.  # noqa: E501


        :return: The due_date of this CodatDataContractsDatasetsCommerceDispute.  # noqa: E501
        :rtype: datetime
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this CodatDataContractsDatasetsCommerceDispute.


        :param due_date: The due_date of this CodatDataContractsDatasetsCommerceDispute.  # noqa: E501
        :type: datetime
        """

        self._due_date = due_date

    @property
    def created_date(self):
        """Gets the created_date of this CodatDataContractsDatasetsCommerceDispute.  # noqa: E501


        :return: The created_date of this CodatDataContractsDatasetsCommerceDispute.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this CodatDataContractsDatasetsCommerceDispute.


        :param created_date: The created_date of this CodatDataContractsDatasetsCommerceDispute.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def modified_date(self):
        """Gets the modified_date of this CodatDataContractsDatasetsCommerceDispute.  # noqa: E501


        :return: The modified_date of this CodatDataContractsDatasetsCommerceDispute.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """Sets the modified_date of this CodatDataContractsDatasetsCommerceDispute.


        :param modified_date: The modified_date of this CodatDataContractsDatasetsCommerceDispute.  # noqa: E501
        :type: datetime
        """

        self._modified_date = modified_date

    @property
    def source_modified_date(self):
        """Gets the source_modified_date of this CodatDataContractsDatasetsCommerceDispute.  # noqa: E501


        :return: The source_modified_date of this CodatDataContractsDatasetsCommerceDispute.  # noqa: E501
        :rtype: datetime
        """
        return self._source_modified_date

    @source_modified_date.setter
    def source_modified_date(self, source_modified_date):
        """Sets the source_modified_date of this CodatDataContractsDatasetsCommerceDispute.


        :param source_modified_date: The source_modified_date of this CodatDataContractsDatasetsCommerceDispute.  # noqa: E501
        :type: datetime
        """

        self._source_modified_date = source_modified_date

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
        if issubclass(CodatDataContractsDatasetsCommerceDispute, dict):
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
        if not isinstance(other, CodatDataContractsDatasetsCommerceDispute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
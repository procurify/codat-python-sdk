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

class CodatDataContractsDatasetsCommerceCustomer(object):
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
        'customer_name': 'str',
        'email_address': 'str',
        'default_currency': 'str',
        'phone': 'str',
        'addresses': 'list[CodatDataContractsDatasetsCommerceAddress]',
        'note': 'str',
        'created_date': 'datetime',
        'modified_date': 'datetime',
        'source_modified_date': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'customer_name': 'customerName',
        'email_address': 'emailAddress',
        'default_currency': 'defaultCurrency',
        'phone': 'phone',
        'addresses': 'addresses',
        'note': 'note',
        'created_date': 'createdDate',
        'modified_date': 'modifiedDate',
        'source_modified_date': 'sourceModifiedDate'
    }

    def __init__(self, id=None, customer_name=None, email_address=None, default_currency=None, phone=None, addresses=None, note=None, created_date=None, modified_date=None, source_modified_date=None):  # noqa: E501
        """CodatDataContractsDatasetsCommerceCustomer - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._customer_name = None
        self._email_address = None
        self._default_currency = None
        self._phone = None
        self._addresses = None
        self._note = None
        self._created_date = None
        self._modified_date = None
        self._source_modified_date = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if customer_name is not None:
            self.customer_name = customer_name
        if email_address is not None:
            self.email_address = email_address
        if default_currency is not None:
            self.default_currency = default_currency
        if phone is not None:
            self.phone = phone
        if addresses is not None:
            self.addresses = addresses
        if note is not None:
            self.note = note
        if created_date is not None:
            self.created_date = created_date
        if modified_date is not None:
            self.modified_date = modified_date
        if source_modified_date is not None:
            self.source_modified_date = source_modified_date

    @property
    def id(self):
        """Gets the id of this CodatDataContractsDatasetsCommerceCustomer.  # noqa: E501


        :return: The id of this CodatDataContractsDatasetsCommerceCustomer.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CodatDataContractsDatasetsCommerceCustomer.


        :param id: The id of this CodatDataContractsDatasetsCommerceCustomer.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def customer_name(self):
        """Gets the customer_name of this CodatDataContractsDatasetsCommerceCustomer.  # noqa: E501


        :return: The customer_name of this CodatDataContractsDatasetsCommerceCustomer.  # noqa: E501
        :rtype: str
        """
        return self._customer_name

    @customer_name.setter
    def customer_name(self, customer_name):
        """Sets the customer_name of this CodatDataContractsDatasetsCommerceCustomer.


        :param customer_name: The customer_name of this CodatDataContractsDatasetsCommerceCustomer.  # noqa: E501
        :type: str
        """

        self._customer_name = customer_name

    @property
    def email_address(self):
        """Gets the email_address of this CodatDataContractsDatasetsCommerceCustomer.  # noqa: E501


        :return: The email_address of this CodatDataContractsDatasetsCommerceCustomer.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this CodatDataContractsDatasetsCommerceCustomer.


        :param email_address: The email_address of this CodatDataContractsDatasetsCommerceCustomer.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def default_currency(self):
        """Gets the default_currency of this CodatDataContractsDatasetsCommerceCustomer.  # noqa: E501


        :return: The default_currency of this CodatDataContractsDatasetsCommerceCustomer.  # noqa: E501
        :rtype: str
        """
        return self._default_currency

    @default_currency.setter
    def default_currency(self, default_currency):
        """Sets the default_currency of this CodatDataContractsDatasetsCommerceCustomer.


        :param default_currency: The default_currency of this CodatDataContractsDatasetsCommerceCustomer.  # noqa: E501
        :type: str
        """

        self._default_currency = default_currency

    @property
    def phone(self):
        """Gets the phone of this CodatDataContractsDatasetsCommerceCustomer.  # noqa: E501


        :return: The phone of this CodatDataContractsDatasetsCommerceCustomer.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this CodatDataContractsDatasetsCommerceCustomer.


        :param phone: The phone of this CodatDataContractsDatasetsCommerceCustomer.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def addresses(self):
        """Gets the addresses of this CodatDataContractsDatasetsCommerceCustomer.  # noqa: E501


        :return: The addresses of this CodatDataContractsDatasetsCommerceCustomer.  # noqa: E501
        :rtype: list[CodatDataContractsDatasetsCommerceAddress]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this CodatDataContractsDatasetsCommerceCustomer.


        :param addresses: The addresses of this CodatDataContractsDatasetsCommerceCustomer.  # noqa: E501
        :type: list[CodatDataContractsDatasetsCommerceAddress]
        """

        self._addresses = addresses

    @property
    def note(self):
        """Gets the note of this CodatDataContractsDatasetsCommerceCustomer.  # noqa: E501


        :return: The note of this CodatDataContractsDatasetsCommerceCustomer.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this CodatDataContractsDatasetsCommerceCustomer.


        :param note: The note of this CodatDataContractsDatasetsCommerceCustomer.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def created_date(self):
        """Gets the created_date of this CodatDataContractsDatasetsCommerceCustomer.  # noqa: E501


        :return: The created_date of this CodatDataContractsDatasetsCommerceCustomer.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this CodatDataContractsDatasetsCommerceCustomer.


        :param created_date: The created_date of this CodatDataContractsDatasetsCommerceCustomer.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def modified_date(self):
        """Gets the modified_date of this CodatDataContractsDatasetsCommerceCustomer.  # noqa: E501


        :return: The modified_date of this CodatDataContractsDatasetsCommerceCustomer.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """Sets the modified_date of this CodatDataContractsDatasetsCommerceCustomer.


        :param modified_date: The modified_date of this CodatDataContractsDatasetsCommerceCustomer.  # noqa: E501
        :type: datetime
        """

        self._modified_date = modified_date

    @property
    def source_modified_date(self):
        """Gets the source_modified_date of this CodatDataContractsDatasetsCommerceCustomer.  # noqa: E501


        :return: The source_modified_date of this CodatDataContractsDatasetsCommerceCustomer.  # noqa: E501
        :rtype: datetime
        """
        return self._source_modified_date

    @source_modified_date.setter
    def source_modified_date(self, source_modified_date):
        """Sets the source_modified_date of this CodatDataContractsDatasetsCommerceCustomer.


        :param source_modified_date: The source_modified_date of this CodatDataContractsDatasetsCommerceCustomer.  # noqa: E501
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
        if issubclass(CodatDataContractsDatasetsCommerceCustomer, dict):
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
        if not isinstance(other, CodatDataContractsDatasetsCommerceCustomer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
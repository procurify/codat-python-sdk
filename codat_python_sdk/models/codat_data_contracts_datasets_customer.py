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

class CodatDataContractsDatasetsCustomer(object):
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
        'contact_name': 'str',
        'email_address': 'str',
        'default_currency': 'str',
        'phone': 'str',
        'addresses': 'list[CodatDataContractsDatasetsAddress]',
        'contacts': 'list[CodatDataContractsDatasetsContact]',
        'registration_number': 'str',
        'tax_number': 'str',
        'status': 'CodatDataContractsDatasetsCustomerStatus',
        'modified_date': 'datetime',
        'source_modified_date': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'customer_name': 'customerName',
        'contact_name': 'contactName',
        'email_address': 'emailAddress',
        'default_currency': 'defaultCurrency',
        'phone': 'phone',
        'addresses': 'addresses',
        'contacts': 'contacts',
        'registration_number': 'registrationNumber',
        'tax_number': 'taxNumber',
        'status': 'status',
        'modified_date': 'modifiedDate',
        'source_modified_date': 'sourceModifiedDate'
    }

    def __init__(self, id=None, customer_name=None, contact_name=None, email_address=None, default_currency=None, phone=None, addresses=None, contacts=None, registration_number=None, tax_number=None, status=None, modified_date=None, source_modified_date=None):  # noqa: E501
        """CodatDataContractsDatasetsCustomer - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._customer_name = None
        self._contact_name = None
        self._email_address = None
        self._default_currency = None
        self._phone = None
        self._addresses = None
        self._contacts = None
        self._registration_number = None
        self._tax_number = None
        self._status = None
        self._modified_date = None
        self._source_modified_date = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if customer_name is not None:
            self.customer_name = customer_name
        if contact_name is not None:
            self.contact_name = contact_name
        if email_address is not None:
            self.email_address = email_address
        if default_currency is not None:
            self.default_currency = default_currency
        if phone is not None:
            self.phone = phone
        if addresses is not None:
            self.addresses = addresses
        if contacts is not None:
            self.contacts = contacts
        if registration_number is not None:
            self.registration_number = registration_number
        if tax_number is not None:
            self.tax_number = tax_number
        self.status = status
        if modified_date is not None:
            self.modified_date = modified_date
        if source_modified_date is not None:
            self.source_modified_date = source_modified_date

    @property
    def id(self):
        """Gets the id of this CodatDataContractsDatasetsCustomer.  # noqa: E501


        :return: The id of this CodatDataContractsDatasetsCustomer.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CodatDataContractsDatasetsCustomer.


        :param id: The id of this CodatDataContractsDatasetsCustomer.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def customer_name(self):
        """Gets the customer_name of this CodatDataContractsDatasetsCustomer.  # noqa: E501


        :return: The customer_name of this CodatDataContractsDatasetsCustomer.  # noqa: E501
        :rtype: str
        """
        return self._customer_name

    @customer_name.setter
    def customer_name(self, customer_name):
        """Sets the customer_name of this CodatDataContractsDatasetsCustomer.


        :param customer_name: The customer_name of this CodatDataContractsDatasetsCustomer.  # noqa: E501
        :type: str
        """

        self._customer_name = customer_name

    @property
    def contact_name(self):
        """Gets the contact_name of this CodatDataContractsDatasetsCustomer.  # noqa: E501


        :return: The contact_name of this CodatDataContractsDatasetsCustomer.  # noqa: E501
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        """Sets the contact_name of this CodatDataContractsDatasetsCustomer.


        :param contact_name: The contact_name of this CodatDataContractsDatasetsCustomer.  # noqa: E501
        :type: str
        """

        self._contact_name = contact_name

    @property
    def email_address(self):
        """Gets the email_address of this CodatDataContractsDatasetsCustomer.  # noqa: E501


        :return: The email_address of this CodatDataContractsDatasetsCustomer.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this CodatDataContractsDatasetsCustomer.


        :param email_address: The email_address of this CodatDataContractsDatasetsCustomer.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def default_currency(self):
        """Gets the default_currency of this CodatDataContractsDatasetsCustomer.  # noqa: E501


        :return: The default_currency of this CodatDataContractsDatasetsCustomer.  # noqa: E501
        :rtype: str
        """
        return self._default_currency

    @default_currency.setter
    def default_currency(self, default_currency):
        """Sets the default_currency of this CodatDataContractsDatasetsCustomer.


        :param default_currency: The default_currency of this CodatDataContractsDatasetsCustomer.  # noqa: E501
        :type: str
        """

        self._default_currency = default_currency

    @property
    def phone(self):
        """Gets the phone of this CodatDataContractsDatasetsCustomer.  # noqa: E501


        :return: The phone of this CodatDataContractsDatasetsCustomer.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this CodatDataContractsDatasetsCustomer.


        :param phone: The phone of this CodatDataContractsDatasetsCustomer.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def addresses(self):
        """Gets the addresses of this CodatDataContractsDatasetsCustomer.  # noqa: E501


        :return: The addresses of this CodatDataContractsDatasetsCustomer.  # noqa: E501
        :rtype: list[CodatDataContractsDatasetsAddress]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this CodatDataContractsDatasetsCustomer.


        :param addresses: The addresses of this CodatDataContractsDatasetsCustomer.  # noqa: E501
        :type: list[CodatDataContractsDatasetsAddress]
        """

        self._addresses = addresses

    @property
    def contacts(self):
        """Gets the contacts of this CodatDataContractsDatasetsCustomer.  # noqa: E501


        :return: The contacts of this CodatDataContractsDatasetsCustomer.  # noqa: E501
        :rtype: list[CodatDataContractsDatasetsContact]
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        """Sets the contacts of this CodatDataContractsDatasetsCustomer.


        :param contacts: The contacts of this CodatDataContractsDatasetsCustomer.  # noqa: E501
        :type: list[CodatDataContractsDatasetsContact]
        """

        self._contacts = contacts

    @property
    def registration_number(self):
        """Gets the registration_number of this CodatDataContractsDatasetsCustomer.  # noqa: E501


        :return: The registration_number of this CodatDataContractsDatasetsCustomer.  # noqa: E501
        :rtype: str
        """
        return self._registration_number

    @registration_number.setter
    def registration_number(self, registration_number):
        """Sets the registration_number of this CodatDataContractsDatasetsCustomer.


        :param registration_number: The registration_number of this CodatDataContractsDatasetsCustomer.  # noqa: E501
        :type: str
        """

        self._registration_number = registration_number

    @property
    def tax_number(self):
        """Gets the tax_number of this CodatDataContractsDatasetsCustomer.  # noqa: E501


        :return: The tax_number of this CodatDataContractsDatasetsCustomer.  # noqa: E501
        :rtype: str
        """
        return self._tax_number

    @tax_number.setter
    def tax_number(self, tax_number):
        """Sets the tax_number of this CodatDataContractsDatasetsCustomer.


        :param tax_number: The tax_number of this CodatDataContractsDatasetsCustomer.  # noqa: E501
        :type: str
        """

        self._tax_number = tax_number

    @property
    def status(self):
        """Gets the status of this CodatDataContractsDatasetsCustomer.  # noqa: E501


        :return: The status of this CodatDataContractsDatasetsCustomer.  # noqa: E501
        :rtype: CodatDataContractsDatasetsCustomerStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CodatDataContractsDatasetsCustomer.


        :param status: The status of this CodatDataContractsDatasetsCustomer.  # noqa: E501
        :type: CodatDataContractsDatasetsCustomerStatus
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def modified_date(self):
        """Gets the modified_date of this CodatDataContractsDatasetsCustomer.  # noqa: E501


        :return: The modified_date of this CodatDataContractsDatasetsCustomer.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """Sets the modified_date of this CodatDataContractsDatasetsCustomer.


        :param modified_date: The modified_date of this CodatDataContractsDatasetsCustomer.  # noqa: E501
        :type: datetime
        """

        self._modified_date = modified_date

    @property
    def source_modified_date(self):
        """Gets the source_modified_date of this CodatDataContractsDatasetsCustomer.  # noqa: E501


        :return: The source_modified_date of this CodatDataContractsDatasetsCustomer.  # noqa: E501
        :rtype: datetime
        """
        return self._source_modified_date

    @source_modified_date.setter
    def source_modified_date(self, source_modified_date):
        """Sets the source_modified_date of this CodatDataContractsDatasetsCustomer.


        :param source_modified_date: The source_modified_date of this CodatDataContractsDatasetsCustomer.  # noqa: E501
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
        if issubclass(CodatDataContractsDatasetsCustomer, dict):
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
        if not isinstance(other, CodatDataContractsDatasetsCustomer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
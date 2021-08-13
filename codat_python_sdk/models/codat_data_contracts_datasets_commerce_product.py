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

class CodatDataContractsDatasetsCommerceProduct(object):
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
        'categorization': 'str',
        'name': 'str',
        'description': 'str',
        'is_gift_card': 'bool',
        'variants': 'list[CodatDataContractsDatasetsCommerceProductVariant]',
        'created_date': 'datetime',
        'modified_date': 'datetime',
        'source_modified_date': 'datetime',
        'status': 'CodatDataContractsDatasetsCommerceProductStatus'
    }

    attribute_map = {
        'id': 'id',
        'categorization': 'categorization',
        'name': 'name',
        'description': 'description',
        'is_gift_card': 'isGiftCard',
        'variants': 'variants',
        'created_date': 'createdDate',
        'modified_date': 'modifiedDate',
        'source_modified_date': 'sourceModifiedDate',
        'status': 'status'
    }

    def __init__(self, id=None, categorization=None, name=None, description=None, is_gift_card=None, variants=None, created_date=None, modified_date=None, source_modified_date=None, status=None):  # noqa: E501
        """CodatDataContractsDatasetsCommerceProduct - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._categorization = None
        self._name = None
        self._description = None
        self._is_gift_card = None
        self._variants = None
        self._created_date = None
        self._modified_date = None
        self._source_modified_date = None
        self._status = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if categorization is not None:
            self.categorization = categorization
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if is_gift_card is not None:
            self.is_gift_card = is_gift_card
        if variants is not None:
            self.variants = variants
        if created_date is not None:
            self.created_date = created_date
        if modified_date is not None:
            self.modified_date = modified_date
        if source_modified_date is not None:
            self.source_modified_date = source_modified_date
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this CodatDataContractsDatasetsCommerceProduct.  # noqa: E501


        :return: The id of this CodatDataContractsDatasetsCommerceProduct.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CodatDataContractsDatasetsCommerceProduct.


        :param id: The id of this CodatDataContractsDatasetsCommerceProduct.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def categorization(self):
        """Gets the categorization of this CodatDataContractsDatasetsCommerceProduct.  # noqa: E501


        :return: The categorization of this CodatDataContractsDatasetsCommerceProduct.  # noqa: E501
        :rtype: str
        """
        return self._categorization

    @categorization.setter
    def categorization(self, categorization):
        """Sets the categorization of this CodatDataContractsDatasetsCommerceProduct.


        :param categorization: The categorization of this CodatDataContractsDatasetsCommerceProduct.  # noqa: E501
        :type: str
        """

        self._categorization = categorization

    @property
    def name(self):
        """Gets the name of this CodatDataContractsDatasetsCommerceProduct.  # noqa: E501


        :return: The name of this CodatDataContractsDatasetsCommerceProduct.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CodatDataContractsDatasetsCommerceProduct.


        :param name: The name of this CodatDataContractsDatasetsCommerceProduct.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this CodatDataContractsDatasetsCommerceProduct.  # noqa: E501


        :return: The description of this CodatDataContractsDatasetsCommerceProduct.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CodatDataContractsDatasetsCommerceProduct.


        :param description: The description of this CodatDataContractsDatasetsCommerceProduct.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def is_gift_card(self):
        """Gets the is_gift_card of this CodatDataContractsDatasetsCommerceProduct.  # noqa: E501


        :return: The is_gift_card of this CodatDataContractsDatasetsCommerceProduct.  # noqa: E501
        :rtype: bool
        """
        return self._is_gift_card

    @is_gift_card.setter
    def is_gift_card(self, is_gift_card):
        """Sets the is_gift_card of this CodatDataContractsDatasetsCommerceProduct.


        :param is_gift_card: The is_gift_card of this CodatDataContractsDatasetsCommerceProduct.  # noqa: E501
        :type: bool
        """

        self._is_gift_card = is_gift_card

    @property
    def variants(self):
        """Gets the variants of this CodatDataContractsDatasetsCommerceProduct.  # noqa: E501


        :return: The variants of this CodatDataContractsDatasetsCommerceProduct.  # noqa: E501
        :rtype: list[CodatDataContractsDatasetsCommerceProductVariant]
        """
        return self._variants

    @variants.setter
    def variants(self, variants):
        """Sets the variants of this CodatDataContractsDatasetsCommerceProduct.


        :param variants: The variants of this CodatDataContractsDatasetsCommerceProduct.  # noqa: E501
        :type: list[CodatDataContractsDatasetsCommerceProductVariant]
        """

        self._variants = variants

    @property
    def created_date(self):
        """Gets the created_date of this CodatDataContractsDatasetsCommerceProduct.  # noqa: E501


        :return: The created_date of this CodatDataContractsDatasetsCommerceProduct.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this CodatDataContractsDatasetsCommerceProduct.


        :param created_date: The created_date of this CodatDataContractsDatasetsCommerceProduct.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def modified_date(self):
        """Gets the modified_date of this CodatDataContractsDatasetsCommerceProduct.  # noqa: E501


        :return: The modified_date of this CodatDataContractsDatasetsCommerceProduct.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """Sets the modified_date of this CodatDataContractsDatasetsCommerceProduct.


        :param modified_date: The modified_date of this CodatDataContractsDatasetsCommerceProduct.  # noqa: E501
        :type: datetime
        """

        self._modified_date = modified_date

    @property
    def source_modified_date(self):
        """Gets the source_modified_date of this CodatDataContractsDatasetsCommerceProduct.  # noqa: E501


        :return: The source_modified_date of this CodatDataContractsDatasetsCommerceProduct.  # noqa: E501
        :rtype: datetime
        """
        return self._source_modified_date

    @source_modified_date.setter
    def source_modified_date(self, source_modified_date):
        """Sets the source_modified_date of this CodatDataContractsDatasetsCommerceProduct.


        :param source_modified_date: The source_modified_date of this CodatDataContractsDatasetsCommerceProduct.  # noqa: E501
        :type: datetime
        """

        self._source_modified_date = source_modified_date

    @property
    def status(self):
        """Gets the status of this CodatDataContractsDatasetsCommerceProduct.  # noqa: E501


        :return: The status of this CodatDataContractsDatasetsCommerceProduct.  # noqa: E501
        :rtype: CodatDataContractsDatasetsCommerceProductStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CodatDataContractsDatasetsCommerceProduct.


        :param status: The status of this CodatDataContractsDatasetsCommerceProduct.  # noqa: E501
        :type: CodatDataContractsDatasetsCommerceProductStatus
        """

        self._status = status

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
        if issubclass(CodatDataContractsDatasetsCommerceProduct, dict):
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
        if not isinstance(other, CodatDataContractsDatasetsCommerceProduct):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
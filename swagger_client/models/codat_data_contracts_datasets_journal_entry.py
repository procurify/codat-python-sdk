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

class CodatDataContractsDatasetsJournalEntry(object):
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
        'posted_on': 'datetime',
        'created_on': 'datetime',
        'updated_on': 'datetime',
        'journal_lines': 'list[CodatDataContractsDatasetsJournalLine]',
        'modified_date': 'datetime',
        'source_modified_date': 'datetime',
        'record_ref': 'CodatDataContractsDatasetsRecordRef'
    }

    attribute_map = {
        'id': 'id',
        'posted_on': 'postedOn',
        'created_on': 'createdOn',
        'updated_on': 'updatedOn',
        'journal_lines': 'journalLines',
        'modified_date': 'modifiedDate',
        'source_modified_date': 'sourceModifiedDate',
        'record_ref': 'recordRef'
    }

    def __init__(self, id=None, posted_on=None, created_on=None, updated_on=None, journal_lines=None, modified_date=None, source_modified_date=None, record_ref=None):  # noqa: E501
        """CodatDataContractsDatasetsJournalEntry - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._posted_on = None
        self._created_on = None
        self._updated_on = None
        self._journal_lines = None
        self._modified_date = None
        self._source_modified_date = None
        self._record_ref = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if posted_on is not None:
            self.posted_on = posted_on
        if created_on is not None:
            self.created_on = created_on
        if updated_on is not None:
            self.updated_on = updated_on
        if journal_lines is not None:
            self.journal_lines = journal_lines
        if modified_date is not None:
            self.modified_date = modified_date
        if source_modified_date is not None:
            self.source_modified_date = source_modified_date
        if record_ref is not None:
            self.record_ref = record_ref

    @property
    def id(self):
        """Gets the id of this CodatDataContractsDatasetsJournalEntry.  # noqa: E501


        :return: The id of this CodatDataContractsDatasetsJournalEntry.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CodatDataContractsDatasetsJournalEntry.


        :param id: The id of this CodatDataContractsDatasetsJournalEntry.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def posted_on(self):
        """Gets the posted_on of this CodatDataContractsDatasetsJournalEntry.  # noqa: E501


        :return: The posted_on of this CodatDataContractsDatasetsJournalEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._posted_on

    @posted_on.setter
    def posted_on(self, posted_on):
        """Sets the posted_on of this CodatDataContractsDatasetsJournalEntry.


        :param posted_on: The posted_on of this CodatDataContractsDatasetsJournalEntry.  # noqa: E501
        :type: datetime
        """

        self._posted_on = posted_on

    @property
    def created_on(self):
        """Gets the created_on of this CodatDataContractsDatasetsJournalEntry.  # noqa: E501


        :return: The created_on of this CodatDataContractsDatasetsJournalEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this CodatDataContractsDatasetsJournalEntry.


        :param created_on: The created_on of this CodatDataContractsDatasetsJournalEntry.  # noqa: E501
        :type: datetime
        """

        self._created_on = created_on

    @property
    def updated_on(self):
        """Gets the updated_on of this CodatDataContractsDatasetsJournalEntry.  # noqa: E501


        :return: The updated_on of this CodatDataContractsDatasetsJournalEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """Sets the updated_on of this CodatDataContractsDatasetsJournalEntry.


        :param updated_on: The updated_on of this CodatDataContractsDatasetsJournalEntry.  # noqa: E501
        :type: datetime
        """

        self._updated_on = updated_on

    @property
    def journal_lines(self):
        """Gets the journal_lines of this CodatDataContractsDatasetsJournalEntry.  # noqa: E501


        :return: The journal_lines of this CodatDataContractsDatasetsJournalEntry.  # noqa: E501
        :rtype: list[CodatDataContractsDatasetsJournalLine]
        """
        return self._journal_lines

    @journal_lines.setter
    def journal_lines(self, journal_lines):
        """Sets the journal_lines of this CodatDataContractsDatasetsJournalEntry.


        :param journal_lines: The journal_lines of this CodatDataContractsDatasetsJournalEntry.  # noqa: E501
        :type: list[CodatDataContractsDatasetsJournalLine]
        """

        self._journal_lines = journal_lines

    @property
    def modified_date(self):
        """Gets the modified_date of this CodatDataContractsDatasetsJournalEntry.  # noqa: E501


        :return: The modified_date of this CodatDataContractsDatasetsJournalEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """Sets the modified_date of this CodatDataContractsDatasetsJournalEntry.


        :param modified_date: The modified_date of this CodatDataContractsDatasetsJournalEntry.  # noqa: E501
        :type: datetime
        """

        self._modified_date = modified_date

    @property
    def source_modified_date(self):
        """Gets the source_modified_date of this CodatDataContractsDatasetsJournalEntry.  # noqa: E501


        :return: The source_modified_date of this CodatDataContractsDatasetsJournalEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._source_modified_date

    @source_modified_date.setter
    def source_modified_date(self, source_modified_date):
        """Sets the source_modified_date of this CodatDataContractsDatasetsJournalEntry.


        :param source_modified_date: The source_modified_date of this CodatDataContractsDatasetsJournalEntry.  # noqa: E501
        :type: datetime
        """

        self._source_modified_date = source_modified_date

    @property
    def record_ref(self):
        """Gets the record_ref of this CodatDataContractsDatasetsJournalEntry.  # noqa: E501


        :return: The record_ref of this CodatDataContractsDatasetsJournalEntry.  # noqa: E501
        :rtype: CodatDataContractsDatasetsRecordRef
        """
        return self._record_ref

    @record_ref.setter
    def record_ref(self, record_ref):
        """Sets the record_ref of this CodatDataContractsDatasetsJournalEntry.


        :param record_ref: The record_ref of this CodatDataContractsDatasetsJournalEntry.  # noqa: E501
        :type: CodatDataContractsDatasetsRecordRef
        """

        self._record_ref = record_ref

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
        if issubclass(CodatDataContractsDatasetsJournalEntry, dict):
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
        if not isinstance(other, CodatDataContractsDatasetsJournalEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

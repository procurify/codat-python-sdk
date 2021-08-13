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

class CodatDataContractsDatasetsBillPushOperation(object):
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
        'data': 'CodatDataContractsDatasetsBill',
        'data_type': 'str',
        'company_id': 'str',
        'push_operation_key': 'str',
        'data_connection_key': 'str',
        'requested_on_utc': 'datetime',
        'completed_on_utc': 'datetime',
        'timeout_in_minutes': 'int',
        'timeout_in_seconds': 'int',
        'status': 'str',
        'error_message': 'str',
        'validation': 'CodatDataContractsValidationValidationResult',
        'status_code': 'int'
    }

    attribute_map = {
        'data': 'data',
        'data_type': 'dataType',
        'company_id': 'companyId',
        'push_operation_key': 'pushOperationKey',
        'data_connection_key': 'dataConnectionKey',
        'requested_on_utc': 'requestedOnUtc',
        'completed_on_utc': 'completedOnUtc',
        'timeout_in_minutes': 'timeoutInMinutes',
        'timeout_in_seconds': 'timeoutInSeconds',
        'status': 'status',
        'error_message': 'errorMessage',
        'validation': 'validation',
        'status_code': 'statusCode'
    }

    def __init__(self, data=None, data_type=None, company_id=None, push_operation_key=None, data_connection_key=None, requested_on_utc=None, completed_on_utc=None, timeout_in_minutes=None, timeout_in_seconds=None, status=None, error_message=None, validation=None, status_code=None):  # noqa: E501
        """CodatDataContractsDatasetsBillPushOperation - a model defined in Swagger"""  # noqa: E501
        self._data = None
        self._data_type = None
        self._company_id = None
        self._push_operation_key = None
        self._data_connection_key = None
        self._requested_on_utc = None
        self._completed_on_utc = None
        self._timeout_in_minutes = None
        self._timeout_in_seconds = None
        self._status = None
        self._error_message = None
        self._validation = None
        self._status_code = None
        self.discriminator = None
        if data is not None:
            self.data = data
        if data_type is not None:
            self.data_type = data_type
        self.company_id = company_id
        self.push_operation_key = push_operation_key
        self.data_connection_key = data_connection_key
        self.requested_on_utc = requested_on_utc
        if completed_on_utc is not None:
            self.completed_on_utc = completed_on_utc
        if timeout_in_minutes is not None:
            self.timeout_in_minutes = timeout_in_minutes
        if timeout_in_seconds is not None:
            self.timeout_in_seconds = timeout_in_seconds
        self.status = status
        if error_message is not None:
            self.error_message = error_message
        if validation is not None:
            self.validation = validation
        self.status_code = status_code

    @property
    def data(self):
        """Gets the data of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501


        :return: The data of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501
        :rtype: CodatDataContractsDatasetsBill
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CodatDataContractsDatasetsBillPushOperation.


        :param data: The data of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501
        :type: CodatDataContractsDatasetsBill
        """

        self._data = data

    @property
    def data_type(self):
        """Gets the data_type of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501


        :return: The data_type of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this CodatDataContractsDatasetsBillPushOperation.


        :param data_type: The data_type of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501
        :type: str
        """

        self._data_type = data_type

    @property
    def company_id(self):
        """Gets the company_id of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501


        :return: The company_id of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this CodatDataContractsDatasetsBillPushOperation.


        :param company_id: The company_id of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501
        :type: str
        """
        if company_id is None:
            raise ValueError("Invalid value for `company_id`, must not be `None`")  # noqa: E501

        self._company_id = company_id

    @property
    def push_operation_key(self):
        """Gets the push_operation_key of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501


        :return: The push_operation_key of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501
        :rtype: str
        """
        return self._push_operation_key

    @push_operation_key.setter
    def push_operation_key(self, push_operation_key):
        """Sets the push_operation_key of this CodatDataContractsDatasetsBillPushOperation.


        :param push_operation_key: The push_operation_key of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501
        :type: str
        """
        if push_operation_key is None:
            raise ValueError("Invalid value for `push_operation_key`, must not be `None`")  # noqa: E501

        self._push_operation_key = push_operation_key

    @property
    def data_connection_key(self):
        """Gets the data_connection_key of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501


        :return: The data_connection_key of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501
        :rtype: str
        """
        return self._data_connection_key

    @data_connection_key.setter
    def data_connection_key(self, data_connection_key):
        """Sets the data_connection_key of this CodatDataContractsDatasetsBillPushOperation.


        :param data_connection_key: The data_connection_key of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501
        :type: str
        """
        if data_connection_key is None:
            raise ValueError("Invalid value for `data_connection_key`, must not be `None`")  # noqa: E501

        self._data_connection_key = data_connection_key

    @property
    def requested_on_utc(self):
        """Gets the requested_on_utc of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501


        :return: The requested_on_utc of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501
        :rtype: datetime
        """
        return self._requested_on_utc

    @requested_on_utc.setter
    def requested_on_utc(self, requested_on_utc):
        """Sets the requested_on_utc of this CodatDataContractsDatasetsBillPushOperation.


        :param requested_on_utc: The requested_on_utc of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501
        :type: datetime
        """
        if requested_on_utc is None:
            raise ValueError("Invalid value for `requested_on_utc`, must not be `None`")  # noqa: E501

        self._requested_on_utc = requested_on_utc

    @property
    def completed_on_utc(self):
        """Gets the completed_on_utc of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501


        :return: The completed_on_utc of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501
        :rtype: datetime
        """
        return self._completed_on_utc

    @completed_on_utc.setter
    def completed_on_utc(self, completed_on_utc):
        """Sets the completed_on_utc of this CodatDataContractsDatasetsBillPushOperation.


        :param completed_on_utc: The completed_on_utc of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501
        :type: datetime
        """

        self._completed_on_utc = completed_on_utc

    @property
    def timeout_in_minutes(self):
        """Gets the timeout_in_minutes of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501


        :return: The timeout_in_minutes of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501
        :rtype: int
        """
        return self._timeout_in_minutes

    @timeout_in_minutes.setter
    def timeout_in_minutes(self, timeout_in_minutes):
        """Sets the timeout_in_minutes of this CodatDataContractsDatasetsBillPushOperation.


        :param timeout_in_minutes: The timeout_in_minutes of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501
        :type: int
        """

        self._timeout_in_minutes = timeout_in_minutes

    @property
    def timeout_in_seconds(self):
        """Gets the timeout_in_seconds of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501


        :return: The timeout_in_seconds of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501
        :rtype: int
        """
        return self._timeout_in_seconds

    @timeout_in_seconds.setter
    def timeout_in_seconds(self, timeout_in_seconds):
        """Sets the timeout_in_seconds of this CodatDataContractsDatasetsBillPushOperation.


        :param timeout_in_seconds: The timeout_in_seconds of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501
        :type: int
        """

        self._timeout_in_seconds = timeout_in_seconds

    @property
    def status(self):
        """Gets the status of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501


        :return: The status of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CodatDataContractsDatasetsBillPushOperation.


        :param status: The status of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def error_message(self):
        """Gets the error_message of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501


        :return: The error_message of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this CodatDataContractsDatasetsBillPushOperation.


        :param error_message: The error_message of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def validation(self):
        """Gets the validation of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501


        :return: The validation of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501
        :rtype: CodatDataContractsValidationValidationResult
        """
        return self._validation

    @validation.setter
    def validation(self, validation):
        """Sets the validation of this CodatDataContractsDatasetsBillPushOperation.


        :param validation: The validation of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501
        :type: CodatDataContractsValidationValidationResult
        """

        self._validation = validation

    @property
    def status_code(self):
        """Gets the status_code of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501


        :return: The status_code of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this CodatDataContractsDatasetsBillPushOperation.


        :param status_code: The status_code of this CodatDataContractsDatasetsBillPushOperation.  # noqa: E501
        :type: int
        """
        if status_code is None:
            raise ValueError("Invalid value for `status_code`, must not be `None`")  # noqa: E501

        self._status_code = status_code

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
        if issubclass(CodatDataContractsDatasetsBillPushOperation, dict):
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
        if not isinstance(other, CodatDataContractsDatasetsBillPushOperation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

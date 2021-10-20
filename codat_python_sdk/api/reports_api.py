"""
    Codat API

    [What's changed in our Swagger](https://docs.codat.io/docs/new-swagger-ui)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from codat_python_sdk.api_client import ApiClient, Endpoint as _Endpoint
from codat_python_sdk.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from codat_python_sdk.model.codat_data_contracts_datasets_aged_creditor_outstanding_i_collection_report import CodatDataContractsDatasetsAgedCreditorOutstandingICollectionReport
from codat_python_sdk.model.codat_data_contracts_datasets_aged_debtor_outstanding_i_collection_report import CodatDataContractsDatasetsAgedDebtorOutstandingICollectionReport
from codat_python_sdk.model.codat_public_api_models_company_company_event_stream import CodatPublicApiModelsCompanyCompanyEventStream


class ReportsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __companies_company_id_reports_aged_creditor_available_get(
            self,
            company_id,
            **kwargs
        ):
            """companies_company_id_reports_aged_creditor_available_get  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.companies_company_id_reports_aged_creditor_available_get(company_id, async_req=True)
            >>> result = thread.get()

            Args:
                company_id (str):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                bool
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['company_id'] = \
                company_id
            return self.call_with_http_info(**kwargs)

        self.companies_company_id_reports_aged_creditor_available_get = _Endpoint(
            settings={
                'response_type': (bool,),
                'auth': [
                    'API Key Auth',
                    'Codat Login'
                ],
                'endpoint_path': '/companies/{companyId}/reports/agedCreditor/available',
                'operation_id': 'companies_company_id_reports_aged_creditor_available_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                ],
                'required': [
                    'company_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'company_id':
                        (str,),
                },
                'attribute_map': {
                    'company_id': 'companyId',
                },
                'location_map': {
                    'company_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__companies_company_id_reports_aged_creditor_available_get
        )

        def __companies_company_id_reports_aged_creditor_get(
            self,
            company_id,
            **kwargs
        ):
            """Gets the aged creditor report for a company.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.companies_company_id_reports_aged_creditor_get(company_id, async_req=True)
            >>> result = thread.get()

            Args:
                company_id (str):

            Keyword Args:
                report_date (datetime): [optional]
                number_of_periods (int): [optional]
                period_length_days (int): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                CodatDataContractsDatasetsAgedCreditorOutstandingICollectionReport
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['company_id'] = \
                company_id
            return self.call_with_http_info(**kwargs)

        self.companies_company_id_reports_aged_creditor_get = _Endpoint(
            settings={
                'response_type': (CodatDataContractsDatasetsAgedCreditorOutstandingICollectionReport,),
                'auth': [
                    'API Key Auth',
                    'Codat Login'
                ],
                'endpoint_path': '/companies/{companyId}/reports/agedCreditor',
                'operation_id': 'companies_company_id_reports_aged_creditor_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'report_date',
                    'number_of_periods',
                    'period_length_days',
                ],
                'required': [
                    'company_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'company_id':
                        (str,),
                    'report_date':
                        (datetime,),
                    'number_of_periods':
                        (int,),
                    'period_length_days':
                        (int,),
                },
                'attribute_map': {
                    'company_id': 'companyId',
                    'report_date': 'reportDate',
                    'number_of_periods': 'numberOfPeriods',
                    'period_length_days': 'periodLengthDays',
                },
                'location_map': {
                    'company_id': 'path',
                    'report_date': 'query',
                    'number_of_periods': 'query',
                    'period_length_days': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__companies_company_id_reports_aged_creditor_get
        )

        def __companies_company_id_reports_aged_debtor_available_get(
            self,
            company_id,
            **kwargs
        ):
            """companies_company_id_reports_aged_debtor_available_get  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.companies_company_id_reports_aged_debtor_available_get(company_id, async_req=True)
            >>> result = thread.get()

            Args:
                company_id (str):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                bool
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['company_id'] = \
                company_id
            return self.call_with_http_info(**kwargs)

        self.companies_company_id_reports_aged_debtor_available_get = _Endpoint(
            settings={
                'response_type': (bool,),
                'auth': [
                    'API Key Auth',
                    'Codat Login'
                ],
                'endpoint_path': '/companies/{companyId}/reports/agedDebtor/available',
                'operation_id': 'companies_company_id_reports_aged_debtor_available_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                ],
                'required': [
                    'company_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'company_id':
                        (str,),
                },
                'attribute_map': {
                    'company_id': 'companyId',
                },
                'location_map': {
                    'company_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__companies_company_id_reports_aged_debtor_available_get
        )

        def __companies_company_id_reports_aged_debtor_get(
            self,
            company_id,
            **kwargs
        ):
            """Gets the aged debtor report for a company.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.companies_company_id_reports_aged_debtor_get(company_id, async_req=True)
            >>> result = thread.get()

            Args:
                company_id (str):

            Keyword Args:
                report_date (datetime): [optional]
                number_of_periods (int): [optional]
                period_length_days (int): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                CodatDataContractsDatasetsAgedDebtorOutstandingICollectionReport
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['company_id'] = \
                company_id
            return self.call_with_http_info(**kwargs)

        self.companies_company_id_reports_aged_debtor_get = _Endpoint(
            settings={
                'response_type': (CodatDataContractsDatasetsAgedDebtorOutstandingICollectionReport,),
                'auth': [
                    'API Key Auth',
                    'Codat Login'
                ],
                'endpoint_path': '/companies/{companyId}/reports/agedDebtor',
                'operation_id': 'companies_company_id_reports_aged_debtor_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'report_date',
                    'number_of_periods',
                    'period_length_days',
                ],
                'required': [
                    'company_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'company_id':
                        (str,),
                    'report_date':
                        (datetime,),
                    'number_of_periods':
                        (int,),
                    'period_length_days':
                        (int,),
                },
                'attribute_map': {
                    'company_id': 'companyId',
                    'report_date': 'reportDate',
                    'number_of_periods': 'numberOfPeriods',
                    'period_length_days': 'periodLengthDays',
                },
                'location_map': {
                    'company_id': 'path',
                    'report_date': 'query',
                    'number_of_periods': 'query',
                    'period_length_days': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__companies_company_id_reports_aged_debtor_get
        )

        def __companies_company_id_reports_events_get(
            self,
            company_id,
            **kwargs
        ):
            """companies_company_id_reports_events_get  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.companies_company_id_reports_events_get(company_id, async_req=True)
            >>> result = thread.get()

            Args:
                company_id (str):

            Keyword Args:
                from_date (datetime): [optional]
                to_date (datetime): [optional]
                page_size (int): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                CodatPublicApiModelsCompanyCompanyEventStream
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['company_id'] = \
                company_id
            return self.call_with_http_info(**kwargs)

        self.companies_company_id_reports_events_get = _Endpoint(
            settings={
                'response_type': (CodatPublicApiModelsCompanyCompanyEventStream,),
                'auth': [
                    'API Key Auth',
                    'Codat Login'
                ],
                'endpoint_path': '/companies/{companyId}/reports/events',
                'operation_id': 'companies_company_id_reports_events_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'from_date',
                    'to_date',
                    'page_size',
                ],
                'required': [
                    'company_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'company_id':
                        (str,),
                    'from_date':
                        (datetime,),
                    'to_date':
                        (datetime,),
                    'page_size':
                        (int,),
                },
                'attribute_map': {
                    'company_id': 'companyId',
                    'from_date': 'fromDate',
                    'to_date': 'toDate',
                    'page_size': 'pageSize',
                },
                'location_map': {
                    'company_id': 'path',
                    'from_date': 'query',
                    'to_date': 'query',
                    'page_size': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__companies_company_id_reports_events_get
        )

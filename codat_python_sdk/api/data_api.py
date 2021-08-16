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
from codat_python_sdk.model.codat_public_api_models_data_data_set import CodatPublicApiModelsDataDataSet
from codat_python_sdk.model.codat_public_api_models_data_data_set_paged_response_model import CodatPublicApiModelsDataDataSetPagedResponseModel


class DataApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __companies_company_id_data_all_post(
            self,
            company_id,
            **kwargs
        ):
            """Initiates the process of capturing a new data snapshot for a company  # noqa: E501

            Initiates the synchronisation for all possible data types supported by the linked data sources  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.companies_company_id_data_all_post(company_id, async_req=True)
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
                None
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

        self.companies_company_id_data_all_post = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'API Key Auth'
                ],
                'endpoint_path': '/companies/{companyId}/data/all',
                'operation_id': 'companies_company_id_data_all_post',
                'http_method': 'POST',
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
                'accept': [],
                'content_type': [],
            },
            api_client=api_client,
            callable=__companies_company_id_data_all_post
        )

        def __companies_company_id_data_history_dataset_id_get(
            self,
            company_id,
            dataset_id,
            **kwargs
        ):
            """Fetch metadata on a single data synchronisation  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.companies_company_id_data_history_dataset_id_get(company_id, dataset_id, async_req=True)
            >>> result = thread.get()

            Args:
                company_id (str):
                dataset_id (str):

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
                CodatPublicApiModelsDataDataSet
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
            kwargs['dataset_id'] = \
                dataset_id
            return self.call_with_http_info(**kwargs)

        self.companies_company_id_data_history_dataset_id_get = _Endpoint(
            settings={
                'response_type': (CodatPublicApiModelsDataDataSet,),
                'auth': [
                    'API Key Auth'
                ],
                'endpoint_path': '/companies/{companyId}/data/history/{datasetId}',
                'operation_id': 'companies_company_id_data_history_dataset_id_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'dataset_id',
                ],
                'required': [
                    'company_id',
                    'dataset_id',
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
                    'dataset_id':
                        (str,),
                },
                'attribute_map': {
                    'company_id': 'companyId',
                    'dataset_id': 'datasetId',
                },
                'location_map': {
                    'company_id': 'path',
                    'dataset_id': 'path',
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
            callable=__companies_company_id_data_history_dataset_id_get
        )

        def __companies_company_id_data_history_get(
            self,
            company_id,
            page=1,
            **kwargs
        ):
            """Fetch a list of all data snapshots captured for a company  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.companies_company_id_data_history_get(company_id, page=1, async_req=True)
            >>> result = thread.get()

            Args:
                company_id (str):
                page (int): defaults to 1, must be one of [1]

            Keyword Args:
                page_size (int): [optional] if omitted the server will use the default value of 100
                query (str): [optional]
                order_by (str): [optional]
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
                CodatPublicApiModelsDataDataSetPagedResponseModel
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
            kwargs['page'] = \
                page
            return self.call_with_http_info(**kwargs)

        self.companies_company_id_data_history_get = _Endpoint(
            settings={
                'response_type': (CodatPublicApiModelsDataDataSetPagedResponseModel,),
                'auth': [
                    'API Key Auth'
                ],
                'endpoint_path': '/companies/{companyId}/data/history',
                'operation_id': 'companies_company_id_data_history_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'page',
                    'page_size',
                    'query',
                    'order_by',
                ],
                'required': [
                    'company_id',
                    'page',
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
                    'page':
                        (int,),
                    'page_size':
                        (int,),
                    'query':
                        (str,),
                    'order_by':
                        (str,),
                },
                'attribute_map': {
                    'company_id': 'companyId',
                    'page': 'page',
                    'page_size': 'pageSize',
                    'query': 'query',
                    'order_by': 'orderBy',
                },
                'location_map': {
                    'company_id': 'path',
                    'page': 'query',
                    'page_size': 'query',
                    'query': 'query',
                    'order_by': 'query',
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
            callable=__companies_company_id_data_history_get
        )

        def __companies_company_id_data_queue_data_type_post(
            self,
            company_id,
            data_type,
            **kwargs
        ):
            """Initiates the process of capturing a data snapshot of a specified type for a company  # noqa: E501

            Initiates the synchronisation for a specified data type  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.companies_company_id_data_queue_data_type_post(company_id, data_type, async_req=True)
            >>> result = thread.get()

            Args:
                company_id (str):
                data_type (str):

            Keyword Args:
                connection_id (str): [optional]
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
                CodatPublicApiModelsDataDataSet
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
            kwargs['data_type'] = \
                data_type
            return self.call_with_http_info(**kwargs)

        self.companies_company_id_data_queue_data_type_post = _Endpoint(
            settings={
                'response_type': (CodatPublicApiModelsDataDataSet,),
                'auth': [
                    'API Key Auth'
                ],
                'endpoint_path': '/companies/{companyId}/data/queue/{dataType}',
                'operation_id': 'companies_company_id_data_queue_data_type_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'data_type',
                    'connection_id',
                ],
                'required': [
                    'company_id',
                    'data_type',
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
                    'data_type':
                        (str,),
                    'connection_id':
                        (str,),
                },
                'attribute_map': {
                    'company_id': 'companyId',
                    'data_type': 'dataType',
                    'connection_id': 'connectionId',
                },
                'location_map': {
                    'company_id': 'path',
                    'data_type': 'path',
                    'connection_id': 'query',
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
            callable=__companies_company_id_data_queue_data_type_post
        )

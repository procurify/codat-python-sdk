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
from codat_python_sdk.model.codat_data_contracts_push_push_option import CodatDataContractsPushPushOption
from codat_python_sdk.model.system_object_push_operation import SystemObjectPushOperation
from codat_python_sdk.model.system_object_push_operation_paged_response_model import SystemObjectPushOperationPagedResponseModel


class PushApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __companies_company_id_connections_connection_id_options_data_type_get(
            self,
            company_id,
            connection_id,
            data_type,
            **kwargs
        ):
            """Gets the push options for the given data type  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.companies_company_id_connections_connection_id_options_data_type_get(company_id, connection_id, data_type, async_req=True)
            >>> result = thread.get()

            Args:
                company_id (str):
                connection_id (str):
                data_type (str):

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
                CodatDataContractsPushPushOption
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
            kwargs['connection_id'] = \
                connection_id
            kwargs['data_type'] = \
                data_type
            return self.call_with_http_info(**kwargs)

        self.companies_company_id_connections_connection_id_options_data_type_get = _Endpoint(
            settings={
                'response_type': (CodatDataContractsPushPushOption,),
                'auth': [
                    'API Key Auth',
                    'Codat Login'
                ],
                'endpoint_path': '/companies/{companyId}/connections/{connectionId}/options/{dataType}',
                'operation_id': 'companies_company_id_connections_connection_id_options_data_type_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'connection_id',
                    'data_type',
                ],
                'required': [
                    'company_id',
                    'connection_id',
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
                    'connection_id':
                        (str,),
                    'data_type':
                        (str,),
                },
                'attribute_map': {
                    'company_id': 'companyId',
                    'connection_id': 'connectionId',
                    'data_type': 'dataType',
                },
                'location_map': {
                    'company_id': 'path',
                    'connection_id': 'path',
                    'data_type': 'path',
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
            callable=__companies_company_id_connections_connection_id_options_data_type_get
        )

        def __companies_company_id_push_get(
            self,
            company_id,
            page,
            **kwargs
        ):
            """Gets paged push operation records  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.companies_company_id_push_get(company_id, page, async_req=True)
            >>> result = thread.get()

            Args:
                company_id (str): Company Id
                page (int): Page

            Keyword Args:
                page_size (int): Page size. [optional] if omitted the server will use the default value of 100
                query (str): Data query. [optional]
                order_by (str): Order by property (ascending). [optional]
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
                SystemObjectPushOperationPagedResponseModel
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

        self.companies_company_id_push_get = _Endpoint(
            settings={
                'response_type': (SystemObjectPushOperationPagedResponseModel,),
                'auth': [
                    'API Key Auth',
                    'Codat Login'
                ],
                'endpoint_path': '/companies/{companyId}/push',
                'operation_id': 'companies_company_id_push_get',
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
            callable=__companies_company_id_push_get
        )

        def __companies_company_id_push_push_operation_key_get(
            self,
            company_id,
            push_operation_key,
            **kwargs
        ):
            """Gets a single push operation record  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.companies_company_id_push_push_operation_key_get(company_id, push_operation_key, async_req=True)
            >>> result = thread.get()

            Args:
                company_id (str):
                push_operation_key (str):

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
                SystemObjectPushOperation
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
            kwargs['push_operation_key'] = \
                push_operation_key
            return self.call_with_http_info(**kwargs)

        self.companies_company_id_push_push_operation_key_get = _Endpoint(
            settings={
                'response_type': (SystemObjectPushOperation,),
                'auth': [
                    'API Key Auth',
                    'Codat Login'
                ],
                'endpoint_path': '/companies/{companyId}/push/{pushOperationKey}',
                'operation_id': 'companies_company_id_push_push_operation_key_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'push_operation_key',
                ],
                'required': [
                    'company_id',
                    'push_operation_key',
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
                    'push_operation_key':
                        (str,),
                },
                'attribute_map': {
                    'company_id': 'companyId',
                    'push_operation_key': 'pushOperationKey',
                },
                'location_map': {
                    'company_id': 'path',
                    'push_operation_key': 'path',
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
            callable=__companies_company_id_push_push_operation_key_get
        )

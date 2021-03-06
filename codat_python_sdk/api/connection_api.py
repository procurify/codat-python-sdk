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
from codat_python_sdk.model.codat_public_api_models_company_data_connection import CodatPublicApiModelsCompanyDataConnection
from codat_python_sdk.model.codat_public_api_models_company_data_connection_paged_response_model import CodatPublicApiModelsCompanyDataConnectionPagedResponseModel
from codat_python_sdk.model.codat_public_api_models_company_patch_data_connection_model import CodatPublicApiModelsCompanyPatchDataConnectionModel


class ConnectionApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __companies_company_id_connections_connection_id_delete(
            self,
            company_id,
            connection_id,
            **kwargs
        ):
            """Disconnect and delete a data source from a company  # noqa: E501

            This revokes and removes a data connection from being listed as a company's connection(s).  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.companies_company_id_connections_connection_id_delete(company_id, connection_id, async_req=True)
            >>> result = thread.get()

            Args:
                company_id (str):
                connection_id (str):

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
            kwargs['connection_id'] = \
                connection_id
            return self.call_with_http_info(**kwargs)

        self.companies_company_id_connections_connection_id_delete = _Endpoint(
            settings={
                'response_type': (bool,),
                'auth': [
                    'API Key Auth',
                    'Codat Login'
                ],
                'endpoint_path': '/companies/{companyId}/connections/{connectionId}',
                'operation_id': 'companies_company_id_connections_connection_id_delete',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'connection_id',
                ],
                'required': [
                    'company_id',
                    'connection_id',
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
                },
                'attribute_map': {
                    'company_id': 'companyId',
                    'connection_id': 'connectionId',
                },
                'location_map': {
                    'company_id': 'path',
                    'connection_id': 'path',
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
            callable=__companies_company_id_connections_connection_id_delete
        )

        def __companies_company_id_connections_connection_id_get(
            self,
            company_id,
            connection_id,
            **kwargs
        ):
            """Retrieve a single data source connected to a single company, including its connection status  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.companies_company_id_connections_connection_id_get(company_id, connection_id, async_req=True)
            >>> result = thread.get()

            Args:
                company_id (str):
                connection_id (str):

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
                CodatPublicApiModelsCompanyDataConnection
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
            return self.call_with_http_info(**kwargs)

        self.companies_company_id_connections_connection_id_get = _Endpoint(
            settings={
                'response_type': (CodatPublicApiModelsCompanyDataConnection,),
                'auth': [
                    'API Key Auth',
                    'Codat Login'
                ],
                'endpoint_path': '/companies/{companyId}/connections/{connectionId}',
                'operation_id': 'companies_company_id_connections_connection_id_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'connection_id',
                ],
                'required': [
                    'company_id',
                    'connection_id',
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
                },
                'attribute_map': {
                    'company_id': 'companyId',
                    'connection_id': 'connectionId',
                },
                'location_map': {
                    'company_id': 'path',
                    'connection_id': 'path',
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
            callable=__companies_company_id_connections_connection_id_get
        )

        def __companies_company_id_connections_connection_id_patch(
            self,
            company_id,
            connection_id,
            **kwargs
        ):
            """Disconnect a data source from a company  # noqa: E501

            This revokes a company???s access to a data source, but the data connection is still listed as a part of a company's  data connection(s). The status value in the request body should be \"Unlinked\" (case sensitive). Data connections  can only be unlinked if in the Linked or Deauthorized state.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.companies_company_id_connections_connection_id_patch(company_id, connection_id, async_req=True)
            >>> result = thread.get()

            Args:
                company_id (str):
                connection_id (str):

            Keyword Args:
                codat_public_api_models_company_patch_data_connection_model (CodatPublicApiModelsCompanyPatchDataConnectionModel): [optional]
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
                CodatPublicApiModelsCompanyDataConnection
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
            return self.call_with_http_info(**kwargs)

        self.companies_company_id_connections_connection_id_patch = _Endpoint(
            settings={
                'response_type': (CodatPublicApiModelsCompanyDataConnection,),
                'auth': [
                    'API Key Auth',
                    'Codat Login'
                ],
                'endpoint_path': '/companies/{companyId}/connections/{connectionId}',
                'operation_id': 'companies_company_id_connections_connection_id_patch',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'connection_id',
                    'codat_public_api_models_company_patch_data_connection_model',
                ],
                'required': [
                    'company_id',
                    'connection_id',
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
                    'codat_public_api_models_company_patch_data_connection_model':
                        (CodatPublicApiModelsCompanyPatchDataConnectionModel,),
                },
                'attribute_map': {
                    'company_id': 'companyId',
                    'connection_id': 'connectionId',
                },
                'location_map': {
                    'company_id': 'path',
                    'connection_id': 'path',
                    'codat_public_api_models_company_patch_data_connection_model': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__companies_company_id_connections_connection_id_patch
        )

        def __companies_company_id_connections_get(
            self,
            company_id,
            page,
            **kwargs
        ):
            """Retrieve all data sources connected to a single company, including their connection statuses  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.companies_company_id_connections_get(company_id, page, async_req=True)
            >>> result = thread.get()

            Args:
                company_id (str):
                page (int):

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
                CodatPublicApiModelsCompanyDataConnectionPagedResponseModel
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

        self.companies_company_id_connections_get = _Endpoint(
            settings={
                'response_type': (CodatPublicApiModelsCompanyDataConnectionPagedResponseModel,),
                'auth': [
                    'API Key Auth',
                    'Codat Login'
                ],
                'endpoint_path': '/companies/{companyId}/connections',
                'operation_id': 'companies_company_id_connections_get',
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
            callable=__companies_company_id_connections_get
        )

        def __companies_company_id_connections_post(
            self,
            company_id,
            **kwargs
        ):
            """Connect a data source to a company  # noqa: E501

            This creates a new data connection in the PendingAuth state. You can get a list of data connections (platformKeys)  supported by Codat from GET /integrations.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.companies_company_id_connections_post(company_id, async_req=True)
            >>> result = thread.get()

            Args:
                company_id (str):

            Keyword Args:
                body (str): [optional]
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
                CodatPublicApiModelsCompanyDataConnection
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

        self.companies_company_id_connections_post = _Endpoint(
            settings={
                'response_type': (CodatPublicApiModelsCompanyDataConnection,),
                'auth': [
                    'API Key Auth',
                    'Codat Login'
                ],
                'endpoint_path': '/companies/{companyId}/connections',
                'operation_id': 'companies_company_id_connections_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'body',
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
                    'body':
                        (str,),
                },
                'attribute_map': {
                    'company_id': 'companyId',
                },
                'location_map': {
                    'company_id': 'path',
                    'body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__companies_company_id_connections_post
        )

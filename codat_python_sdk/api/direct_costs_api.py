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
from codat_python_sdk.model.codat_data_contracts_datasets_direct_cost import CodatDataContractsDatasetsDirectCost
from codat_python_sdk.model.codat_data_contracts_datasets_direct_cost_paged_response_model import CodatDataContractsDatasetsDirectCostPagedResponseModel
from codat_python_sdk.model.codat_data_contracts_datasets_direct_cost_push_operation import CodatDataContractsDatasetsDirectCostPushOperation


class DirectCostsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __companies_company_id_connections_connection_id_data_direct_costs_direct_cost_id_get(
            self,
            company_id,
            direct_cost_id,
            connection_id,
            **kwargs
        ):
            """Gets the specified direct cost for a given company.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.companies_company_id_connections_connection_id_data_direct_costs_direct_cost_id_get(company_id, direct_cost_id, connection_id, async_req=True)
            >>> result = thread.get()

            Args:
                company_id (str):
                direct_cost_id (str):
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
                CodatDataContractsDatasetsDirectCost
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
            kwargs['direct_cost_id'] = \
                direct_cost_id
            kwargs['connection_id'] = \
                connection_id
            return self.call_with_http_info(**kwargs)

        self.companies_company_id_connections_connection_id_data_direct_costs_direct_cost_id_get = _Endpoint(
            settings={
                'response_type': (CodatDataContractsDatasetsDirectCost,),
                'auth': [
                    'API Key Auth'
                ],
                'endpoint_path': '/companies/{companyId}/connections/{connectionId}/data/directCosts/{directCostId}',
                'operation_id': 'companies_company_id_connections_connection_id_data_direct_costs_direct_cost_id_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'direct_cost_id',
                    'connection_id',
                ],
                'required': [
                    'company_id',
                    'direct_cost_id',
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
                    'direct_cost_id':
                        (str,),
                    'connection_id':
                        (str,),
                },
                'attribute_map': {
                    'company_id': 'companyId',
                    'direct_cost_id': 'directCostId',
                    'connection_id': 'connectionId',
                },
                'location_map': {
                    'company_id': 'path',
                    'direct_cost_id': 'path',
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
            callable=__companies_company_id_connections_connection_id_data_direct_costs_direct_cost_id_get
        )

        def __companies_company_id_connections_connection_id_data_direct_costs_get(
            self,
            company_id,
            connection_id,
            page=1,
            **kwargs
        ):
            """Gets the direct costs for the company.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.companies_company_id_connections_connection_id_data_direct_costs_get(company_id, connection_id, page=1, async_req=True)
            >>> result = thread.get()

            Args:
                company_id (str):
                connection_id (str):
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
                CodatDataContractsDatasetsDirectCostPagedResponseModel
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
            kwargs['page'] = \
                page
            return self.call_with_http_info(**kwargs)

        self.companies_company_id_connections_connection_id_data_direct_costs_get = _Endpoint(
            settings={
                'response_type': (CodatDataContractsDatasetsDirectCostPagedResponseModel,),
                'auth': [
                    'API Key Auth'
                ],
                'endpoint_path': '/companies/{companyId}/connections/{connectionId}/data/directCosts',
                'operation_id': 'companies_company_id_connections_connection_id_data_direct_costs_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'connection_id',
                    'page',
                    'page_size',
                    'query',
                    'order_by',
                ],
                'required': [
                    'company_id',
                    'connection_id',
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
                    'connection_id':
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
                    'connection_id': 'connectionId',
                    'page': 'page',
                    'page_size': 'pageSize',
                    'query': 'query',
                    'order_by': 'orderBy',
                },
                'location_map': {
                    'company_id': 'path',
                    'connection_id': 'path',
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
            callable=__companies_company_id_connections_connection_id_data_direct_costs_get
        )

        def __companies_company_id_connections_connection_id_push_direct_costs_post(
            self,
            company_id,
            connection_id,
            **kwargs
        ):
            """Posts a new direct cost to the accounting package for a given company.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.companies_company_id_connections_connection_id_push_direct_costs_post(company_id, connection_id, async_req=True)
            >>> result = thread.get()

            Args:
                company_id (str):
                connection_id (str):

            Keyword Args:
                timeout_in_minutes (int): [optional]
                codat_data_contracts_datasets_direct_cost (CodatDataContractsDatasetsDirectCost): [optional]
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
                CodatDataContractsDatasetsDirectCostPushOperation
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

        self.companies_company_id_connections_connection_id_push_direct_costs_post = _Endpoint(
            settings={
                'response_type': (CodatDataContractsDatasetsDirectCostPushOperation,),
                'auth': [
                    'API Key Auth'
                ],
                'endpoint_path': '/companies/{companyId}/connections/{connectionId}/push/directCosts',
                'operation_id': 'companies_company_id_connections_connection_id_push_direct_costs_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'connection_id',
                    'timeout_in_minutes',
                    'codat_data_contracts_datasets_direct_cost',
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
                    'timeout_in_minutes':
                        (int,),
                    'codat_data_contracts_datasets_direct_cost':
                        (CodatDataContractsDatasetsDirectCost,),
                },
                'attribute_map': {
                    'company_id': 'companyId',
                    'connection_id': 'connectionId',
                    'timeout_in_minutes': 'timeoutInMinutes',
                },
                'location_map': {
                    'company_id': 'path',
                    'connection_id': 'path',
                    'timeout_in_minutes': 'query',
                    'codat_data_contracts_datasets_direct_cost': 'body',
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
            callable=__companies_company_id_connections_connection_id_push_direct_costs_post
        )

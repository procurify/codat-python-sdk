# coding: utf-8

"""
    Codat API

    [What's changed in our Swagger](https://docs.codat.io/docs/new-swagger-ui)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class DirectCostsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def companies_company_id_connections_connection_id_data_direct_costs_direct_cost_id_get(self, company_id, direct_cost_id, connection_id, **kwargs):  # noqa: E501
        """Gets the specified direct cost for a given company.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.companies_company_id_connections_connection_id_data_direct_costs_direct_cost_id_get(company_id, direct_cost_id, connection_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str company_id: (required)
        :param str direct_cost_id: (required)
        :param str connection_id: (required)
        :return: CodatDataContractsDatasetsDirectCost
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.companies_company_id_connections_connection_id_data_direct_costs_direct_cost_id_get_with_http_info(company_id, direct_cost_id, connection_id, **kwargs)  # noqa: E501
        else:
            (data) = self.companies_company_id_connections_connection_id_data_direct_costs_direct_cost_id_get_with_http_info(company_id, direct_cost_id, connection_id, **kwargs)  # noqa: E501
            return data

    def companies_company_id_connections_connection_id_data_direct_costs_direct_cost_id_get_with_http_info(self, company_id, direct_cost_id, connection_id, **kwargs):  # noqa: E501
        """Gets the specified direct cost for a given company.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.companies_company_id_connections_connection_id_data_direct_costs_direct_cost_id_get_with_http_info(company_id, direct_cost_id, connection_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str company_id: (required)
        :param str direct_cost_id: (required)
        :param str connection_id: (required)
        :return: CodatDataContractsDatasetsDirectCost
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['company_id', 'direct_cost_id', 'connection_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method companies_company_id_connections_connection_id_data_direct_costs_direct_cost_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'company_id' is set
        if ('company_id' not in params or
                params['company_id'] is None):
            raise ValueError("Missing the required parameter `company_id` when calling `companies_company_id_connections_connection_id_data_direct_costs_direct_cost_id_get`")  # noqa: E501
        # verify the required parameter 'direct_cost_id' is set
        if ('direct_cost_id' not in params or
                params['direct_cost_id'] is None):
            raise ValueError("Missing the required parameter `direct_cost_id` when calling `companies_company_id_connections_connection_id_data_direct_costs_direct_cost_id_get`")  # noqa: E501
        # verify the required parameter 'connection_id' is set
        if ('connection_id' not in params or
                params['connection_id'] is None):
            raise ValueError("Missing the required parameter `connection_id` when calling `companies_company_id_connections_connection_id_data_direct_costs_direct_cost_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'company_id' in params:
            path_params['companyId'] = params['company_id']  # noqa: E501
        if 'direct_cost_id' in params:
            path_params['directCostId'] = params['direct_cost_id']  # noqa: E501
        if 'connection_id' in params:
            path_params['connectionId'] = params['connection_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API Key Auth']  # noqa: E501

        return self.api_client.call_api(
            '/companies/{companyId}/connections/{connectionId}/data/directCosts/{directCostId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CodatDataContractsDatasetsDirectCost',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def companies_company_id_connections_connection_id_data_direct_costs_get(self, company_id, connection_id, page, **kwargs):  # noqa: E501
        """Gets the direct costs for the company.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.companies_company_id_connections_connection_id_data_direct_costs_get(company_id, connection_id, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str company_id: (required)
        :param str connection_id: (required)
        :param int page: (required)
        :param int page_size:
        :param str query:
        :param str order_by:
        :return: CodatDataContractsDatasetsDirectCostPagedResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.companies_company_id_connections_connection_id_data_direct_costs_get_with_http_info(company_id, connection_id, page, **kwargs)  # noqa: E501
        else:
            (data) = self.companies_company_id_connections_connection_id_data_direct_costs_get_with_http_info(company_id, connection_id, page, **kwargs)  # noqa: E501
            return data

    def companies_company_id_connections_connection_id_data_direct_costs_get_with_http_info(self, company_id, connection_id, page, **kwargs):  # noqa: E501
        """Gets the direct costs for the company.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.companies_company_id_connections_connection_id_data_direct_costs_get_with_http_info(company_id, connection_id, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str company_id: (required)
        :param str connection_id: (required)
        :param int page: (required)
        :param int page_size:
        :param str query:
        :param str order_by:
        :return: CodatDataContractsDatasetsDirectCostPagedResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['company_id', 'connection_id', 'page', 'page_size', 'query', 'order_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method companies_company_id_connections_connection_id_data_direct_costs_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'company_id' is set
        if ('company_id' not in params or
                params['company_id'] is None):
            raise ValueError("Missing the required parameter `company_id` when calling `companies_company_id_connections_connection_id_data_direct_costs_get`")  # noqa: E501
        # verify the required parameter 'connection_id' is set
        if ('connection_id' not in params or
                params['connection_id'] is None):
            raise ValueError("Missing the required parameter `connection_id` when calling `companies_company_id_connections_connection_id_data_direct_costs_get`")  # noqa: E501
        # verify the required parameter 'page' is set
        if ('page' not in params or
                params['page'] is None):
            raise ValueError("Missing the required parameter `page` when calling `companies_company_id_connections_connection_id_data_direct_costs_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'company_id' in params:
            path_params['companyId'] = params['company_id']  # noqa: E501
        if 'connection_id' in params:
            path_params['connectionId'] = params['connection_id']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('orderBy', params['order_by']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API Key Auth']  # noqa: E501

        return self.api_client.call_api(
            '/companies/{companyId}/connections/{connectionId}/data/directCosts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CodatDataContractsDatasetsDirectCostPagedResponseModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def companies_company_id_connections_connection_id_push_direct_costs_post(self, company_id, connection_id, **kwargs):  # noqa: E501
        """Posts a new direct cost to the accounting package for a given company.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.companies_company_id_connections_connection_id_push_direct_costs_post(company_id, connection_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str company_id: (required)
        :param str connection_id: (required)
        :param CodatDataContractsDatasetsDirectCost body:
        :param int timeout_in_minutes:
        :return: CodatDataContractsDatasetsDirectCostPushOperation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.companies_company_id_connections_connection_id_push_direct_costs_post_with_http_info(company_id, connection_id, **kwargs)  # noqa: E501
        else:
            (data) = self.companies_company_id_connections_connection_id_push_direct_costs_post_with_http_info(company_id, connection_id, **kwargs)  # noqa: E501
            return data

    def companies_company_id_connections_connection_id_push_direct_costs_post_with_http_info(self, company_id, connection_id, **kwargs):  # noqa: E501
        """Posts a new direct cost to the accounting package for a given company.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.companies_company_id_connections_connection_id_push_direct_costs_post_with_http_info(company_id, connection_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str company_id: (required)
        :param str connection_id: (required)
        :param CodatDataContractsDatasetsDirectCost body:
        :param int timeout_in_minutes:
        :return: CodatDataContractsDatasetsDirectCostPushOperation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['company_id', 'connection_id', 'body', 'timeout_in_minutes']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method companies_company_id_connections_connection_id_push_direct_costs_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'company_id' is set
        if ('company_id' not in params or
                params['company_id'] is None):
            raise ValueError("Missing the required parameter `company_id` when calling `companies_company_id_connections_connection_id_push_direct_costs_post`")  # noqa: E501
        # verify the required parameter 'connection_id' is set
        if ('connection_id' not in params or
                params['connection_id'] is None):
            raise ValueError("Missing the required parameter `connection_id` when calling `companies_company_id_connections_connection_id_push_direct_costs_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'company_id' in params:
            path_params['companyId'] = params['company_id']  # noqa: E501
        if 'connection_id' in params:
            path_params['connectionId'] = params['connection_id']  # noqa: E501

        query_params = []
        if 'timeout_in_minutes' in params:
            query_params.append(('timeoutInMinutes', params['timeout_in_minutes']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API Key Auth']  # noqa: E501

        return self.api_client.call_api(
            '/companies/{companyId}/connections/{connectionId}/push/directCosts', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CodatDataContractsDatasetsDirectCostPushOperation',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

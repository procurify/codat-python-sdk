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

from codat_python_sdk.api_client import ApiClient


class BankStatementsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def companies_company_id_data_bank_statements_accounts_get(self, company_id, **kwargs):  # noqa: E501
        """Gets the latest bank statements for a company, with pagination  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.companies_company_id_data_bank_statements_accounts_get(company_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str company_id: (required)
        :param str query:
        :return: list[CodatDataContractsDatasetsBankStatementAccount]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.companies_company_id_data_bank_statements_accounts_get_with_http_info(company_id, **kwargs)  # noqa: E501
        else:
            (data) = self.companies_company_id_data_bank_statements_accounts_get_with_http_info(company_id, **kwargs)  # noqa: E501
            return data

    def companies_company_id_data_bank_statements_accounts_get_with_http_info(self, company_id, **kwargs):  # noqa: E501
        """Gets the latest bank statements for a company, with pagination  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.companies_company_id_data_bank_statements_accounts_get_with_http_info(company_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str company_id: (required)
        :param str query:
        :return: list[CodatDataContractsDatasetsBankStatementAccount]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['company_id', 'query']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method companies_company_id_data_bank_statements_accounts_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'company_id' is set
        if ('company_id' not in params or
                params['company_id'] is None):
            raise ValueError("Missing the required parameter `company_id` when calling `companies_company_id_data_bank_statements_accounts_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'company_id' in params:
            path_params['companyId'] = params['company_id']  # noqa: E501

        query_params = []
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501

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
            '/companies/{companyId}/data/bankStatements/accounts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[CodatDataContractsDatasetsBankStatementAccount]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def companies_company_id_data_bank_statements_get(self, company_id, page, **kwargs):  # noqa: E501
        """Gets the latest bank statements for a company, with pagination  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.companies_company_id_data_bank_statements_get(company_id, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str company_id: (required)
        :param int page: (required)
        :param str account_id:
        :param int page_size:
        :param str query:
        :param str order_by:
        :return: CodatDataContractsDatasetsBankStatementLinePagedResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.companies_company_id_data_bank_statements_get_with_http_info(company_id, page, **kwargs)  # noqa: E501
        else:
            (data) = self.companies_company_id_data_bank_statements_get_with_http_info(company_id, page, **kwargs)  # noqa: E501
            return data

    def companies_company_id_data_bank_statements_get_with_http_info(self, company_id, page, **kwargs):  # noqa: E501
        """Gets the latest bank statements for a company, with pagination  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.companies_company_id_data_bank_statements_get_with_http_info(company_id, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str company_id: (required)
        :param int page: (required)
        :param str account_id:
        :param int page_size:
        :param str query:
        :param str order_by:
        :return: CodatDataContractsDatasetsBankStatementLinePagedResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['company_id', 'page', 'account_id', 'page_size', 'query', 'order_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method companies_company_id_data_bank_statements_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'company_id' is set
        if ('company_id' not in params or
                params['company_id'] is None):
            raise ValueError("Missing the required parameter `company_id` when calling `companies_company_id_data_bank_statements_get`")  # noqa: E501
        # verify the required parameter 'page' is set
        if ('page' not in params or
                params['page'] is None):
            raise ValueError("Missing the required parameter `page` when calling `companies_company_id_data_bank_statements_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'company_id' in params:
            path_params['companyId'] = params['company_id']  # noqa: E501

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
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
            '/companies/{companyId}/data/bankStatements', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CodatDataContractsDatasetsBankStatementLinePagedResponseModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

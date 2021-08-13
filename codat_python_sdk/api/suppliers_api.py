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


class SuppliersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_download_get(self, company_id, connection_id, supplier_id, attachment_id, **kwargs):  # noqa: E501
        """companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_download_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_download_get(company_id, connection_id, supplier_id, attachment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str company_id: (required)
        :param str connection_id: (required)
        :param str supplier_id: (required)
        :param str attachment_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_download_get_with_http_info(company_id, connection_id, supplier_id, attachment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_download_get_with_http_info(company_id, connection_id, supplier_id, attachment_id, **kwargs)  # noqa: E501
            return data

    def companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_download_get_with_http_info(self, company_id, connection_id, supplier_id, attachment_id, **kwargs):  # noqa: E501
        """companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_download_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_download_get_with_http_info(company_id, connection_id, supplier_id, attachment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str company_id: (required)
        :param str connection_id: (required)
        :param str supplier_id: (required)
        :param str attachment_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['company_id', 'connection_id', 'supplier_id', 'attachment_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_download_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'company_id' is set
        if ('company_id' not in params or
                params['company_id'] is None):
            raise ValueError("Missing the required parameter `company_id` when calling `companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_download_get`")  # noqa: E501
        # verify the required parameter 'connection_id' is set
        if ('connection_id' not in params or
                params['connection_id'] is None):
            raise ValueError("Missing the required parameter `connection_id` when calling `companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_download_get`")  # noqa: E501
        # verify the required parameter 'supplier_id' is set
        if ('supplier_id' not in params or
                params['supplier_id'] is None):
            raise ValueError("Missing the required parameter `supplier_id` when calling `companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_download_get`")  # noqa: E501
        # verify the required parameter 'attachment_id' is set
        if ('attachment_id' not in params or
                params['attachment_id'] is None):
            raise ValueError("Missing the required parameter `attachment_id` when calling `companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_download_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'company_id' in params:
            path_params['companyId'] = params['company_id']  # noqa: E501
        if 'connection_id' in params:
            path_params['connectionId'] = params['connection_id']  # noqa: E501
        if 'supplier_id' in params:
            path_params['supplierId'] = params['supplier_id']  # noqa: E501
        if 'attachment_id' in params:
            path_params['attachmentId'] = params['attachment_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['API Key Auth']  # noqa: E501

        return self.api_client.call_api(
            '/companies/{companyId}/connections/{connectionId}/data/suppliers/{supplierId}/attachments/{attachmentId}/download', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_get(self, company_id, connection_id, supplier_id, attachment_id, **kwargs):  # noqa: E501
        """companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_get(company_id, connection_id, supplier_id, attachment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str company_id: (required)
        :param str connection_id: (required)
        :param str supplier_id: (required)
        :param str attachment_id: (required)
        :return: CodatDataContractsDatasetsAttachmentsDatasetAttachment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_get_with_http_info(company_id, connection_id, supplier_id, attachment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_get_with_http_info(company_id, connection_id, supplier_id, attachment_id, **kwargs)  # noqa: E501
            return data

    def companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_get_with_http_info(self, company_id, connection_id, supplier_id, attachment_id, **kwargs):  # noqa: E501
        """companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_get_with_http_info(company_id, connection_id, supplier_id, attachment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str company_id: (required)
        :param str connection_id: (required)
        :param str supplier_id: (required)
        :param str attachment_id: (required)
        :return: CodatDataContractsDatasetsAttachmentsDatasetAttachment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['company_id', 'connection_id', 'supplier_id', 'attachment_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'company_id' is set
        if ('company_id' not in params or
                params['company_id'] is None):
            raise ValueError("Missing the required parameter `company_id` when calling `companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_get`")  # noqa: E501
        # verify the required parameter 'connection_id' is set
        if ('connection_id' not in params or
                params['connection_id'] is None):
            raise ValueError("Missing the required parameter `connection_id` when calling `companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_get`")  # noqa: E501
        # verify the required parameter 'supplier_id' is set
        if ('supplier_id' not in params or
                params['supplier_id'] is None):
            raise ValueError("Missing the required parameter `supplier_id` when calling `companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_get`")  # noqa: E501
        # verify the required parameter 'attachment_id' is set
        if ('attachment_id' not in params or
                params['attachment_id'] is None):
            raise ValueError("Missing the required parameter `attachment_id` when calling `companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'company_id' in params:
            path_params['companyId'] = params['company_id']  # noqa: E501
        if 'connection_id' in params:
            path_params['connectionId'] = params['connection_id']  # noqa: E501
        if 'supplier_id' in params:
            path_params['supplierId'] = params['supplier_id']  # noqa: E501
        if 'attachment_id' in params:
            path_params['attachmentId'] = params['attachment_id']  # noqa: E501

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
            '/companies/{companyId}/connections/{connectionId}/data/suppliers/{supplierId}/attachments/{attachmentId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CodatDataContractsDatasetsAttachmentsDatasetAttachment',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_get(self, company_id, connection_id, supplier_id, **kwargs):  # noqa: E501
        """companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_get(company_id, connection_id, supplier_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str company_id: (required)
        :param str connection_id: (required)
        :param str supplier_id: (required)
        :return: CodatDataContractsDatasetsAttachmentsDataset
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_get_with_http_info(company_id, connection_id, supplier_id, **kwargs)  # noqa: E501
        else:
            (data) = self.companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_get_with_http_info(company_id, connection_id, supplier_id, **kwargs)  # noqa: E501
            return data

    def companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_get_with_http_info(self, company_id, connection_id, supplier_id, **kwargs):  # noqa: E501
        """companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_get_with_http_info(company_id, connection_id, supplier_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str company_id: (required)
        :param str connection_id: (required)
        :param str supplier_id: (required)
        :return: CodatDataContractsDatasetsAttachmentsDataset
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['company_id', 'connection_id', 'supplier_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'company_id' is set
        if ('company_id' not in params or
                params['company_id'] is None):
            raise ValueError("Missing the required parameter `company_id` when calling `companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_get`")  # noqa: E501
        # verify the required parameter 'connection_id' is set
        if ('connection_id' not in params or
                params['connection_id'] is None):
            raise ValueError("Missing the required parameter `connection_id` when calling `companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_get`")  # noqa: E501
        # verify the required parameter 'supplier_id' is set
        if ('supplier_id' not in params or
                params['supplier_id'] is None):
            raise ValueError("Missing the required parameter `supplier_id` when calling `companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'company_id' in params:
            path_params['companyId'] = params['company_id']  # noqa: E501
        if 'connection_id' in params:
            path_params['connectionId'] = params['connection_id']  # noqa: E501
        if 'supplier_id' in params:
            path_params['supplierId'] = params['supplier_id']  # noqa: E501

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
            '/companies/{companyId}/connections/{connectionId}/data/suppliers/{supplierId}/attachments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CodatDataContractsDatasetsAttachmentsDataset',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def companies_company_id_connections_connection_id_push_suppliers_post(self, company_id, connection_id, **kwargs):  # noqa: E501
        """companies_company_id_connections_connection_id_push_suppliers_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.companies_company_id_connections_connection_id_push_suppliers_post(company_id, connection_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str company_id: (required)
        :param str connection_id: (required)
        :param CodatDataContractsDatasetsSupplier body:
        :param int timeout_in_minutes:
        :return: CodatDataContractsDatasetsSupplierPushOperation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.companies_company_id_connections_connection_id_push_suppliers_post_with_http_info(company_id, connection_id, **kwargs)  # noqa: E501
        else:
            (data) = self.companies_company_id_connections_connection_id_push_suppliers_post_with_http_info(company_id, connection_id, **kwargs)  # noqa: E501
            return data

    def companies_company_id_connections_connection_id_push_suppliers_post_with_http_info(self, company_id, connection_id, **kwargs):  # noqa: E501
        """companies_company_id_connections_connection_id_push_suppliers_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.companies_company_id_connections_connection_id_push_suppliers_post_with_http_info(company_id, connection_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str company_id: (required)
        :param str connection_id: (required)
        :param CodatDataContractsDatasetsSupplier body:
        :param int timeout_in_minutes:
        :return: CodatDataContractsDatasetsSupplierPushOperation
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
                    " to method companies_company_id_connections_connection_id_push_suppliers_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'company_id' is set
        if ('company_id' not in params or
                params['company_id'] is None):
            raise ValueError("Missing the required parameter `company_id` when calling `companies_company_id_connections_connection_id_push_suppliers_post`")  # noqa: E501
        # verify the required parameter 'connection_id' is set
        if ('connection_id' not in params or
                params['connection_id'] is None):
            raise ValueError("Missing the required parameter `connection_id` when calling `companies_company_id_connections_connection_id_push_suppliers_post`")  # noqa: E501

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
            '/companies/{companyId}/connections/{connectionId}/push/suppliers', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CodatDataContractsDatasetsSupplierPushOperation',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def companies_company_id_data_suppliers_get(self, company_id, page, **kwargs):  # noqa: E501
        """Gets the latest suppliers for a company, with pagination  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.companies_company_id_data_suppliers_get(company_id, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str company_id: (required)
        :param int page: (required)
        :param int page_size:
        :param str query:
        :param str order_by:
        :return: CodatDataContractsDatasetsSupplierPagedResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.companies_company_id_data_suppliers_get_with_http_info(company_id, page, **kwargs)  # noqa: E501
        else:
            (data) = self.companies_company_id_data_suppliers_get_with_http_info(company_id, page, **kwargs)  # noqa: E501
            return data

    def companies_company_id_data_suppliers_get_with_http_info(self, company_id, page, **kwargs):  # noqa: E501
        """Gets the latest suppliers for a company, with pagination  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.companies_company_id_data_suppliers_get_with_http_info(company_id, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str company_id: (required)
        :param int page: (required)
        :param int page_size:
        :param str query:
        :param str order_by:
        :return: CodatDataContractsDatasetsSupplierPagedResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['company_id', 'page', 'page_size', 'query', 'order_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method companies_company_id_data_suppliers_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'company_id' is set
        if ('company_id' not in params or
                params['company_id'] is None):
            raise ValueError("Missing the required parameter `company_id` when calling `companies_company_id_data_suppliers_get`")  # noqa: E501
        # verify the required parameter 'page' is set
        if ('page' not in params or
                params['page'] is None):
            raise ValueError("Missing the required parameter `page` when calling `companies_company_id_data_suppliers_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'company_id' in params:
            path_params['companyId'] = params['company_id']  # noqa: E501

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
            '/companies/{companyId}/data/suppliers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CodatDataContractsDatasetsSupplierPagedResponseModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def companies_company_id_data_suppliers_supplier_id_get(self, company_id, supplier_id, **kwargs):  # noqa: E501
        """Gets a single supplier corresponding to the supplied Id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.companies_company_id_data_suppliers_supplier_id_get(company_id, supplier_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str company_id: (required)
        :param str supplier_id: (required)
        :return: CodatDataContractsDatasetsSupplier
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.companies_company_id_data_suppliers_supplier_id_get_with_http_info(company_id, supplier_id, **kwargs)  # noqa: E501
        else:
            (data) = self.companies_company_id_data_suppliers_supplier_id_get_with_http_info(company_id, supplier_id, **kwargs)  # noqa: E501
            return data

    def companies_company_id_data_suppliers_supplier_id_get_with_http_info(self, company_id, supplier_id, **kwargs):  # noqa: E501
        """Gets a single supplier corresponding to the supplied Id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.companies_company_id_data_suppliers_supplier_id_get_with_http_info(company_id, supplier_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str company_id: (required)
        :param str supplier_id: (required)
        :return: CodatDataContractsDatasetsSupplier
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['company_id', 'supplier_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method companies_company_id_data_suppliers_supplier_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'company_id' is set
        if ('company_id' not in params or
                params['company_id'] is None):
            raise ValueError("Missing the required parameter `company_id` when calling `companies_company_id_data_suppliers_supplier_id_get`")  # noqa: E501
        # verify the required parameter 'supplier_id' is set
        if ('supplier_id' not in params or
                params['supplier_id'] is None):
            raise ValueError("Missing the required parameter `supplier_id` when calling `companies_company_id_data_suppliers_supplier_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'company_id' in params:
            path_params['companyId'] = params['company_id']  # noqa: E501
        if 'supplier_id' in params:
            path_params['supplierId'] = params['supplier_id']  # noqa: E501

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
            '/companies/{companyId}/data/suppliers/{supplierId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CodatDataContractsDatasetsSupplier',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

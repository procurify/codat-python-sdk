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


class SettingsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def settings_get(self, **kwargs):  # noqa: E501
        """Fetch your settings  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.settings_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: CodatPublicApiModelsClientsClientSettingsModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.settings_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.settings_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def settings_get_with_http_info(self, **kwargs):  # noqa: E501
        """Fetch your settings  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.settings_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: CodatPublicApiModelsClientsClientSettingsModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method settings_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/settings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CodatPublicApiModelsClientsClientSettingsModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def settings_integrations_integration_id_get(self, integration_id, **kwargs):  # noqa: E501
        """Fetch your organisations integration settings  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.settings_integrations_integration_id_get(integration_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str integration_id: (required)
        :return: CodatPublicApiModelsClientsIntegrationSettingsModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.settings_integrations_integration_id_get_with_http_info(integration_id, **kwargs)  # noqa: E501
        else:
            (data) = self.settings_integrations_integration_id_get_with_http_info(integration_id, **kwargs)  # noqa: E501
            return data

    def settings_integrations_integration_id_get_with_http_info(self, integration_id, **kwargs):  # noqa: E501
        """Fetch your organisations integration settings  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.settings_integrations_integration_id_get_with_http_info(integration_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str integration_id: (required)
        :return: CodatPublicApiModelsClientsIntegrationSettingsModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method settings_integrations_integration_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'integration_id' is set
        if ('integration_id' not in params or
                params['integration_id'] is None):
            raise ValueError("Missing the required parameter `integration_id` when calling `settings_integrations_integration_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'integration_id' in params:
            path_params['integrationId'] = params['integration_id']  # noqa: E501

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
            '/settings/integrations/{integrationId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CodatPublicApiModelsClientsIntegrationSettingsModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def settings_integrations_integration_id_patch(self, integration_id, **kwargs):  # noqa: E501
        """Update your organisations integration settings  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.settings_integrations_integration_id_patch(integration_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str integration_id: (required)
        :param CodatPublicApiModelsClientsIntegrationSettingsPatchModel body:
        :return: CodatPublicApiModelsClientsIntegrationSettingsModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.settings_integrations_integration_id_patch_with_http_info(integration_id, **kwargs)  # noqa: E501
        else:
            (data) = self.settings_integrations_integration_id_patch_with_http_info(integration_id, **kwargs)  # noqa: E501
            return data

    def settings_integrations_integration_id_patch_with_http_info(self, integration_id, **kwargs):  # noqa: E501
        """Update your organisations integration settings  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.settings_integrations_integration_id_patch_with_http_info(integration_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str integration_id: (required)
        :param CodatPublicApiModelsClientsIntegrationSettingsPatchModel body:
        :return: CodatPublicApiModelsClientsIntegrationSettingsModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method settings_integrations_integration_id_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'integration_id' is set
        if ('integration_id' not in params or
                params['integration_id'] is None):
            raise ValueError("Missing the required parameter `integration_id` when calling `settings_integrations_integration_id_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'integration_id' in params:
            path_params['integrationId'] = params['integration_id']  # noqa: E501

        query_params = []

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
            '/settings/integrations/{integrationId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CodatPublicApiModelsClientsIntegrationSettingsModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def settings_patch(self, **kwargs):  # noqa: E501
        """Update your settings  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.settings_patch(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CodatPublicApiModelsClientsClientSettingsPatchModel body:
        :return: CodatPublicApiModelsClientsClientSettingsModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.settings_patch_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.settings_patch_with_http_info(**kwargs)  # noqa: E501
            return data

    def settings_patch_with_http_info(self, **kwargs):  # noqa: E501
        """Update your settings  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.settings_patch_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CodatPublicApiModelsClientsClientSettingsPatchModel body:
        :return: CodatPublicApiModelsClientsClientSettingsModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method settings_patch" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

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
            '/settings', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CodatPublicApiModelsClientsClientSettingsModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

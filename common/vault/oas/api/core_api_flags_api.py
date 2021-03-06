# coding: utf-8

"""
    vault/kernel/core_api/proto/v1/accounts/core_api_account_schedule_tags.proto

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from common.vault.oas.api_client import ApiClient


class CoreAPIFlagsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def batch_get_flag_definitions(self, **kwargs):  # noqa: E501
        """Retrieves flag definitions that correspond to the requested flag definition IDs.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.batch_get_flag_definitions(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] ids: The flag definition IDs or names to be retrieved.
        :return: FlagsBatchGetFlagDefinitionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.batch_get_flag_definitions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.batch_get_flag_definitions_with_http_info(**kwargs)  # noqa: E501
            return data

    def batch_get_flag_definitions_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves flag definitions that correspond to the requested flag definition IDs.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.batch_get_flag_definitions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] ids: The flag definition IDs or names to be retrieved.
        :return: FlagsBatchGetFlagDefinitionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method batch_get_flag_definitions" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ids' in params:
            query_params.append(('ids', params['ids']))  # noqa: E501
            collection_formats['ids'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/flag-definitions:batchGet', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FlagsBatchGetFlagDefinitionsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_flag(self, body, **kwargs):  # noqa: E501
        """Creates a flag.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_flag(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FlagsCreateFlagRequest body: (required)
        :return: FlagsFlag
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_flag_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_flag_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_flag_with_http_info(self, body, **kwargs):  # noqa: E501
        """Creates a flag.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_flag_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FlagsCreateFlagRequest body: (required)
        :return: FlagsFlag
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
                    " to method create_flag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_flag`")  # noqa: E501

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
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/flags', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FlagsFlag',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_flag_definition(self, body, **kwargs):  # noqa: E501
        """Creates a flag definition.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_flag_definition(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FlagsCreateFlagDefinitionRequest body: (required)
        :return: FlagsFlagDefinition
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_flag_definition_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_flag_definition_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_flag_definition_with_http_info(self, body, **kwargs):  # noqa: E501
        """Creates a flag definition.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_flag_definition_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FlagsCreateFlagDefinitionRequest body: (required)
        :return: FlagsFlagDefinition
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
                    " to method create_flag_definition" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_flag_definition`")  # noqa: E501

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
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/flag-definitions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FlagsFlagDefinition',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_flag_definitions(self, **kwargs):  # noqa: E501
        """Retrieves flag definitions that correspond to the parameters supplied.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_flag_definitions(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str flag_visibility_level: The flag visibility level that flag definitions are to be returned for. Set this to FLAG_VISIBILITY_OPERATOR to return flag definitions with flag visibility=FLAG_VISIBILITY_OPERATOR. Set this to FLAG_VISIBILITY_CONTRACT to return all flag definitions. Optional.
        :param list[str] flag_levels: The flag levels in the flag definition. If unspecified, this is equivalent to all flag levels. Optional.
        :param bool include_inactive: Indicates whether inactive flag definitions are included. Optional.
        :param int page_size: Number of results to be retrieved. Required; must be non-zero.
        :param str page_token: Token of the page the results are to be retrieved from. If empty, returns the first page of results. Optional.
        :return: FlagsListFlagDefinitionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_flag_definitions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_flag_definitions_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_flag_definitions_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves flag definitions that correspond to the parameters supplied.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_flag_definitions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str flag_visibility_level: The flag visibility level that flag definitions are to be returned for. Set this to FLAG_VISIBILITY_OPERATOR to return flag definitions with flag visibility=FLAG_VISIBILITY_OPERATOR. Set this to FLAG_VISIBILITY_CONTRACT to return all flag definitions. Optional.
        :param list[str] flag_levels: The flag levels in the flag definition. If unspecified, this is equivalent to all flag levels. Optional.
        :param bool include_inactive: Indicates whether inactive flag definitions are included. Optional.
        :param int page_size: Number of results to be retrieved. Required; must be non-zero.
        :param str page_token: Token of the page the results are to be retrieved from. If empty, returns the first page of results. Optional.
        :return: FlagsListFlagDefinitionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['flag_visibility_level', 'flag_levels', 'include_inactive', 'page_size', 'page_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_flag_definitions" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'flag_visibility_level' in params:
            query_params.append(('flag_visibility_level', params['flag_visibility_level']))  # noqa: E501
        if 'flag_levels' in params:
            query_params.append(('flag_levels', params['flag_levels']))  # noqa: E501
            collection_formats['flag_levels'] = 'multi'  # noqa: E501
        if 'include_inactive' in params:
            query_params.append(('include_inactive', params['include_inactive']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'page_token' in params:
            query_params.append(('page_token', params['page_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/flag-definitions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FlagsListFlagDefinitionsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_flags(self, **kwargs):  # noqa: E501
        """Retrieves flags that correspond to the parameters supplied.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_flags(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str flag_definition_id: The flag definition ID that returned flags should correspond to. Optional.
        :param list[str] customer_ids: The IDs of customers the applied flags should be included for. Optional.
        :param list[str] account_ids: The IDs of accounts the applied flags should be included for. Optional.
        :param list[str] payment_device_ids: The IDs of payment devices the applied flags should be included for. Optional.
        :param str flag_visibility_level: The flag visibility level that flags are to be returned for. Set this to FLAG_VISIBILITY_OPERATOR to return only flags belonging to a flag_definition with a flag_visibility=FLAG_VISIBILITY_OPERATOR. Set this to FLAG_VISIBILITY_CONTRACT to return all flags. Optional.
        :param datetime effective_timestamp: Timestamp after which the flag will be effective. Cannot be used in conjunction with effective_timestamp_range. Optional.
        :param RangesTimestampRange effective_timestamp_range:
        :param bool include_inactive: Indicates whether inactive flag definitions are included. Optional.
        :param int page_size: The number of results to be retrieved. Required; must be non-zero and less than 3000.
        :param str page_token: Token of the page the results are to be retrieved from. If empty, returns the first page of results. Optional.
        :return: FlagsListFlagsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_flags_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_flags_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_flags_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves flags that correspond to the parameters supplied.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_flags_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str flag_definition_id: The flag definition ID that returned flags should correspond to. Optional.
        :param list[str] customer_ids: The IDs of customers the applied flags should be included for. Optional.
        :param list[str] account_ids: The IDs of accounts the applied flags should be included for. Optional.
        :param list[str] payment_device_ids: The IDs of payment devices the applied flags should be included for. Optional.
        :param str flag_visibility_level: The flag visibility level that flags are to be returned for. Set this to FLAG_VISIBILITY_OPERATOR to return only flags belonging to a flag_definition with a flag_visibility=FLAG_VISIBILITY_OPERATOR. Set this to FLAG_VISIBILITY_CONTRACT to return all flags. Optional.
        :param datetime effective_timestamp: Timestamp after which the flag will be effective. Cannot be used in conjunction with effective_timestamp_range. Optional.
        :param RangesTimestampRange effective_timestamp_range:
        :param bool include_inactive: Indicates whether inactive flag definitions are included. Optional.
        :param int page_size: The number of results to be retrieved. Required; must be non-zero and less than 3000.
        :param str page_token: Token of the page the results are to be retrieved from. If empty, returns the first page of results. Optional.
        :return: FlagsListFlagsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['flag_definition_id', 'customer_ids', 'account_ids', 'payment_device_ids', 'flag_visibility_level', 'effective_timestamp', 'effective_timestamp_range', 'include_inactive', 'page_size', 'page_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_flags" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'flag_definition_id' in params:
            query_params.append(('flag_definition_id', params['flag_definition_id']))  # noqa: E501
        if 'customer_ids' in params:
            query_params.append(('customer_ids', params['customer_ids']))  # noqa: E501
            collection_formats['customer_ids'] = 'multi'  # noqa: E501
        if 'account_ids' in params:
            query_params.append(('account_ids', params['account_ids']))  # noqa: E501
            collection_formats['account_ids'] = 'multi'  # noqa: E501
        if 'payment_device_ids' in params:
            query_params.append(('payment_device_ids', params['payment_device_ids']))  # noqa: E501
            collection_formats['payment_device_ids'] = 'multi'  # noqa: E501
        if 'flag_visibility_level' in params:
            query_params.append(('flag_visibility_level', params['flag_visibility_level']))  # noqa: E501
        if 'effective_timestamp' in params:
            query_params.append(('effective_timestamp', params['effective_timestamp']))  # noqa: E501
        if 'effective_timestamp_range' in params:
            query_params.append(('effective_timestamp_range', params['effective_timestamp_range']))  # noqa: E501
        if 'include_inactive' in params:
            query_params.append(('include_inactive', params['include_inactive']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'page_token' in params:
            query_params.append(('page_token', params['page_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/flags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FlagsListFlagsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_flag(self, body, flag_id, **kwargs):  # noqa: E501
        """Updates a flag.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_flag(body, flag_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FlagsUpdateFlagRequest body: (required)
        :param str flag_id: The ID of the flag. Output only. (required)
        :return: FlagsFlag
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_flag_with_http_info(body, flag_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_flag_with_http_info(body, flag_id, **kwargs)  # noqa: E501
            return data

    def update_flag_with_http_info(self, body, flag_id, **kwargs):  # noqa: E501
        """Updates a flag.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_flag_with_http_info(body, flag_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FlagsUpdateFlagRequest body: (required)
        :param str flag_id: The ID of the flag. Output only. (required)
        :return: FlagsFlag
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'flag_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_flag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_flag`")  # noqa: E501
        # verify the required parameter 'flag_id' is set
        if ('flag_id' not in params or
                params['flag_id'] is None):
            raise ValueError("Missing the required parameter `flag_id` when calling `update_flag`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'flag_id' in params:
            path_params['flag.id'] = params['flag_id']  # noqa: E501

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
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/flags/{flag.id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FlagsFlag',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_flag_definition(self, body, flag_definition_id, **kwargs):  # noqa: E501
        """Updates a flag definition.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_flag_definition(body, flag_definition_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FlagsUpdateFlagDefinitionRequest body: (required)
        :param str flag_definition_id: The ID of the flag definition. Must equal the flag definition name when creating a flag definition. Required for create requests. (required)
        :return: FlagsFlagDefinition
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_flag_definition_with_http_info(body, flag_definition_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_flag_definition_with_http_info(body, flag_definition_id, **kwargs)  # noqa: E501
            return data

    def update_flag_definition_with_http_info(self, body, flag_definition_id, **kwargs):  # noqa: E501
        """Updates a flag definition.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_flag_definition_with_http_info(body, flag_definition_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FlagsUpdateFlagDefinitionRequest body: (required)
        :param str flag_definition_id: The ID of the flag definition. Must equal the flag definition name when creating a flag definition. Required for create requests. (required)
        :return: FlagsFlagDefinition
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'flag_definition_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_flag_definition" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_flag_definition`")  # noqa: E501
        # verify the required parameter 'flag_definition_id' is set
        if ('flag_definition_id' not in params or
                params['flag_definition_id'] is None):
            raise ValueError("Missing the required parameter `flag_definition_id` when calling `update_flag_definition`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'flag_definition_id' in params:
            path_params['flag_definition.id'] = params['flag_definition_id']  # noqa: E501

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
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/flag-definitions/{flag_definition.id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FlagsFlagDefinition',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

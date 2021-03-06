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


class CoreAPIAuthApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def batch_get_service_accounts(self, ids, **kwargs):  # noqa: E501
        """Retrieves service accounts for the service account IDs provided.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.batch_get_service_accounts(ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] ids: A list of the IDs of service accounts that are to be retrieved. Required; must be non-empty.  Required. Min length: 1 characters. (required)
        :return: AuthBatchGetServiceAccountsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.batch_get_service_accounts_with_http_info(ids, **kwargs)  # noqa: E501
        else:
            (data) = self.batch_get_service_accounts_with_http_info(ids, **kwargs)  # noqa: E501
            return data

    def batch_get_service_accounts_with_http_info(self, ids, **kwargs):  # noqa: E501
        """Retrieves service accounts for the service account IDs provided.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.batch_get_service_accounts_with_http_info(ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] ids: A list of the IDs of service accounts that are to be retrieved. Required; must be non-empty.  Required. Min length: 1 characters. (required)
        :return: AuthBatchGetServiceAccountsResponse
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
                    " to method batch_get_service_accounts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ids' is set
        if ('ids' not in params or
                params['ids'] is None):
            raise ValueError("Missing the required parameter `ids` when calling `batch_get_service_accounts`")  # noqa: E501

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
            '/v1/service-accounts:batchGet', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AuthBatchGetServiceAccountsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_service_account(self, body, **kwargs):  # noqa: E501
        """Creates and returns a service account with the access token populated. The name field of the service account is required for creation. For this endpoint retries work as normal but a new token is generated each time.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_service_account(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuthCreateServiceAccountRequest body: (required)
        :return: AuthServiceAccount
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_service_account_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_service_account_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_service_account_with_http_info(self, body, **kwargs):  # noqa: E501
        """Creates and returns a service account with the access token populated. The name field of the service account is required for creation. For this endpoint retries work as normal but a new token is generated each time.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_service_account_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuthCreateServiceAccountRequest body: (required)
        :return: AuthServiceAccount
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
                    " to method create_service_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_service_account`")  # noqa: E501

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
            '/v1/service-accounts', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AuthServiceAccount',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_service_account(self, id, **kwargs):  # noqa: E501
        """Retrieves the service account for the service account ID provided.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_service_account(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The ID of the service account that is to be retrieved. (required)
        :return: AuthServiceAccount
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_service_account_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_service_account_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_service_account_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieves the service account for the service account ID provided.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_service_account_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The ID of the service account that is to be retrieved. (required)
        :return: AuthServiceAccount
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_service_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_service_account`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

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
            '/v1/service-accounts/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AuthServiceAccount',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_service_accounts(self, page_size, **kwargs):  # noqa: E501
        """Lists service accounts with pagination. The request must include a page_size parameter. A list of statuses may be used as a filter. A page_token may be included to retrieve a specific page of results.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_service_accounts(page_size, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_size: The number of results to be listed. Required; must have an integer value in the range 1-100.  Required. Min: 1. Max: 100. (required)
        :param list[str] service_account_statuses: A list of service account statuses that may be used as logical OR filters for results. Optional.
        :param str page_token: Token of the page the results are to be retrieved from. If empty, returns the first page of results. Optional.
        :return: AuthListServiceAccountsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_service_accounts_with_http_info(page_size, **kwargs)  # noqa: E501
        else:
            (data) = self.list_service_accounts_with_http_info(page_size, **kwargs)  # noqa: E501
            return data

    def list_service_accounts_with_http_info(self, page_size, **kwargs):  # noqa: E501
        """Lists service accounts with pagination. The request must include a page_size parameter. A list of statuses may be used as a filter. A page_token may be included to retrieve a specific page of results.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_service_accounts_with_http_info(page_size, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_size: The number of results to be listed. Required; must have an integer value in the range 1-100.  Required. Min: 1. Max: 100. (required)
        :param list[str] service_account_statuses: A list of service account statuses that may be used as logical OR filters for results. Optional.
        :param str page_token: Token of the page the results are to be retrieved from. If empty, returns the first page of results. Optional.
        :return: AuthListServiceAccountsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'service_account_statuses', 'page_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_service_accounts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'page_size' is set
        if ('page_size' not in params or
                params['page_size'] is None):
            raise ValueError("Missing the required parameter `page_size` when calling `list_service_accounts`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'service_account_statuses' in params:
            query_params.append(('service_account_statuses', params['service_account_statuses']))  # noqa: E501
            collection_formats['service_account_statuses'] = 'multi'  # noqa: E501
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
            '/v1/service-accounts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AuthListServiceAccountsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_service_account(self, body, service_account_id, **kwargs):  # noqa: E501
        """Updates a service account. The service account token will only be returned when the token is refreshed or if an inactive service account is reactivated. If an inactive service account is reactivated, a new token is generated. A service account with active status can be updated to be frozen or inactive. A service account with frozen status can be updated to active or inactive. If a frozen account is reactivated, a new token is not required. A service account with inactive status can only be updated to active status. Freezing a service account will disable existing tokens until the service account is reactivated. Deactivating a service account will permanently invalidate all previous tokens and new tokens will be required.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_service_account(body, service_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuthUpdateServiceAccountRequest body: (required)
        :param str service_account_id: A unique string ID for a service account. Output only. (required)
        :return: AuthServiceAccount
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_service_account_with_http_info(body, service_account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_service_account_with_http_info(body, service_account_id, **kwargs)  # noqa: E501
            return data

    def update_service_account_with_http_info(self, body, service_account_id, **kwargs):  # noqa: E501
        """Updates a service account. The service account token will only be returned when the token is refreshed or if an inactive service account is reactivated. If an inactive service account is reactivated, a new token is generated. A service account with active status can be updated to be frozen or inactive. A service account with frozen status can be updated to active or inactive. If a frozen account is reactivated, a new token is not required. A service account with inactive status can only be updated to active status. Freezing a service account will disable existing tokens until the service account is reactivated. Deactivating a service account will permanently invalidate all previous tokens and new tokens will be required.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_service_account_with_http_info(body, service_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuthUpdateServiceAccountRequest body: (required)
        :param str service_account_id: A unique string ID for a service account. Output only. (required)
        :return: AuthServiceAccount
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'service_account_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_service_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_service_account`")  # noqa: E501
        # verify the required parameter 'service_account_id' is set
        if ('service_account_id' not in params or
                params['service_account_id'] is None):
            raise ValueError("Missing the required parameter `service_account_id` when calling `update_service_account`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'service_account_id' in params:
            path_params['service_account.id'] = params['service_account_id']  # noqa: E501

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
            '/v1/service-accounts/{service_account.id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AuthServiceAccount',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_service_account_permissions(self, body, service_account_id, **kwargs):  # noqa: E501
        """Updates the permissions for a service account.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_service_account_permissions(body, service_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuthUpdateServiceAccountPermissionsRequest body: (required)
        :param str service_account_id: The ID of the service account that is to be updated. Required. (required)
        :return: AuthServiceAccount
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_service_account_permissions_with_http_info(body, service_account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_service_account_permissions_with_http_info(body, service_account_id, **kwargs)  # noqa: E501
            return data

    def update_service_account_permissions_with_http_info(self, body, service_account_id, **kwargs):  # noqa: E501
        """Updates the permissions for a service account.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_service_account_permissions_with_http_info(body, service_account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AuthUpdateServiceAccountPermissionsRequest body: (required)
        :param str service_account_id: The ID of the service account that is to be updated. Required. (required)
        :return: AuthServiceAccount
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'service_account_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_service_account_permissions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_service_account_permissions`")  # noqa: E501
        # verify the required parameter 'service_account_id' is set
        if ('service_account_id' not in params or
                params['service_account_id'] is None):
            raise ValueError("Missing the required parameter `service_account_id` when calling `update_service_account_permissions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'service_account_id' in params:
            path_params['service_account_id'] = params['service_account_id']  # noqa: E501

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
            '/v1/service-accounts/{service_account_id}:updatePermissions', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AuthServiceAccount',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def validate_token(self, **kwargs):  # noqa: E501
        """Checks if a token is valid.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.validate_token(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: AuthValidateTokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.validate_token_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.validate_token_with_http_info(**kwargs)  # noqa: E501
            return data

    def validate_token_with_http_info(self, **kwargs):  # noqa: E501
        """Checks if a token is valid.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.validate_token_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: AuthValidateTokenResponse
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
                    " to method validate_token" % key
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
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/token:validate', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AuthValidateTokenResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

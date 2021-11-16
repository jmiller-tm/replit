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


class CoreAPIPostingsAPIClientApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def batch_get_postings_api_clients(self, **kwargs):  # noqa: E501
        """Gets a map of `id` to `PostingsAPIClient` for a given set of `id`s.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.batch_get_postings_api_clients(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] ids: A list of unique IDs that identify `PostingsAPIClient`s to the Postings API. Required.
        :return: PostingsApiClientsBatchGetPostingsAPIClientsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.batch_get_postings_api_clients_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.batch_get_postings_api_clients_with_http_info(**kwargs)  # noqa: E501
            return data

    def batch_get_postings_api_clients_with_http_info(self, **kwargs):  # noqa: E501
        """Gets a map of `id` to `PostingsAPIClient` for a given set of `id`s.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.batch_get_postings_api_clients_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] ids: A list of unique IDs that identify `PostingsAPIClient`s to the Postings API. Required.
        :return: PostingsApiClientsBatchGetPostingsAPIClientsResponse
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
                    " to method batch_get_postings_api_clients" % key
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
            '/v1/postings-api-clients:batchGet', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PostingsApiClientsBatchGetPostingsAPIClientsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_postings_api_client(self, body, **kwargs):  # noqa: E501
        """Creates and returns a specified `PostingsAPIClient`. The response topic will be created if it does not exist and must contain the prefix 'integration.'. For compatibility, existing topics that are not prefixed with 'integration.' are allowed.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_postings_api_client(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostingsApiClientsCreatePostingsAPIClientRequest body: (required)
        :return: PostingsApiClientsPostingsAPIClient
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_postings_api_client_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_postings_api_client_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_postings_api_client_with_http_info(self, body, **kwargs):  # noqa: E501
        """Creates and returns a specified `PostingsAPIClient`. The response topic will be created if it does not exist and must contain the prefix 'integration.'. For compatibility, existing topics that are not prefixed with 'integration.' are allowed.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_postings_api_client_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostingsApiClientsCreatePostingsAPIClientRequest body: (required)
        :return: PostingsApiClientsPostingsAPIClient
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
                    " to method create_postings_api_client" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_postings_api_client`")  # noqa: E501

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
            '/v1/postings-api-clients', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PostingsApiClientsPostingsAPIClient',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_postings_api_client(self, id, **kwargs):  # noqa: E501
        """Gets a `PostingsAPIClient` for the given `id`.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_postings_api_client(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: A unique ID that identifies a `PostingsAPIClient` to the Postings API. Required. (required)
        :return: PostingsApiClientsPostingsAPIClient
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_postings_api_client_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_postings_api_client_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_postings_api_client_with_http_info(self, id, **kwargs):  # noqa: E501
        """Gets a `PostingsAPIClient` for the given `id`.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_postings_api_client_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: A unique ID that identifies a `PostingsAPIClient` to the Postings API. Required. (required)
        :return: PostingsApiClientsPostingsAPIClient
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
                    " to method get_postings_api_client" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_postings_api_client`")  # noqa: E501

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
            '/v1/postings-api-clients/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PostingsApiClientsPostingsAPIClient',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_postings_api_clients(self, **kwargs):  # noqa: E501
        """Gets a list of all `PostingsAPIClient`s.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_postings_api_clients(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_size: The number of results to retrieve. Required; must be non-zero.
        :param str page_token: Token of the page the results are to be retrieved from. If empty, the first page of results will be returned. Optional.
        :return: PostingsApiClientsListPostingsAPIClientsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_postings_api_clients_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_postings_api_clients_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_postings_api_clients_with_http_info(self, **kwargs):  # noqa: E501
        """Gets a list of all `PostingsAPIClient`s.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_postings_api_clients_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_size: The number of results to retrieve. Required; must be non-zero.
        :param str page_token: Token of the page the results are to be retrieved from. If empty, the first page of results will be returned. Optional.
        :return: PostingsApiClientsListPostingsAPIClientsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'page_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_postings_api_clients" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
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
            '/v1/postings-api-clients', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PostingsApiClientsListPostingsAPIClientsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_postings_api_client(self, body, postings_api_client_id, **kwargs):  # noqa: E501
        """Updates an existing `PostingsAPIClient` with a new `response_topic_low_priority`, which must differ from `response_topic`. The response topic will be created if it does not exist and must contain the prefix 'integration.'. For compatibility, existing topics that are not prefixed with 'integration.' are allowed.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_postings_api_client(body, postings_api_client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostingsApiClientsUpdatePostingsAPIClientRequest body: (required)
        :param str postings_api_client_id: A unique ID that identifies a `PostingsAPIClient` to the Postings API. (required)
        :return: PostingsApiClientsPostingsAPIClient
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_postings_api_client_with_http_info(body, postings_api_client_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_postings_api_client_with_http_info(body, postings_api_client_id, **kwargs)  # noqa: E501
            return data

    def update_postings_api_client_with_http_info(self, body, postings_api_client_id, **kwargs):  # noqa: E501
        """Updates an existing `PostingsAPIClient` with a new `response_topic_low_priority`, which must differ from `response_topic`. The response topic will be created if it does not exist and must contain the prefix 'integration.'. For compatibility, existing topics that are not prefixed with 'integration.' are allowed.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_postings_api_client_with_http_info(body, postings_api_client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostingsApiClientsUpdatePostingsAPIClientRequest body: (required)
        :param str postings_api_client_id: A unique ID that identifies a `PostingsAPIClient` to the Postings API. (required)
        :return: PostingsApiClientsPostingsAPIClient
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'postings_api_client_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_postings_api_client" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_postings_api_client`")  # noqa: E501
        # verify the required parameter 'postings_api_client_id' is set
        if ('postings_api_client_id' not in params or
                params['postings_api_client_id'] is None):
            raise ValueError("Missing the required parameter `postings_api_client_id` when calling `update_postings_api_client`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'postings_api_client_id' in params:
            path_params['postings_api_client.id'] = params['postings_api_client_id']  # noqa: E501

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
            '/v1/postings-api-clients/{postings_api_client.id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PostingsApiClientsPostingsAPIClient',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
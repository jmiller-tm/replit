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


class CoreAPIAccountScheduleTagsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def batch_get_account_schedule_tags(self, ids, **kwargs):  # noqa: E501
        """Retrieves one or more AccountScheduleTags based on their AccountScheduleTag IDs.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.batch_get_account_schedule_tags(ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] ids: A list of the IDs of the AccountScheduleTags that are to be retrieved.  Required. Min length: 1 characters. (required)
        :return: AccountScheduleTagsBatchGetAccountScheduleTagsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.batch_get_account_schedule_tags_with_http_info(ids, **kwargs)  # noqa: E501
        else:
            (data) = self.batch_get_account_schedule_tags_with_http_info(ids, **kwargs)  # noqa: E501
            return data

    def batch_get_account_schedule_tags_with_http_info(self, ids, **kwargs):  # noqa: E501
        """Retrieves one or more AccountScheduleTags based on their AccountScheduleTag IDs.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.batch_get_account_schedule_tags_with_http_info(ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] ids: A list of the IDs of the AccountScheduleTags that are to be retrieved.  Required. Min length: 1 characters. (required)
        :return: AccountScheduleTagsBatchGetAccountScheduleTagsResponse
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
                    " to method batch_get_account_schedule_tags" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ids' is set
        if ('ids' not in params or
                params['ids'] is None):
            raise ValueError("Missing the required parameter `ids` when calling `batch_get_account_schedule_tags`")  # noqa: E501

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
            '/v1/account-schedule-tags:batchGet', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccountScheduleTagsBatchGetAccountScheduleTagsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_account_schedule_tag(self, body, **kwargs):  # noqa: E501
        """Creates an AccountScheduleTag. The AccountScheduleTag can be created with a status of `ACCOUNT_SCHEDULE_TAG_SCHEDULE_STATUS_OVERRIDE_NO_OVERRIDE`, `ACCOUNT_SCHEDULE_TAG_SCHEDULE_STATUS_OVERRIDE_TO_ENABLED`, `ACCOUNT_SCHEDULE_TAG_SCHEDULE_STATUS_OVERRIDE_TO_FAST_FORWARDED` or `ACCOUNT_SCHEDULE_TAG_SCHEDULE_STATUS_OVERRIDE_TO_SKIPPED`.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_account_schedule_tag(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccountScheduleTagsCreateAccountScheduleTagRequest body: (required)
        :return: AccountScheduleTagsAccountScheduleTag
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_account_schedule_tag_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_account_schedule_tag_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_account_schedule_tag_with_http_info(self, body, **kwargs):  # noqa: E501
        """Creates an AccountScheduleTag. The AccountScheduleTag can be created with a status of `ACCOUNT_SCHEDULE_TAG_SCHEDULE_STATUS_OVERRIDE_NO_OVERRIDE`, `ACCOUNT_SCHEDULE_TAG_SCHEDULE_STATUS_OVERRIDE_TO_ENABLED`, `ACCOUNT_SCHEDULE_TAG_SCHEDULE_STATUS_OVERRIDE_TO_FAST_FORWARDED` or `ACCOUNT_SCHEDULE_TAG_SCHEDULE_STATUS_OVERRIDE_TO_SKIPPED`.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_account_schedule_tag_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccountScheduleTagsCreateAccountScheduleTagRequest body: (required)
        :return: AccountScheduleTagsAccountScheduleTag
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
                    " to method create_account_schedule_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_account_schedule_tag`")  # noqa: E501

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
            '/v1/account-schedule-tags', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccountScheduleTagsAccountScheduleTag',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_account_schedule_tags(self, page_size, **kwargs):  # noqa: E501
        """Retrieves all AccountScheduleTags.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_account_schedule_tags(page_size, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_size: The number of results to be listed.  Required. Min: 1. Max: 500. (required)
        :param str page_token: Token of the page the results are to be retrieved from. If empty, returns the first page of results. Optional.
        :return: AccountScheduleTagsListAccountScheduleTagsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_account_schedule_tags_with_http_info(page_size, **kwargs)  # noqa: E501
        else:
            (data) = self.list_account_schedule_tags_with_http_info(page_size, **kwargs)  # noqa: E501
            return data

    def list_account_schedule_tags_with_http_info(self, page_size, **kwargs):  # noqa: E501
        """Retrieves all AccountScheduleTags.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_account_schedule_tags_with_http_info(page_size, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_size: The number of results to be listed.  Required. Min: 1. Max: 500. (required)
        :param str page_token: Token of the page the results are to be retrieved from. If empty, returns the first page of results. Optional.
        :return: AccountScheduleTagsListAccountScheduleTagsResponse
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
                    " to method list_account_schedule_tags" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'page_size' is set
        if ('page_size' not in params or
                params['page_size'] is None):
            raise ValueError("Missing the required parameter `page_size` when calling `list_account_schedule_tags`")  # noqa: E501

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
            '/v1/account-schedule-tags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccountScheduleTagsListAccountScheduleTagsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_account_schedule_tag(self, body, account_schedule_tag_id, **kwargs):  # noqa: E501
        """Updates an AccountScheduleTag.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_account_schedule_tag(body, account_schedule_tag_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccountScheduleTagsUpdateAccountScheduleTagRequest body: (required)
        :param str account_schedule_tag_id: The ID of the AccountScheduleTag; it is used to tag schedules in a Smart Contract or Supervisor Contract. (required)
        :return: AccountScheduleTagsAccountScheduleTag
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_account_schedule_tag_with_http_info(body, account_schedule_tag_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_account_schedule_tag_with_http_info(body, account_schedule_tag_id, **kwargs)  # noqa: E501
            return data

    def update_account_schedule_tag_with_http_info(self, body, account_schedule_tag_id, **kwargs):  # noqa: E501
        """Updates an AccountScheduleTag.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_account_schedule_tag_with_http_info(body, account_schedule_tag_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccountScheduleTagsUpdateAccountScheduleTagRequest body: (required)
        :param str account_schedule_tag_id: The ID of the AccountScheduleTag; it is used to tag schedules in a Smart Contract or Supervisor Contract. (required)
        :return: AccountScheduleTagsAccountScheduleTag
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'account_schedule_tag_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_account_schedule_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_account_schedule_tag`")  # noqa: E501
        # verify the required parameter 'account_schedule_tag_id' is set
        if ('account_schedule_tag_id' not in params or
                params['account_schedule_tag_id'] is None):
            raise ValueError("Missing the required parameter `account_schedule_tag_id` when calling `update_account_schedule_tag`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_schedule_tag_id' in params:
            path_params['account_schedule_tag.id'] = params['account_schedule_tag_id']  # noqa: E501

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
            '/v1/account-schedule-tags/{account_schedule_tag.id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccountScheduleTagsAccountScheduleTag',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

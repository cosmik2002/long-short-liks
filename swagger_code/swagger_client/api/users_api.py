# coding: utf-8

"""
    short_long_links

    This is a simple API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: you@your-company.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class UsersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_long_to_short_put(self, **kwargs):  # noqa: E501
        """shotter link, return short link  # noqa: E501

        shotter link, return short link  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_long_to_short_put(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str long_url: long link
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_long_to_short_put_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_long_to_short_put_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_long_to_short_put_with_http_info(self, **kwargs):  # noqa: E501
        """shotter link, return short link  # noqa: E501

        shotter link, return short link  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_long_to_short_put_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str long_url: long link
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['long_url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_long_to_short_put" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'long_url' in params:
            form_params.append(('long_url', params['long_url']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/long_to_short', 'PUT',
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

    def api_short_postfix_get(self, short_postfix, **kwargs):  # noqa: E501
        """redirect to long link  # noqa: E501

        search long link and redirect  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_short_postfix_get(short_postfix, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str short_postfix: short_postfix for long link (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_short_postfix_get_with_http_info(short_postfix, **kwargs)  # noqa: E501
        else:
            (data) = self.api_short_postfix_get_with_http_info(short_postfix, **kwargs)  # noqa: E501
            return data

    def api_short_postfix_get_with_http_info(self, short_postfix, **kwargs):  # noqa: E501
        """redirect to long link  # noqa: E501

        search long link and redirect  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_short_postfix_get_with_http_info(short_postfix, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str short_postfix: short_postfix for long link (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['short_postfix']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_short_postfix_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'short_postfix' is set
        if ('short_postfix' not in params or
                params['short_postfix'] is None):
            raise ValueError("Missing the required parameter `short_postfix` when calling `api_short_postfix_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'short_postfix' in params:
            path_params['short_postfix'] = params['short_postfix']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['redirect'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/{short_postfix}', 'GET',
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

    def api_statistic_short_postfix_get(self, short_postfix, **kwargs):  # noqa: E501
        """statistic to short link  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_statistic_short_postfix_get(short_postfix, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str short_postfix: short_postfix for long link (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_statistic_short_postfix_get_with_http_info(short_postfix, **kwargs)  # noqa: E501
        else:
            (data) = self.api_statistic_short_postfix_get_with_http_info(short_postfix, **kwargs)  # noqa: E501
            return data

    def api_statistic_short_postfix_get_with_http_info(self, short_postfix, **kwargs):  # noqa: E501
        """statistic to short link  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_statistic_short_postfix_get_with_http_info(short_postfix, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str short_postfix: short_postfix for long link (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['short_postfix']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_statistic_short_postfix_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'short_postfix' is set
        if ('short_postfix' not in params or
                params['short_postfix'] is None):
            raise ValueError("Missing the required parameter `short_postfix` when calling `api_statistic_short_postfix_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'short_postfix' in params:
            path_params['short_postfix'] = params['short_postfix']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/statistic/{short_postfix}', 'GET',
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
# coding: utf-8

"""
    short_long_links

    This is a simple API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: you@your-company.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.users_api import UsersApi  # noqa: E501
from swagger_client.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.users_api.UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_long_to_short_put(self):
        """Test case for api_long_to_short_put

        shotter link, return short link  # noqa: E501
        """
        pass

    def test_api_short_postfix_get(self):
        """Test case for api_short_postfix_get

        redirect to long link  # noqa: E501
        """
        pass

    def test_api_statistic_short_postfix_get(self):
        """Test case for api_statistic_short_postfix_get

        statistic to short link  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

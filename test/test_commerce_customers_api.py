# coding: utf-8

"""
    Codat API

    [What's changed in our Swagger](https://docs.codat.io/docs/new-swagger-ui)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.commerce_customers_api import CommerceCustomersApi  # noqa: E501
from swagger_client.rest import ApiException


class TestCommerceCustomersApi(unittest.TestCase):
    """CommerceCustomersApi unit test stubs"""

    def setUp(self):
        self.api = CommerceCustomersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_companies_company_id_connections_connection_id_data_commerce_customers_customer_id_get(self):
        """Test case for companies_company_id_connections_connection_id_data_commerce_customers_customer_id_get

        Gets the specified commerce customer for a given company  # noqa: E501
        """
        pass

    def test_companies_company_id_connections_connection_id_data_commerce_customers_get(self):
        """Test case for companies_company_id_connections_connection_id_data_commerce_customers_get

        Gets the latest commerce customers for a company, with pagination  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

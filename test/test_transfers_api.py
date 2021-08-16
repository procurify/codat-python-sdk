# coding: utf-8

"""
    Codat API

    [What's changed in our Swagger](https://docs.codat.io/docs/new-swagger-ui)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import codat_python_sdk
from codat_python_sdk.api.transfers_api import TransfersApi  # noqa: E501
from codat_python_sdk.rest import ApiException


class TestTransfersApi(unittest.TestCase):
    """TransfersApi unit test stubs"""

    def setUp(self):
        self.api = TransfersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_companies_company_id_connections_connection_id_data_transfers_get(self):
        """Test case for companies_company_id_connections_connection_id_data_transfers_get

        Gets the transfers for a given company.  # noqa: E501
        """
        pass

    def test_companies_company_id_connections_connection_id_data_transfers_transfer_id_get(self):
        """Test case for companies_company_id_connections_connection_id_data_transfers_transfer_id_get

        Gets the specified transfer for a given company.  # noqa: E501
        """
        pass

    def test_companies_company_id_connections_connection_id_push_transfers_post(self):
        """Test case for companies_company_id_connections_connection_id_push_transfers_post

        Posts a new transfer to the accounting package for a given company.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

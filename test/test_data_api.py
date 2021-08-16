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
from codat_python_sdk.api.data_api import DataApi  # noqa: E501
from codat_python_sdk.rest import ApiException


class TestDataApi(unittest.TestCase):
    """DataApi unit test stubs"""

    def setUp(self):
        self.api = DataApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_companies_company_id_data_all_post(self):
        """Test case for companies_company_id_data_all_post

        Initiates the process of capturing a new data snapshot for a company  # noqa: E501
        """
        pass

    def test_companies_company_id_data_history_dataset_id_get(self):
        """Test case for companies_company_id_data_history_dataset_id_get

        Fetch metadata on a single data synchronisation  # noqa: E501
        """
        pass

    def test_companies_company_id_data_history_get(self):
        """Test case for companies_company_id_data_history_get

        Fetch a list of all data snapshots captured for a company  # noqa: E501
        """
        pass

    def test_companies_company_id_data_queue_data_type_post(self):
        """Test case for companies_company_id_data_queue_data_type_post

        Initiates the process of capturing a data snapshot of a specified type for a company  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

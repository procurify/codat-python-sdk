"""
    Codat API

    [What's changed in our Swagger](https://docs.codat.io/docs/new-swagger-ui)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import unittest

import codat_python_sdk
from codat_python_sdk.api.commerce_locations_api import CommerceLocationsApi  # noqa: E501


class TestCommerceLocationsApi(unittest.TestCase):
    """CommerceLocationsApi unit test stubs"""

    def setUp(self):
        self.api = CommerceLocationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_companies_company_id_connections_connection_id_data_commerce_locations_get(self):
        """Test case for companies_company_id_connections_connection_id_data_commerce_locations_get

        Gets the latest commerce locations for a company, with pagination  # noqa: E501
        """
        pass

    def test_companies_company_id_connections_connection_id_data_commerce_locations_location_id_get(self):
        """Test case for companies_company_id_connections_connection_id_data_commerce_locations_location_id_get

        Gets the specified commerce location for a given company  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

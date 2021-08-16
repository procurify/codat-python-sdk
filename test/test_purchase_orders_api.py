"""
    Codat API

    [What's changed in our Swagger](https://docs.codat.io/docs/new-swagger-ui)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import unittest

import codat_python_sdk
from codat_python_sdk.api.purchase_orders_api import PurchaseOrdersApi  # noqa: E501


class TestPurchaseOrdersApi(unittest.TestCase):
    """PurchaseOrdersApi unit test stubs"""

    def setUp(self):
        self.api = PurchaseOrdersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_companies_company_id_connections_connection_id_push_purchase_orders_post(self):
        """Test case for companies_company_id_connections_connection_id_push_purchase_orders_post

        Posts a new purchase order to the accounting package for a given company.  # noqa: E501
        """
        pass

    def test_companies_company_id_connections_connection_id_push_purchase_orders_purchase_order_id_put(self):
        """Test case for companies_company_id_connections_connection_id_push_purchase_orders_purchase_order_id_put

        Posts an updated purchase order to the accounting package for a given company.  # noqa: E501
        """
        pass

    def test_companies_company_id_data_purchase_orders_get(self):
        """Test case for companies_company_id_data_purchase_orders_get

        """
        pass

    def test_companies_company_id_data_purchase_orders_purchase_order_id_get(self):
        """Test case for companies_company_id_data_purchase_orders_purchase_order_id_get

        """
        pass


if __name__ == '__main__':
    unittest.main()

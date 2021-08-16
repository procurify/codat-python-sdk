"""
    Codat API

    [What's changed in our Swagger](https://docs.codat.io/docs/new-swagger-ui)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import unittest

import codat_python_sdk
from codat_python_sdk.api.suppliers_api import SuppliersApi  # noqa: E501


class TestSuppliersApi(unittest.TestCase):
    """SuppliersApi unit test stubs"""

    def setUp(self):
        self.api = SuppliersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_download_get(self):
        """Test case for companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_download_get

        """
        pass

    def test_companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_get(self):
        """Test case for companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_get

        """
        pass

    def test_companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_get(self):
        """Test case for companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_get

        """
        pass

    def test_companies_company_id_connections_connection_id_push_suppliers_post(self):
        """Test case for companies_company_id_connections_connection_id_push_suppliers_post

        """
        pass

    def test_companies_company_id_data_suppliers_get(self):
        """Test case for companies_company_id_data_suppliers_get

        Gets the latest suppliers for a company, with pagination  # noqa: E501
        """
        pass

    def test_companies_company_id_data_suppliers_supplier_id_get(self):
        """Test case for companies_company_id_data_suppliers_supplier_id_get

        Gets a single supplier corresponding to the supplied Id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

"""
    Codat API

    [What's changed in our Swagger](https://docs.codat.io/docs/new-swagger-ui)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import unittest

import codat_python_sdk
from codat_python_sdk.api.bills_api import BillsApi  # noqa: E501


class TestBillsApi(unittest.TestCase):
    """BillsApi unit test stubs"""

    def setUp(self):
        self.api = BillsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_companies_company_id_connections_connection_id_data_bills_bill_id_attachments_attachment_id_download_get(self):
        """Test case for companies_company_id_connections_connection_id_data_bills_bill_id_attachments_attachment_id_download_get

        """
        pass

    def test_companies_company_id_connections_connection_id_data_bills_bill_id_attachments_attachment_id_get(self):
        """Test case for companies_company_id_connections_connection_id_data_bills_bill_id_attachments_attachment_id_get

        """
        pass

    def test_companies_company_id_connections_connection_id_data_bills_bill_id_attachments_get(self):
        """Test case for companies_company_id_connections_connection_id_data_bills_bill_id_attachments_get

        """
        pass

    def test_companies_company_id_connections_connection_id_push_bills_bill_id_attachments_post(self):
        """Test case for companies_company_id_connections_connection_id_push_bills_bill_id_attachments_post

        """
        pass

    def test_companies_company_id_connections_connection_id_push_bills_bill_id_put(self):
        """Test case for companies_company_id_connections_connection_id_push_bills_bill_id_put

        Posts an updated bill to the accounting package for a given company.  # noqa: E501
        """
        pass

    def test_companies_company_id_connections_connection_id_push_bills_post(self):
        """Test case for companies_company_id_connections_connection_id_push_bills_post

        Posts a new bill to the accounting package for a given company.  # noqa: E501
        """
        pass

    def test_companies_company_id_data_bills_bill_id_get(self):
        """Test case for companies_company_id_data_bills_bill_id_get

        """
        pass

    def test_companies_company_id_data_bills_get(self):
        """Test case for companies_company_id_data_bills_get

        Gets the latest bills for a company, with pagination  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

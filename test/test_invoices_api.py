"""
    Codat API

    [What's changed in our Swagger](https://docs.codat.io/docs/new-swagger-ui)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import unittest

import codat_python_sdk
from codat_python_sdk.api.invoices_api import InvoicesApi  # noqa: E501


class TestInvoicesApi(unittest.TestCase):
    """InvoicesApi unit test stubs"""

    def setUp(self):
        self.api = InvoicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_attachment_id_download_get(self):
        """Test case for companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_attachment_id_download_get

        """
        pass

    def test_companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_attachment_id_get(self):
        """Test case for companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_attachment_id_get

        """
        pass

    def test_companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_get(self):
        """Test case for companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_get

        """
        pass

    def test_companies_company_id_connections_connection_id_push_invoices_invoice_id_attachment_post(self):
        """Test case for companies_company_id_connections_connection_id_push_invoices_invoice_id_attachment_post

        """
        pass

    def test_companies_company_id_connections_connection_id_push_invoices_invoice_id_put(self):
        """Test case for companies_company_id_connections_connection_id_push_invoices_invoice_id_put

        Posts an updated invoice to the accounting package for a given company.  # noqa: E501
        """
        pass

    def test_companies_company_id_connections_connection_id_push_invoices_post(self):
        """Test case for companies_company_id_connections_connection_id_push_invoices_post

        Posts a new invoice to the accounting package for a given company.  # noqa: E501
        """
        pass

    def test_companies_company_id_data_invoices_get(self):
        """Test case for companies_company_id_data_invoices_get

        Gets the latest invoices for a company, with pagination  # noqa: E501
        """
        pass

    def test_companies_company_id_data_invoices_invoice_id_get(self):
        """Test case for companies_company_id_data_invoices_invoice_id_get

        """
        pass

    def test_companies_company_id_data_invoices_invoice_id_pdf_get(self):
        """Test case for companies_company_id_data_invoices_invoice_id_pdf_get

        """
        pass


if __name__ == '__main__':
    unittest.main()

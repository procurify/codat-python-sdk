# codat_python_sdk.InvoicesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_attachment_id_download_get**](InvoicesApi.md#companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_attachment_id_download_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/invoices/{invoiceId}/attachments/{attachmentId}/download | 
[**companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_attachment_id_get**](InvoicesApi.md#companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_attachment_id_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/invoices/{invoiceId}/attachments/{attachmentId} | 
[**companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_get**](InvoicesApi.md#companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/invoices/{invoiceId}/attachments | 
[**companies_company_id_connections_connection_id_push_invoices_invoice_id_attachment_post**](InvoicesApi.md#companies_company_id_connections_connection_id_push_invoices_invoice_id_attachment_post) | **POST** /companies/{companyId}/connections/{connectionId}/push/invoices/{invoiceId}/attachment | 
[**companies_company_id_connections_connection_id_push_invoices_invoice_id_put**](InvoicesApi.md#companies_company_id_connections_connection_id_push_invoices_invoice_id_put) | **PUT** /companies/{companyId}/connections/{connectionId}/push/invoices/{invoiceId} | Posts an updated invoice to the accounting package for a given company.
[**companies_company_id_connections_connection_id_push_invoices_post**](InvoicesApi.md#companies_company_id_connections_connection_id_push_invoices_post) | **POST** /companies/{companyId}/connections/{connectionId}/push/invoices | Posts a new invoice to the accounting package for a given company.
[**companies_company_id_data_invoices_get**](InvoicesApi.md#companies_company_id_data_invoices_get) | **GET** /companies/{companyId}/data/invoices | Gets the latest invoices for a company, with pagination
[**companies_company_id_data_invoices_invoice_id_get**](InvoicesApi.md#companies_company_id_data_invoices_invoice_id_get) | **GET** /companies/{companyId}/data/invoices/{invoiceId} | 
[**companies_company_id_data_invoices_invoice_id_pdf_get**](InvoicesApi.md#companies_company_id_data_invoices_invoice_id_pdf_get) | **GET** /companies/{companyId}/data/invoices/{invoiceId}/pdf | 


# **companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_attachment_id_download_get**
> companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_attachment_id_download_get(company_id, connection_id, invoice_id, attachment_id)



### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import invoices_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = codat_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: API Key Auth
configuration.api_key['API Key Auth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API Key Auth'] = 'Bearer'

# Configure OAuth2 access token for authorization: Codat Login
configuration = codat_python_sdk.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with codat_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = invoices_api.InvoicesApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    invoice_id = "invoiceId_example" # str | 
    attachment_id = "attachmentId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_attachment_id_download_get(company_id, connection_id, invoice_id, attachment_id)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling InvoicesApi->companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_attachment_id_download_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **invoice_id** | **str**|  |
 **attachment_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[API Key Auth](../README.md#API Key Auth), [Codat Login](../README.md#Codat Login)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_attachment_id_get**
> CodatDataContractsDatasetsAttachmentsDatasetAttachment companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_attachment_id_get(company_id, connection_id, invoice_id, attachment_id)



### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import invoices_api
from codat_python_sdk.model.codat_data_contracts_datasets_attachments_dataset_attachment import CodatDataContractsDatasetsAttachmentsDatasetAttachment
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = codat_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: API Key Auth
configuration.api_key['API Key Auth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API Key Auth'] = 'Bearer'

# Configure OAuth2 access token for authorization: Codat Login
configuration = codat_python_sdk.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with codat_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = invoices_api.InvoicesApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    invoice_id = "invoiceId_example" # str | 
    attachment_id = "attachmentId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_attachment_id_get(company_id, connection_id, invoice_id, attachment_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling InvoicesApi->companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_attachment_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **invoice_id** | **str**|  |
 **attachment_id** | **str**|  |

### Return type

[**CodatDataContractsDatasetsAttachmentsDatasetAttachment**](CodatDataContractsDatasetsAttachmentsDatasetAttachment.md)

### Authorization

[API Key Auth](../README.md#API Key Auth), [Codat Login](../README.md#Codat Login)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_get**
> CodatDataContractsDatasetsAttachmentsDataset companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_get(company_id, connection_id, invoice_id)



### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import invoices_api
from codat_python_sdk.model.codat_data_contracts_datasets_attachments_dataset import CodatDataContractsDatasetsAttachmentsDataset
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = codat_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: API Key Auth
configuration.api_key['API Key Auth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API Key Auth'] = 'Bearer'

# Configure OAuth2 access token for authorization: Codat Login
configuration = codat_python_sdk.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with codat_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = invoices_api.InvoicesApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    invoice_id = "invoiceId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_get(company_id, connection_id, invoice_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling InvoicesApi->companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **invoice_id** | **str**|  |

### Return type

[**CodatDataContractsDatasetsAttachmentsDataset**](CodatDataContractsDatasetsAttachmentsDataset.md)

### Authorization

[API Key Auth](../README.md#API Key Auth), [Codat Login](../README.md#Codat Login)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_push_invoices_invoice_id_attachment_post**
> companies_company_id_connections_connection_id_push_invoices_invoice_id_attachment_post(company_id, connection_id, invoice_id)



### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import invoices_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = codat_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: API Key Auth
configuration.api_key['API Key Auth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API Key Auth'] = 'Bearer'

# Configure OAuth2 access token for authorization: Codat Login
configuration = codat_python_sdk.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with codat_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = invoices_api.InvoicesApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    invoice_id = "invoiceId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.companies_company_id_connections_connection_id_push_invoices_invoice_id_attachment_post(company_id, connection_id, invoice_id)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling InvoicesApi->companies_company_id_connections_connection_id_push_invoices_invoice_id_attachment_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **invoice_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[API Key Auth](../README.md#API Key Auth), [Codat Login](../README.md#Codat Login)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_push_invoices_invoice_id_put**
> CodatDataContractsDatasetsLegacyInvoicePushOperation companies_company_id_connections_connection_id_push_invoices_invoice_id_put(company_id, connection_id, invoice_id)

Posts an updated invoice to the accounting package for a given company.

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import invoices_api
from codat_python_sdk.model.codat_data_contracts_datasets_legacy_invoice import CodatDataContractsDatasetsLegacyInvoice
from codat_python_sdk.model.codat_data_contracts_datasets_legacy_invoice_push_operation import CodatDataContractsDatasetsLegacyInvoicePushOperation
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = codat_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: API Key Auth
configuration.api_key['API Key Auth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API Key Auth'] = 'Bearer'

# Configure OAuth2 access token for authorization: Codat Login
configuration = codat_python_sdk.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with codat_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = invoices_api.InvoicesApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    invoice_id = "invoiceId_example" # str | 
    timeout_in_minutes = 1 # int |  (optional)
    force_update = False # bool |  (optional) if omitted the server will use the default value of False
    codat_data_contracts_datasets_legacy_invoice = CodatDataContractsDatasetsLegacyInvoice(
        id="id_example",
        invoice_number="invoice_number_example",
        customer_ref=CodatDataContractsDatasetsCustomerRef(
            id="id_example",
            company_name="company_name_example",
        ),
        issue_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        due_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        source_modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        paid_on_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        currency="currency_example",
        currency_rate=3.14,
        line_items=[
            CodatDataContractsDatasetsInvoiceLineItem(
                description="description_example",
                unit_amount=3.14,
                quantity=3.14,
                discount_amount=3.14,
                sub_total=3.14,
                tax_amount=3.14,
                total_amount=3.14,
                account_ref=CodatDataContractsDatasetsAccountRef(
                    id="id_example",
                    name="name_example",
                ),
                discount_percentage=3.14,
                tax_rate_ref=CodatDataContractsDatasetsTaxRateRef(
                    id="id_example",
                    name="name_example",
                    effective_tax_rate=3.14,
                ),
                item_ref=CodatDataContractsDatasetsItemRef(
                    id="id_example",
                    name="name_example",
                ),
                tracking_category_refs=[
                    CodatDataContractsDatasetsTrackingCategoryRef(
                        id="id_example",
                        name="name_example",
                    ),
                ],
                tracking=CodatDataContractsDatasetsAccountsReceivableTracking(
                    category_refs=[
                        CodatDataContractsDatasetsTrackingCategoryRef(
                            id="id_example",
                            name="name_example",
                        ),
                    ],
                    project_ref=CodatDataContractsDatasetsProjectRef(
                        id="id_example",
                        name="name_example",
                    ),
                    customer_ref=CodatDataContractsDatasetsCustomerRef(
                        id="id_example",
                        company_name="company_name_example",
                    ),
                    is_billed_to=CodatDataContractsDatasetsAccountsReceivableIsBilledToType("Unknown"),
                    is_rebilled_to=CodatDataContractsDatasetsAccountsReceivableIsBilledToType("Unknown"),
                ),
            ),
        ],
        payment_allocations=[
            CodatDataContractsDatasetsLegacyInvoicePaymentAllocation(
                id="id_example",
                total_amount=3.14,
                currency="currency_example",
                currency_rate=3.14,
                date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                note="note_example",
                allocated_on_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                account_ref=CodatDataContractsDatasetsAccountRef(
                    id="id_example",
                    name="name_example",
                ),
                reference="reference_example",
            ),
        ],
        withholding_tax=[
            CodatDataContractsDatasetsWithholdingTax(
                name="name_example",
                amount=3.14,
            ),
        ],
        total_discount=3.14,
        sub_total=3.14,
        additional_tax_amount=3.14,
        additional_tax_percentage=3.14,
        total_tax_amount=3.14,
        total_amount=3.14,
        amount_due=3.14,
        discount_percentage=3.14,
        status=CodatDataContractsDatasetsInvoiceStatus("Unknown"),
        note="note_example",
    ) # CodatDataContractsDatasetsLegacyInvoice |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Posts an updated invoice to the accounting package for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_push_invoices_invoice_id_put(company_id, connection_id, invoice_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling InvoicesApi->companies_company_id_connections_connection_id_push_invoices_invoice_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Posts an updated invoice to the accounting package for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_push_invoices_invoice_id_put(company_id, connection_id, invoice_id, timeout_in_minutes=timeout_in_minutes, force_update=force_update, codat_data_contracts_datasets_legacy_invoice=codat_data_contracts_datasets_legacy_invoice)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling InvoicesApi->companies_company_id_connections_connection_id_push_invoices_invoice_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **invoice_id** | **str**|  |
 **timeout_in_minutes** | **int**|  | [optional]
 **force_update** | **bool**|  | [optional] if omitted the server will use the default value of False
 **codat_data_contracts_datasets_legacy_invoice** | [**CodatDataContractsDatasetsLegacyInvoice**](CodatDataContractsDatasetsLegacyInvoice.md)|  | [optional]

### Return type

[**CodatDataContractsDatasetsLegacyInvoicePushOperation**](CodatDataContractsDatasetsLegacyInvoicePushOperation.md)

### Authorization

[API Key Auth](../README.md#API Key Auth), [Codat Login](../README.md#Codat Login)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_push_invoices_post**
> CodatDataContractsDatasetsLegacyInvoicePushOperation companies_company_id_connections_connection_id_push_invoices_post(company_id, connection_id)

Posts a new invoice to the accounting package for a given company.

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import invoices_api
from codat_python_sdk.model.codat_data_contracts_datasets_legacy_invoice import CodatDataContractsDatasetsLegacyInvoice
from codat_python_sdk.model.codat_data_contracts_datasets_legacy_invoice_push_operation import CodatDataContractsDatasetsLegacyInvoicePushOperation
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = codat_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: API Key Auth
configuration.api_key['API Key Auth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API Key Auth'] = 'Bearer'

# Configure OAuth2 access token for authorization: Codat Login
configuration = codat_python_sdk.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with codat_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = invoices_api.InvoicesApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    timeout_in_minutes = 1 # int |  (optional)
    codat_data_contracts_datasets_legacy_invoice = CodatDataContractsDatasetsLegacyInvoice(
        id="id_example",
        invoice_number="invoice_number_example",
        customer_ref=CodatDataContractsDatasetsCustomerRef(
            id="id_example",
            company_name="company_name_example",
        ),
        issue_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        due_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        source_modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        paid_on_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        currency="currency_example",
        currency_rate=3.14,
        line_items=[
            CodatDataContractsDatasetsInvoiceLineItem(
                description="description_example",
                unit_amount=3.14,
                quantity=3.14,
                discount_amount=3.14,
                sub_total=3.14,
                tax_amount=3.14,
                total_amount=3.14,
                account_ref=CodatDataContractsDatasetsAccountRef(
                    id="id_example",
                    name="name_example",
                ),
                discount_percentage=3.14,
                tax_rate_ref=CodatDataContractsDatasetsTaxRateRef(
                    id="id_example",
                    name="name_example",
                    effective_tax_rate=3.14,
                ),
                item_ref=CodatDataContractsDatasetsItemRef(
                    id="id_example",
                    name="name_example",
                ),
                tracking_category_refs=[
                    CodatDataContractsDatasetsTrackingCategoryRef(
                        id="id_example",
                        name="name_example",
                    ),
                ],
                tracking=CodatDataContractsDatasetsAccountsReceivableTracking(
                    category_refs=[
                        CodatDataContractsDatasetsTrackingCategoryRef(
                            id="id_example",
                            name="name_example",
                        ),
                    ],
                    project_ref=CodatDataContractsDatasetsProjectRef(
                        id="id_example",
                        name="name_example",
                    ),
                    customer_ref=CodatDataContractsDatasetsCustomerRef(
                        id="id_example",
                        company_name="company_name_example",
                    ),
                    is_billed_to=CodatDataContractsDatasetsAccountsReceivableIsBilledToType("Unknown"),
                    is_rebilled_to=CodatDataContractsDatasetsAccountsReceivableIsBilledToType("Unknown"),
                ),
            ),
        ],
        payment_allocations=[
            CodatDataContractsDatasetsLegacyInvoicePaymentAllocation(
                id="id_example",
                total_amount=3.14,
                currency="currency_example",
                currency_rate=3.14,
                date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                note="note_example",
                allocated_on_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                account_ref=CodatDataContractsDatasetsAccountRef(
                    id="id_example",
                    name="name_example",
                ),
                reference="reference_example",
            ),
        ],
        withholding_tax=[
            CodatDataContractsDatasetsWithholdingTax(
                name="name_example",
                amount=3.14,
            ),
        ],
        total_discount=3.14,
        sub_total=3.14,
        additional_tax_amount=3.14,
        additional_tax_percentage=3.14,
        total_tax_amount=3.14,
        total_amount=3.14,
        amount_due=3.14,
        discount_percentage=3.14,
        status=CodatDataContractsDatasetsInvoiceStatus("Unknown"),
        note="note_example",
    ) # CodatDataContractsDatasetsLegacyInvoice |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Posts a new invoice to the accounting package for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_push_invoices_post(company_id, connection_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling InvoicesApi->companies_company_id_connections_connection_id_push_invoices_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Posts a new invoice to the accounting package for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_push_invoices_post(company_id, connection_id, timeout_in_minutes=timeout_in_minutes, codat_data_contracts_datasets_legacy_invoice=codat_data_contracts_datasets_legacy_invoice)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling InvoicesApi->companies_company_id_connections_connection_id_push_invoices_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **timeout_in_minutes** | **int**|  | [optional]
 **codat_data_contracts_datasets_legacy_invoice** | [**CodatDataContractsDatasetsLegacyInvoice**](CodatDataContractsDatasetsLegacyInvoice.md)|  | [optional]

### Return type

[**CodatDataContractsDatasetsLegacyInvoicePushOperation**](CodatDataContractsDatasetsLegacyInvoicePushOperation.md)

### Authorization

[API Key Auth](../README.md#API Key Auth), [Codat Login](../README.md#Codat Login)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_data_invoices_get**
> CodatDataContractsDatasetsLegacyInvoicePagedResponseModel companies_company_id_data_invoices_get(company_id, )

Gets the latest invoices for a company, with pagination

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import invoices_api
from codat_python_sdk.model.codat_data_contracts_datasets_legacy_invoice_paged_response_model import CodatDataContractsDatasetsLegacyInvoicePagedResponseModel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = codat_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: API Key Auth
configuration.api_key['API Key Auth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API Key Auth'] = 'Bearer'

# Configure OAuth2 access token for authorization: Codat Login
configuration = codat_python_sdk.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with codat_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = invoices_api.InvoicesApi(api_client)
    company_id = "companyId_example" # str | 
    page_size = 100 # int |  (optional) if omitted the server will use the default value of 100
    query = "query_example" # str |  (optional)
    order_by = "orderBy_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets the latest invoices for a company, with pagination
        api_response = api_instance.companies_company_id_data_invoices_get(company_id, )
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling InvoicesApi->companies_company_id_data_invoices_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets the latest invoices for a company, with pagination
        api_response = api_instance.companies_company_id_data_invoices_get(company_id, page_size=page_size, query=query, order_by=order_by)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling InvoicesApi->companies_company_id_data_invoices_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **page** | **int**|  | defaults to 1
 **page_size** | **int**|  | [optional] if omitted the server will use the default value of 100
 **query** | **str**|  | [optional]
 **order_by** | **str**|  | [optional]

### Return type

[**CodatDataContractsDatasetsLegacyInvoicePagedResponseModel**](CodatDataContractsDatasetsLegacyInvoicePagedResponseModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth), [Codat Login](../README.md#Codat Login)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_data_invoices_invoice_id_get**
> CodatDataContractsDatasetsLegacyInvoice companies_company_id_data_invoices_invoice_id_get(company_id, invoice_id)



### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import invoices_api
from codat_python_sdk.model.codat_data_contracts_datasets_legacy_invoice import CodatDataContractsDatasetsLegacyInvoice
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = codat_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: API Key Auth
configuration.api_key['API Key Auth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API Key Auth'] = 'Bearer'

# Configure OAuth2 access token for authorization: Codat Login
configuration = codat_python_sdk.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with codat_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = invoices_api.InvoicesApi(api_client)
    company_id = "companyId_example" # str | 
    invoice_id = "invoiceId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.companies_company_id_data_invoices_invoice_id_get(company_id, invoice_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling InvoicesApi->companies_company_id_data_invoices_invoice_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **invoice_id** | **str**|  |

### Return type

[**CodatDataContractsDatasetsLegacyInvoice**](CodatDataContractsDatasetsLegacyInvoice.md)

### Authorization

[API Key Auth](../README.md#API Key Auth), [Codat Login](../README.md#Codat Login)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_data_invoices_invoice_id_pdf_get**
> companies_company_id_data_invoices_invoice_id_pdf_get(company_id, invoice_id)



### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import invoices_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = codat_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: API Key Auth
configuration.api_key['API Key Auth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API Key Auth'] = 'Bearer'

# Configure OAuth2 access token for authorization: Codat Login
configuration = codat_python_sdk.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with codat_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = invoices_api.InvoicesApi(api_client)
    company_id = "companyId_example" # str | 
    invoice_id = "invoiceId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.companies_company_id_data_invoices_invoice_id_pdf_get(company_id, invoice_id)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling InvoicesApi->companies_company_id_data_invoices_invoice_id_pdf_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **invoice_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[API Key Auth](../README.md#API Key Auth), [Codat Login](../README.md#Codat Login)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


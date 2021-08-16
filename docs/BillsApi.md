# codat_python_sdk.BillsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_data_bills_bill_id_attachments_attachment_id_download_get**](BillsApi.md#companies_company_id_connections_connection_id_data_bills_bill_id_attachments_attachment_id_download_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/bills/{billId}/attachments/{attachmentId}/download | 
[**companies_company_id_connections_connection_id_data_bills_bill_id_attachments_attachment_id_get**](BillsApi.md#companies_company_id_connections_connection_id_data_bills_bill_id_attachments_attachment_id_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/bills/{billId}/attachments/{attachmentId} | 
[**companies_company_id_connections_connection_id_data_bills_bill_id_attachments_get**](BillsApi.md#companies_company_id_connections_connection_id_data_bills_bill_id_attachments_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/bills/{billId}/attachments | 
[**companies_company_id_connections_connection_id_push_bills_bill_id_attachments_post**](BillsApi.md#companies_company_id_connections_connection_id_push_bills_bill_id_attachments_post) | **POST** /companies/{companyId}/connections/{connectionId}/push/bills/{billId}/attachments | 
[**companies_company_id_connections_connection_id_push_bills_bill_id_put**](BillsApi.md#companies_company_id_connections_connection_id_push_bills_bill_id_put) | **PUT** /companies/{companyId}/connections/{connectionId}/push/bills/{billId} | Posts an updated bill to the accounting package for a given company.
[**companies_company_id_connections_connection_id_push_bills_post**](BillsApi.md#companies_company_id_connections_connection_id_push_bills_post) | **POST** /companies/{companyId}/connections/{connectionId}/push/bills | Posts a new bill to the accounting package for a given company.
[**companies_company_id_data_bills_bill_id_get**](BillsApi.md#companies_company_id_data_bills_bill_id_get) | **GET** /companies/{companyId}/data/bills/{billId} | 
[**companies_company_id_data_bills_get**](BillsApi.md#companies_company_id_data_bills_get) | **GET** /companies/{companyId}/data/bills | Gets the latest bills for a company, with pagination


# **companies_company_id_connections_connection_id_data_bills_bill_id_attachments_attachment_id_download_get**
> companies_company_id_connections_connection_id_data_bills_bill_id_attachments_attachment_id_download_get(company_id, connection_id, bill_id, attachment_id)



### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import bills_api
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

# Enter a context with an instance of the API client
with codat_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bills_api.BillsApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    bill_id = "billId_example" # str | 
    attachment_id = "attachmentId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.companies_company_id_connections_connection_id_data_bills_bill_id_attachments_attachment_id_download_get(company_id, connection_id, bill_id, attachment_id)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling BillsApi->companies_company_id_connections_connection_id_data_bills_bill_id_attachments_attachment_id_download_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **bill_id** | **str**|  |
 **attachment_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_data_bills_bill_id_attachments_attachment_id_get**
> CodatDataContractsDatasetsAttachmentsDatasetAttachment companies_company_id_connections_connection_id_data_bills_bill_id_attachments_attachment_id_get(company_id, connection_id, bill_id, attachment_id)



### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import bills_api
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

# Enter a context with an instance of the API client
with codat_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bills_api.BillsApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    bill_id = "billId_example" # str | 
    attachment_id = "attachmentId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.companies_company_id_connections_connection_id_data_bills_bill_id_attachments_attachment_id_get(company_id, connection_id, bill_id, attachment_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling BillsApi->companies_company_id_connections_connection_id_data_bills_bill_id_attachments_attachment_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **bill_id** | **str**|  |
 **attachment_id** | **str**|  |

### Return type

[**CodatDataContractsDatasetsAttachmentsDatasetAttachment**](CodatDataContractsDatasetsAttachmentsDatasetAttachment.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_data_bills_bill_id_attachments_get**
> CodatDataContractsDatasetsAttachmentsDataset companies_company_id_connections_connection_id_data_bills_bill_id_attachments_get(company_id, connection_id, bill_id)



### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import bills_api
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

# Enter a context with an instance of the API client
with codat_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bills_api.BillsApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    bill_id = "billId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.companies_company_id_connections_connection_id_data_bills_bill_id_attachments_get(company_id, connection_id, bill_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling BillsApi->companies_company_id_connections_connection_id_data_bills_bill_id_attachments_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **bill_id** | **str**|  |

### Return type

[**CodatDataContractsDatasetsAttachmentsDataset**](CodatDataContractsDatasetsAttachmentsDataset.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_push_bills_bill_id_attachments_post**
> companies_company_id_connections_connection_id_push_bills_bill_id_attachments_post(company_id, connection_id, bill_id)



### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import bills_api
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

# Enter a context with an instance of the API client
with codat_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bills_api.BillsApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    bill_id = "billId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.companies_company_id_connections_connection_id_push_bills_bill_id_attachments_post(company_id, connection_id, bill_id)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling BillsApi->companies_company_id_connections_connection_id_push_bills_bill_id_attachments_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **bill_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_push_bills_bill_id_put**
> CodatDataContractsDatasetsBillPushOperation companies_company_id_connections_connection_id_push_bills_bill_id_put(company_id, connection_id, bill_id)

Posts an updated bill to the accounting package for a given company.

### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import bills_api
from codat_python_sdk.model.codat_data_contracts_datasets_bill_push_operation import CodatDataContractsDatasetsBillPushOperation
from codat_python_sdk.model.codat_data_contracts_datasets_bill import CodatDataContractsDatasetsBill
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

# Enter a context with an instance of the API client
with codat_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bills_api.BillsApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    bill_id = "billId_example" # str | 
    timeout_in_minutes = 1 # int |  (optional)
    force_update = False # bool |  (optional) if omitted the server will use the default value of False
    codat_data_contracts_datasets_bill = CodatDataContractsDatasetsBill(
        id="id_example",
        reference="reference_example",
        supplier_ref=CodatDataContractsDatasetsSupplierRef(
            id="id_example",
            supplier_name="supplier_name_example",
        ),
        purchase_order_ref=CodatDataContractsDatasetsPurchaseOrderRef(
            id="id_example",
            purchase_order_number="purchase_order_number_example",
        ),
        purchase_order_refs=[
            CodatDataContractsDatasetsPurchaseOrderRef(
                id="id_example",
                purchase_order_number="purchase_order_number_example",
            ),
        ],
        issue_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        due_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        currency="currency_example",
        currency_rate=3.14,
        line_items=[
            CodatDataContractsDatasetsBillLineItem(
                description="description_example",
                unit_amount=3.14,
                quantity=3.14,
                discount_amount=3.14,
                sub_total=3.14,
                tax_amount=3.14,
                total_amount=3.14,
                discount_percentage=3.14,
                account_ref=CodatDataContractsDatasetsAccountRef(
                    id="id_example",
                    name="name_example",
                ),
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
                tracking=CodatDataContractsDatasetsAccountsPayableTracking(
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
                    is_billed_to=CodatDataContractsDatasetsAccountsPayableIsBilledToType("Unknown"),
                ),
                is_direct_cost=True,
            ),
        ],
        withholding_tax=[
            CodatDataContractsDatasetsWithholdingTax(
                name="name_example",
                amount=3.14,
            ),
        ],
        status=CodatDataContractsDatasetsBillStatus("Unknown"),
        sub_total=3.14,
        tax_amount=3.14,
        total_amount=3.14,
        amount_due=3.14,
        modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        source_modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        note="note_example",
        payment_allocations=[
            CodatDataContractsDatasetsDetailedPaymentAllocation(
                payment=CodatDataContractsDatasetsPaymentAllocationPayment(
                    id="id_example",
                    note="note_example",
                    reference="reference_example",
                    account_ref=CodatDataContractsDatasetsAccountRef(
                        id="id_example",
                        name="name_example",
                    ),
                    currency="currency_example",
                    currency_rate=3.14,
                    paid_on_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    total_amount=3.14,
                ),
                allocation=CodatDataContractsDatasetsAllocation(
                    currency="currency_example",
                    currency_rate=3.14,
                    allocated_on_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    total_amount=3.14,
                ),
            ),
        ],
    ) # CodatDataContractsDatasetsBill |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Posts an updated bill to the accounting package for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_push_bills_bill_id_put(company_id, connection_id, bill_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling BillsApi->companies_company_id_connections_connection_id_push_bills_bill_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Posts an updated bill to the accounting package for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_push_bills_bill_id_put(company_id, connection_id, bill_id, timeout_in_minutes=timeout_in_minutes, force_update=force_update, codat_data_contracts_datasets_bill=codat_data_contracts_datasets_bill)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling BillsApi->companies_company_id_connections_connection_id_push_bills_bill_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **bill_id** | **str**|  |
 **timeout_in_minutes** | **int**|  | [optional]
 **force_update** | **bool**|  | [optional] if omitted the server will use the default value of False
 **codat_data_contracts_datasets_bill** | [**CodatDataContractsDatasetsBill**](CodatDataContractsDatasetsBill.md)|  | [optional]

### Return type

[**CodatDataContractsDatasetsBillPushOperation**](CodatDataContractsDatasetsBillPushOperation.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_push_bills_post**
> CodatDataContractsDatasetsBillPushOperation companies_company_id_connections_connection_id_push_bills_post(company_id, connection_id)

Posts a new bill to the accounting package for a given company.

### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import bills_api
from codat_python_sdk.model.codat_data_contracts_datasets_bill_push_operation import CodatDataContractsDatasetsBillPushOperation
from codat_python_sdk.model.codat_data_contracts_datasets_bill import CodatDataContractsDatasetsBill
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

# Enter a context with an instance of the API client
with codat_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bills_api.BillsApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    timeout_in_minutes = 1 # int |  (optional)
    codat_data_contracts_datasets_bill = CodatDataContractsDatasetsBill(
        id="id_example",
        reference="reference_example",
        supplier_ref=CodatDataContractsDatasetsSupplierRef(
            id="id_example",
            supplier_name="supplier_name_example",
        ),
        purchase_order_ref=CodatDataContractsDatasetsPurchaseOrderRef(
            id="id_example",
            purchase_order_number="purchase_order_number_example",
        ),
        purchase_order_refs=[
            CodatDataContractsDatasetsPurchaseOrderRef(
                id="id_example",
                purchase_order_number="purchase_order_number_example",
            ),
        ],
        issue_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        due_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        currency="currency_example",
        currency_rate=3.14,
        line_items=[
            CodatDataContractsDatasetsBillLineItem(
                description="description_example",
                unit_amount=3.14,
                quantity=3.14,
                discount_amount=3.14,
                sub_total=3.14,
                tax_amount=3.14,
                total_amount=3.14,
                discount_percentage=3.14,
                account_ref=CodatDataContractsDatasetsAccountRef(
                    id="id_example",
                    name="name_example",
                ),
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
                tracking=CodatDataContractsDatasetsAccountsPayableTracking(
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
                    is_billed_to=CodatDataContractsDatasetsAccountsPayableIsBilledToType("Unknown"),
                ),
                is_direct_cost=True,
            ),
        ],
        withholding_tax=[
            CodatDataContractsDatasetsWithholdingTax(
                name="name_example",
                amount=3.14,
            ),
        ],
        status=CodatDataContractsDatasetsBillStatus("Unknown"),
        sub_total=3.14,
        tax_amount=3.14,
        total_amount=3.14,
        amount_due=3.14,
        modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        source_modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        note="note_example",
        payment_allocations=[
            CodatDataContractsDatasetsDetailedPaymentAllocation(
                payment=CodatDataContractsDatasetsPaymentAllocationPayment(
                    id="id_example",
                    note="note_example",
                    reference="reference_example",
                    account_ref=CodatDataContractsDatasetsAccountRef(
                        id="id_example",
                        name="name_example",
                    ),
                    currency="currency_example",
                    currency_rate=3.14,
                    paid_on_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    total_amount=3.14,
                ),
                allocation=CodatDataContractsDatasetsAllocation(
                    currency="currency_example",
                    currency_rate=3.14,
                    allocated_on_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    total_amount=3.14,
                ),
            ),
        ],
    ) # CodatDataContractsDatasetsBill |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Posts a new bill to the accounting package for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_push_bills_post(company_id, connection_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling BillsApi->companies_company_id_connections_connection_id_push_bills_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Posts a new bill to the accounting package for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_push_bills_post(company_id, connection_id, timeout_in_minutes=timeout_in_minutes, codat_data_contracts_datasets_bill=codat_data_contracts_datasets_bill)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling BillsApi->companies_company_id_connections_connection_id_push_bills_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **timeout_in_minutes** | **int**|  | [optional]
 **codat_data_contracts_datasets_bill** | [**CodatDataContractsDatasetsBill**](CodatDataContractsDatasetsBill.md)|  | [optional]

### Return type

[**CodatDataContractsDatasetsBillPushOperation**](CodatDataContractsDatasetsBillPushOperation.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_data_bills_bill_id_get**
> CodatDataContractsDatasetsBill companies_company_id_data_bills_bill_id_get(company_id, bill_id)



### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import bills_api
from codat_python_sdk.model.codat_data_contracts_datasets_bill import CodatDataContractsDatasetsBill
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

# Enter a context with an instance of the API client
with codat_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bills_api.BillsApi(api_client)
    company_id = "companyId_example" # str | 
    bill_id = "billId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.companies_company_id_data_bills_bill_id_get(company_id, bill_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling BillsApi->companies_company_id_data_bills_bill_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **bill_id** | **str**|  |

### Return type

[**CodatDataContractsDatasetsBill**](CodatDataContractsDatasetsBill.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_data_bills_get**
> CodatDataContractsDatasetsBillPagedResponseModel companies_company_id_data_bills_get(company_id, )

Gets the latest bills for a company, with pagination

### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import bills_api
from codat_python_sdk.model.codat_data_contracts_datasets_bill_paged_response_model import CodatDataContractsDatasetsBillPagedResponseModel
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

# Enter a context with an instance of the API client
with codat_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bills_api.BillsApi(api_client)
    company_id = "companyId_example" # str | 
    page_size = 100 # int |  (optional) if omitted the server will use the default value of 100
    query = "query_example" # str |  (optional)
    order_by = "orderBy_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets the latest bills for a company, with pagination
        api_response = api_instance.companies_company_id_data_bills_get(company_id, )
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling BillsApi->companies_company_id_data_bills_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets the latest bills for a company, with pagination
        api_response = api_instance.companies_company_id_data_bills_get(company_id, page_size=page_size, query=query, order_by=order_by)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling BillsApi->companies_company_id_data_bills_get: %s\n" % e)
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

[**CodatDataContractsDatasetsBillPagedResponseModel**](CodatDataContractsDatasetsBillPagedResponseModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


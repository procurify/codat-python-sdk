# codat_python_sdk.CreditNotesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_push_credit_notes_credit_note_id_put**](CreditNotesApi.md#companies_company_id_connections_connection_id_push_credit_notes_credit_note_id_put) | **PUT** /companies/{companyId}/connections/{connectionId}/push/creditNotes/{creditNoteId} | Posts an updated credit note to the accounting package for a given company.
[**companies_company_id_connections_connection_id_push_credit_notes_post**](CreditNotesApi.md#companies_company_id_connections_connection_id_push_credit_notes_post) | **POST** /companies/{companyId}/connections/{connectionId}/push/creditNotes | 
[**companies_company_id_data_credit_notes_credit_note_id_get**](CreditNotesApi.md#companies_company_id_data_credit_notes_credit_note_id_get) | **GET** /companies/{companyId}/data/creditNotes/{creditNoteId} | Gets a single creditNote corresponding to the supplied Id
[**companies_company_id_data_credit_notes_get**](CreditNotesApi.md#companies_company_id_data_credit_notes_get) | **GET** /companies/{companyId}/data/creditNotes | Gets a list of all credit notes for a company, with pagination


# **companies_company_id_connections_connection_id_push_credit_notes_credit_note_id_put**
> CodatDataContractsDatasetsLegacyCreditNotePushOperation companies_company_id_connections_connection_id_push_credit_notes_credit_note_id_put(company_id, connection_id, credit_note_id)

Posts an updated credit note to the accounting package for a given company.

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import credit_notes_api
from codat_python_sdk.model.codat_data_contracts_datasets_legacy_credit_note_push_operation import CodatDataContractsDatasetsLegacyCreditNotePushOperation
from codat_python_sdk.model.codat_data_contracts_datasets_legacy_credit_note import CodatDataContractsDatasetsLegacyCreditNote
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
    api_instance = credit_notes_api.CreditNotesApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    credit_note_id = "creditNoteId_example" # str | 
    timeout_in_minutes = 1 # int |  (optional)
    force_update = False # bool |  (optional) if omitted the server will use the default value of False
    codat_data_contracts_datasets_legacy_credit_note = CodatDataContractsDatasetsLegacyCreditNote(
        id="id_example",
        credit_note_number="credit_note_number_example",
        customer_ref=CodatDataContractsDatasetsCustomerRef(
            id="id_example",
            company_name="company_name_example",
        ),
        withholding_tax=[
            CodatDataContractsDatasetsWithholdingTax(
                name="name_example",
                amount=3.14,
            ),
        ],
        total_amount=3.14,
        total_discount=3.14,
        sub_total=3.14,
        additional_tax_amount=3.14,
        additional_tax_percentage=3.14,
        total_tax_amount=3.14,
        discount_percentage=3.14,
        remaining_credit=3.14,
        status=CodatDataContractsDatasetsCreditNoteStatus("Unknown"),
        issue_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        allocated_on_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        currency="currency_example",
        currency_rate=3.14,
        line_items=[
            CodatDataContractsDatasetsCreditNoteLineItem(
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
            CodatDataContractsDatasetsLegacyCreditNotePaymentAllocation(
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
        modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        source_modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        note="note_example",
    ) # CodatDataContractsDatasetsLegacyCreditNote |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Posts an updated credit note to the accounting package for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_push_credit_notes_credit_note_id_put(company_id, connection_id, credit_note_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling CreditNotesApi->companies_company_id_connections_connection_id_push_credit_notes_credit_note_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Posts an updated credit note to the accounting package for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_push_credit_notes_credit_note_id_put(company_id, connection_id, credit_note_id, timeout_in_minutes=timeout_in_minutes, force_update=force_update, codat_data_contracts_datasets_legacy_credit_note=codat_data_contracts_datasets_legacy_credit_note)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling CreditNotesApi->companies_company_id_connections_connection_id_push_credit_notes_credit_note_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **credit_note_id** | **str**|  |
 **timeout_in_minutes** | **int**|  | [optional]
 **force_update** | **bool**|  | [optional] if omitted the server will use the default value of False
 **codat_data_contracts_datasets_legacy_credit_note** | [**CodatDataContractsDatasetsLegacyCreditNote**](CodatDataContractsDatasetsLegacyCreditNote.md)|  | [optional]

### Return type

[**CodatDataContractsDatasetsLegacyCreditNotePushOperation**](CodatDataContractsDatasetsLegacyCreditNotePushOperation.md)

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

# **companies_company_id_connections_connection_id_push_credit_notes_post**
> CodatDataContractsDatasetsLegacyCreditNotePushOperation companies_company_id_connections_connection_id_push_credit_notes_post(company_id, connection_id)



### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import credit_notes_api
from codat_python_sdk.model.codat_data_contracts_datasets_legacy_credit_note_push_operation import CodatDataContractsDatasetsLegacyCreditNotePushOperation
from codat_python_sdk.model.codat_data_contracts_datasets_legacy_credit_note import CodatDataContractsDatasetsLegacyCreditNote
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
    api_instance = credit_notes_api.CreditNotesApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    timeout_in_minutes = 1 # int |  (optional)
    codat_data_contracts_datasets_legacy_credit_note = CodatDataContractsDatasetsLegacyCreditNote(
        id="id_example",
        credit_note_number="credit_note_number_example",
        customer_ref=CodatDataContractsDatasetsCustomerRef(
            id="id_example",
            company_name="company_name_example",
        ),
        withholding_tax=[
            CodatDataContractsDatasetsWithholdingTax(
                name="name_example",
                amount=3.14,
            ),
        ],
        total_amount=3.14,
        total_discount=3.14,
        sub_total=3.14,
        additional_tax_amount=3.14,
        additional_tax_percentage=3.14,
        total_tax_amount=3.14,
        discount_percentage=3.14,
        remaining_credit=3.14,
        status=CodatDataContractsDatasetsCreditNoteStatus("Unknown"),
        issue_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        allocated_on_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        currency="currency_example",
        currency_rate=3.14,
        line_items=[
            CodatDataContractsDatasetsCreditNoteLineItem(
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
            CodatDataContractsDatasetsLegacyCreditNotePaymentAllocation(
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
        modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        source_modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        note="note_example",
    ) # CodatDataContractsDatasetsLegacyCreditNote |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.companies_company_id_connections_connection_id_push_credit_notes_post(company_id, connection_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling CreditNotesApi->companies_company_id_connections_connection_id_push_credit_notes_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.companies_company_id_connections_connection_id_push_credit_notes_post(company_id, connection_id, timeout_in_minutes=timeout_in_minutes, codat_data_contracts_datasets_legacy_credit_note=codat_data_contracts_datasets_legacy_credit_note)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling CreditNotesApi->companies_company_id_connections_connection_id_push_credit_notes_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **timeout_in_minutes** | **int**|  | [optional]
 **codat_data_contracts_datasets_legacy_credit_note** | [**CodatDataContractsDatasetsLegacyCreditNote**](CodatDataContractsDatasetsLegacyCreditNote.md)|  | [optional]

### Return type

[**CodatDataContractsDatasetsLegacyCreditNotePushOperation**](CodatDataContractsDatasetsLegacyCreditNotePushOperation.md)

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

# **companies_company_id_data_credit_notes_credit_note_id_get**
> CodatDataContractsDatasetsLegacyCreditNote companies_company_id_data_credit_notes_credit_note_id_get(company_id, credit_note_id)

Gets a single creditNote corresponding to the supplied Id

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import credit_notes_api
from codat_python_sdk.model.codat_data_contracts_datasets_legacy_credit_note import CodatDataContractsDatasetsLegacyCreditNote
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
    api_instance = credit_notes_api.CreditNotesApi(api_client)
    company_id = "companyId_example" # str | 
    credit_note_id = "creditNoteId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Gets a single creditNote corresponding to the supplied Id
        api_response = api_instance.companies_company_id_data_credit_notes_credit_note_id_get(company_id, credit_note_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling CreditNotesApi->companies_company_id_data_credit_notes_credit_note_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **credit_note_id** | **str**|  |

### Return type

[**CodatDataContractsDatasetsLegacyCreditNote**](CodatDataContractsDatasetsLegacyCreditNote.md)

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

# **companies_company_id_data_credit_notes_get**
> CodatDataContractsDatasetsLegacyCreditNotePagedResponseModel companies_company_id_data_credit_notes_get(company_id, )

Gets a list of all credit notes for a company, with pagination

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import credit_notes_api
from codat_python_sdk.model.codat_data_contracts_datasets_legacy_credit_note_paged_response_model import CodatDataContractsDatasetsLegacyCreditNotePagedResponseModel
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
    api_instance = credit_notes_api.CreditNotesApi(api_client)
    company_id = "companyId_example" # str | 
    page_size = 100 # int |  (optional) if omitted the server will use the default value of 100
    query = "query_example" # str |  (optional)
    order_by = "orderBy_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets a list of all credit notes for a company, with pagination
        api_response = api_instance.companies_company_id_data_credit_notes_get(company_id, )
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling CreditNotesApi->companies_company_id_data_credit_notes_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets a list of all credit notes for a company, with pagination
        api_response = api_instance.companies_company_id_data_credit_notes_get(company_id, page_size=page_size, query=query, order_by=order_by)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling CreditNotesApi->companies_company_id_data_credit_notes_get: %s\n" % e)
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

[**CodatDataContractsDatasetsLegacyCreditNotePagedResponseModel**](CodatDataContractsDatasetsLegacyCreditNotePagedResponseModel.md)

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


# codat_python_sdk.JournalsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_push_journal_entries_post**](JournalsApi.md#companies_company_id_connections_connection_id_push_journal_entries_post) | **POST** /companies/{companyId}/connections/{connectionId}/push/journalEntries | Posts a new journalEntry to the accounting package for a given company.
[**companies_company_id_data_journal_entries_get**](JournalsApi.md#companies_company_id_data_journal_entries_get) | **GET** /companies/{companyId}/data/journalEntries | Gets the latest journal entries for a company, with pagination
[**companies_company_id_data_journal_entries_journal_entry_id_get**](JournalsApi.md#companies_company_id_data_journal_entries_journal_entry_id_get) | **GET** /companies/{companyId}/data/journalEntries/{journalEntryId} | Gets a single JournalEntry corresponding to the supplied Id


# **companies_company_id_connections_connection_id_push_journal_entries_post**
> CodatDataContractsDatasetsJournalEntryPushOperation companies_company_id_connections_connection_id_push_journal_entries_post(company_id, connection_id)

Posts a new journalEntry to the accounting package for a given company.

### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import journals_api
from codat_python_sdk.model.codat_data_contracts_datasets_journal_entry import CodatDataContractsDatasetsJournalEntry
from codat_python_sdk.model.codat_data_contracts_datasets_journal_entry_push_operation import CodatDataContractsDatasetsJournalEntryPushOperation
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
    api_instance = journals_api.JournalsApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    timeout_in_minutes = 1 # int |  (optional)
    codat_data_contracts_datasets_journal_entry = CodatDataContractsDatasetsJournalEntry(
        id="id_example",
        posted_on=dateutil_parser('1970-01-01T00:00:00.00Z'),
        created_on=dateutil_parser('1970-01-01T00:00:00.00Z'),
        updated_on=dateutil_parser('1970-01-01T00:00:00.00Z'),
        journal_lines=[
            CodatDataContractsDatasetsJournalLine(
                description="description_example",
                net_amount=3.14,
                currency="currency_example",
                account_ref=CodatDataContractsDatasetsAccountRef(
                    id="id_example",
                    name="name_example",
                ),
            ),
        ],
        modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        source_modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        record_ref=CodatDataContractsDatasetsRecordRef(
            id="id_example",
            data_type="data_type_example",
        ),
    ) # CodatDataContractsDatasetsJournalEntry |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Posts a new journalEntry to the accounting package for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_push_journal_entries_post(company_id, connection_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling JournalsApi->companies_company_id_connections_connection_id_push_journal_entries_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Posts a new journalEntry to the accounting package for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_push_journal_entries_post(company_id, connection_id, timeout_in_minutes=timeout_in_minutes, codat_data_contracts_datasets_journal_entry=codat_data_contracts_datasets_journal_entry)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling JournalsApi->companies_company_id_connections_connection_id_push_journal_entries_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **timeout_in_minutes** | **int**|  | [optional]
 **codat_data_contracts_datasets_journal_entry** | [**CodatDataContractsDatasetsJournalEntry**](CodatDataContractsDatasetsJournalEntry.md)|  | [optional]

### Return type

[**CodatDataContractsDatasetsJournalEntryPushOperation**](CodatDataContractsDatasetsJournalEntryPushOperation.md)

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

# **companies_company_id_data_journal_entries_get**
> CodatDataContractsDatasetsJournalEntryPagedResponseModel companies_company_id_data_journal_entries_get(company_id, )

Gets the latest journal entries for a company, with pagination

### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import journals_api
from codat_python_sdk.model.codat_data_contracts_datasets_journal_entry_paged_response_model import CodatDataContractsDatasetsJournalEntryPagedResponseModel
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
    api_instance = journals_api.JournalsApi(api_client)
    company_id = "companyId_example" # str | 
    page_size = 100 # int |  (optional) if omitted the server will use the default value of 100
    query = "query_example" # str |  (optional)
    order_by = "orderBy_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets the latest journal entries for a company, with pagination
        api_response = api_instance.companies_company_id_data_journal_entries_get(company_id, )
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling JournalsApi->companies_company_id_data_journal_entries_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets the latest journal entries for a company, with pagination
        api_response = api_instance.companies_company_id_data_journal_entries_get(company_id, page_size=page_size, query=query, order_by=order_by)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling JournalsApi->companies_company_id_data_journal_entries_get: %s\n" % e)
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

[**CodatDataContractsDatasetsJournalEntryPagedResponseModel**](CodatDataContractsDatasetsJournalEntryPagedResponseModel.md)

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

# **companies_company_id_data_journal_entries_journal_entry_id_get**
> CodatDataContractsDatasetsJournalEntry companies_company_id_data_journal_entries_journal_entry_id_get(company_id, journal_entry_id)

Gets a single JournalEntry corresponding to the supplied Id

### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import journals_api
from codat_python_sdk.model.codat_data_contracts_datasets_journal_entry import CodatDataContractsDatasetsJournalEntry
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
    api_instance = journals_api.JournalsApi(api_client)
    company_id = "companyId_example" # str | 
    journal_entry_id = "journalEntryId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Gets a single JournalEntry corresponding to the supplied Id
        api_response = api_instance.companies_company_id_data_journal_entries_journal_entry_id_get(company_id, journal_entry_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling JournalsApi->companies_company_id_data_journal_entries_journal_entry_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **journal_entry_id** | **str**|  |

### Return type

[**CodatDataContractsDatasetsJournalEntry**](CodatDataContractsDatasetsJournalEntry.md)

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


# codat_python_sdk.ItemsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_push_items_post**](ItemsApi.md#companies_company_id_connections_connection_id_push_items_post) | **POST** /companies/{companyId}/connections/{connectionId}/push/items | Posts a new item to the accounting package for a given company.
[**companies_company_id_data_items_get**](ItemsApi.md#companies_company_id_data_items_get) | **GET** /companies/{companyId}/data/items | Gets the items for a given company.
[**companies_company_id_data_items_item_id_get**](ItemsApi.md#companies_company_id_data_items_item_id_get) | **GET** /companies/{companyId}/data/items/{itemId} | Gets the specified item for a given company.


# **companies_company_id_connections_connection_id_push_items_post**
> CodatDataContractsDatasetsItemPushOperation companies_company_id_connections_connection_id_push_items_post(company_id, connection_id)

Posts a new item to the accounting package for a given company.

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import items_api
from codat_python_sdk.model.codat_data_contracts_datasets_item import CodatDataContractsDatasetsItem
from codat_python_sdk.model.codat_data_contracts_datasets_item_push_operation import CodatDataContractsDatasetsItemPushOperation
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
    api_instance = items_api.ItemsApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    timeout_in_minutes = 1 # int |  (optional)
    codat_data_contracts_datasets_item = CodatDataContractsDatasetsItem(
        id="id_example",
        name="name_example",
        code="code_example",
        modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        source_modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        item_status=CodatDataContractsDatasetsItemStatus("Unknown"),
        type=CodatDataContractsDatasetsItemType("Unknown"),
        is_bill_item=True,
        bill_item=CodatDataContractsDatasetsBillItem(
            description="description_example",
            unit_price=3.14,
            account_ref=CodatDataContractsDatasetsAccountRef(
                id="id_example",
                name="name_example",
            ),
            tax_rate_ref=CodatDataContractsDatasetsTaxRateRef(
                id="id_example",
                name="name_example",
                effective_tax_rate=3.14,
            ),
        ),
        is_invoice_item=True,
        invoice_item=CodatDataContractsDatasetsInvoiceItem(
            description="description_example",
            unit_price=3.14,
            account_ref=CodatDataContractsDatasetsAccountRef(
                id="id_example",
                name="name_example",
            ),
            tax_rate_ref=CodatDataContractsDatasetsTaxRateRef(
                id="id_example",
                name="name_example",
                effective_tax_rate=3.14,
            ),
        ),
    ) # CodatDataContractsDatasetsItem |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Posts a new item to the accounting package for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_push_items_post(company_id, connection_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling ItemsApi->companies_company_id_connections_connection_id_push_items_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Posts a new item to the accounting package for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_push_items_post(company_id, connection_id, timeout_in_minutes=timeout_in_minutes, codat_data_contracts_datasets_item=codat_data_contracts_datasets_item)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling ItemsApi->companies_company_id_connections_connection_id_push_items_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **timeout_in_minutes** | **int**|  | [optional]
 **codat_data_contracts_datasets_item** | [**CodatDataContractsDatasetsItem**](CodatDataContractsDatasetsItem.md)|  | [optional]

### Return type

[**CodatDataContractsDatasetsItemPushOperation**](CodatDataContractsDatasetsItemPushOperation.md)

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

# **companies_company_id_data_items_get**
> CodatDataContractsDatasetsItemPagedResponseModel companies_company_id_data_items_get(company_id, )

Gets the items for a given company.

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import items_api
from codat_python_sdk.model.codat_data_contracts_datasets_item_paged_response_model import CodatDataContractsDatasetsItemPagedResponseModel
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
    api_instance = items_api.ItemsApi(api_client)
    company_id = "companyId_example" # str | 
    page_size = 100 # int |  (optional) if omitted the server will use the default value of 100
    query = "query_example" # str |  (optional)
    order_by = "orderBy_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets the items for a given company.
        api_response = api_instance.companies_company_id_data_items_get(company_id, )
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling ItemsApi->companies_company_id_data_items_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets the items for a given company.
        api_response = api_instance.companies_company_id_data_items_get(company_id, page_size=page_size, query=query, order_by=order_by)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling ItemsApi->companies_company_id_data_items_get: %s\n" % e)
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

[**CodatDataContractsDatasetsItemPagedResponseModel**](CodatDataContractsDatasetsItemPagedResponseModel.md)

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

# **companies_company_id_data_items_item_id_get**
> CodatDataContractsDatasetsItem companies_company_id_data_items_item_id_get(company_id, item_id)

Gets the specified item for a given company.

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import items_api
from codat_python_sdk.model.codat_data_contracts_datasets_item import CodatDataContractsDatasetsItem
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
    api_instance = items_api.ItemsApi(api_client)
    company_id = "companyId_example" # str | 
    item_id = "itemId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Gets the specified item for a given company.
        api_response = api_instance.companies_company_id_data_items_item_id_get(company_id, item_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling ItemsApi->companies_company_id_data_items_item_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **item_id** | **str**|  |

### Return type

[**CodatDataContractsDatasetsItem**](CodatDataContractsDatasetsItem.md)

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


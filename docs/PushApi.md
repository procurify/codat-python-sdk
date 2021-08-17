# codat_python_sdk.PushApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_options_data_type_get**](PushApi.md#companies_company_id_connections_connection_id_options_data_type_get) | **GET** /companies/{companyId}/connections/{connectionId}/options/{dataType} | Gets the push options for the given data type
[**companies_company_id_push_get**](PushApi.md#companies_company_id_push_get) | **GET** /companies/{companyId}/push | Gets paged push operation records
[**companies_company_id_push_push_operation_key_get**](PushApi.md#companies_company_id_push_push_operation_key_get) | **GET** /companies/{companyId}/push/{pushOperationKey} | Gets a single push operation record


# **companies_company_id_connections_connection_id_options_data_type_get**
> CodatDataContractsPushPushOption companies_company_id_connections_connection_id_options_data_type_get(company_id, connection_id, data_type)

Gets the push options for the given data type

### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import push_api
from codat_python_sdk.model.codat_data_contracts_push_push_option import CodatDataContractsPushPushOption
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
    api_instance = push_api.PushApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    data_type = "dataType_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Gets the push options for the given data type
        api_response = api_instance.companies_company_id_connections_connection_id_options_data_type_get(company_id, connection_id, data_type)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling PushApi->companies_company_id_connections_connection_id_options_data_type_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **data_type** | **str**|  |

### Return type

[**CodatDataContractsPushPushOption**](CodatDataContractsPushPushOption.md)

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

# **companies_company_id_push_get**
> SystemObjectPushOperationPagedResponseModel companies_company_id_push_get(company_id, page)

Gets paged push operation records

### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import push_api
from codat_python_sdk.model.system_object_push_operation_paged_response_model import SystemObjectPushOperationPagedResponseModel
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
    api_instance = push_api.PushApi(api_client)
    company_id = "companyId_example" # str | Company Id
    page = 1 # int | Page
    page_size = 100 # int | Page size (optional) if omitted the server will use the default value of 100
    query = "query_example" # str | Data query (optional)
    order_by = "orderBy_example" # str | Order by property (ascending) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets paged push operation records
        api_response = api_instance.companies_company_id_push_get(company_id, page)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling PushApi->companies_company_id_push_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets paged push operation records
        api_response = api_instance.companies_company_id_push_get(company_id, page, page_size=page_size, query=query, order_by=order_by)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling PushApi->companies_company_id_push_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| Company Id |
 **page** | **int**| Page |
 **page_size** | **int**| Page size | [optional] if omitted the server will use the default value of 100
 **query** | **str**| Data query | [optional]
 **order_by** | **str**| Order by property (ascending) | [optional]

### Return type

[**SystemObjectPushOperationPagedResponseModel**](SystemObjectPushOperationPagedResponseModel.md)

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

# **companies_company_id_push_push_operation_key_get**
> SystemObjectPushOperation companies_company_id_push_push_operation_key_get(company_id, push_operation_key)

Gets a single push operation record

### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import push_api
from codat_python_sdk.model.system_object_push_operation import SystemObjectPushOperation
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
    api_instance = push_api.PushApi(api_client)
    company_id = "companyId_example" # str | 
    push_operation_key = "pushOperationKey_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Gets a single push operation record
        api_response = api_instance.companies_company_id_push_push_operation_key_get(company_id, push_operation_key)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling PushApi->companies_company_id_push_push_operation_key_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **push_operation_key** | **str**|  |

### Return type

[**SystemObjectPushOperation**](SystemObjectPushOperation.md)

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


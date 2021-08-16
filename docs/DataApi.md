# codat_python_sdk.DataApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_data_all_post**](DataApi.md#companies_company_id_data_all_post) | **POST** /companies/{companyId}/data/all | Initiates the process of capturing a new data snapshot for a company
[**companies_company_id_data_history_dataset_id_get**](DataApi.md#companies_company_id_data_history_dataset_id_get) | **GET** /companies/{companyId}/data/history/{datasetId} | Fetch metadata on a single data synchronisation
[**companies_company_id_data_history_get**](DataApi.md#companies_company_id_data_history_get) | **GET** /companies/{companyId}/data/history | Fetch a list of all data snapshots captured for a company
[**companies_company_id_data_queue_data_type_post**](DataApi.md#companies_company_id_data_queue_data_type_post) | **POST** /companies/{companyId}/data/queue/{dataType} | Initiates the process of capturing a data snapshot of a specified type for a company


# **companies_company_id_data_all_post**
> companies_company_id_data_all_post(company_id)

Initiates the process of capturing a new data snapshot for a company

Initiates the synchronisation for all possible data types supported by the linked data sources

### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import data_api
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
    api_instance = data_api.DataApi(api_client)
    company_id = "companyId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Initiates the process of capturing a new data snapshot for a company
        api_instance.companies_company_id_data_all_post(company_id)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling DataApi->companies_company_id_data_all_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |

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

# **companies_company_id_data_history_dataset_id_get**
> CodatPublicApiModelsDataDataSet companies_company_id_data_history_dataset_id_get(company_id, dataset_id)

Fetch metadata on a single data synchronisation

### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import data_api
from codat_python_sdk.model.codat_public_api_models_data_data_set import CodatPublicApiModelsDataDataSet
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
    api_instance = data_api.DataApi(api_client)
    company_id = "companyId_example" # str | 
    dataset_id = "datasetId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch metadata on a single data synchronisation
        api_response = api_instance.companies_company_id_data_history_dataset_id_get(company_id, dataset_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling DataApi->companies_company_id_data_history_dataset_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **dataset_id** | **str**|  |

### Return type

[**CodatPublicApiModelsDataDataSet**](CodatPublicApiModelsDataDataSet.md)

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

# **companies_company_id_data_history_get**
> CodatPublicApiModelsDataDataSetPagedResponseModel companies_company_id_data_history_get(company_id, )

Fetch a list of all data snapshots captured for a company

### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import data_api
from codat_python_sdk.model.codat_public_api_models_data_data_set_paged_response_model import CodatPublicApiModelsDataDataSetPagedResponseModel
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
    api_instance = data_api.DataApi(api_client)
    company_id = "companyId_example" # str | 
    page_size = 100 # int |  (optional) if omitted the server will use the default value of 100
    query = "query_example" # str |  (optional)
    order_by = "orderBy_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Fetch a list of all data snapshots captured for a company
        api_response = api_instance.companies_company_id_data_history_get(company_id, )
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling DataApi->companies_company_id_data_history_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch a list of all data snapshots captured for a company
        api_response = api_instance.companies_company_id_data_history_get(company_id, page_size=page_size, query=query, order_by=order_by)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling DataApi->companies_company_id_data_history_get: %s\n" % e)
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

[**CodatPublicApiModelsDataDataSetPagedResponseModel**](CodatPublicApiModelsDataDataSetPagedResponseModel.md)

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

# **companies_company_id_data_queue_data_type_post**
> CodatPublicApiModelsDataDataSet companies_company_id_data_queue_data_type_post(company_id, data_type)

Initiates the process of capturing a data snapshot of a specified type for a company

Initiates the synchronisation for a specified data type

### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import data_api
from codat_python_sdk.model.codat_public_api_models_data_data_set import CodatPublicApiModelsDataDataSet
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
    api_instance = data_api.DataApi(api_client)
    company_id = "companyId_example" # str | 
    data_type = "dataType_example" # str | 
    connection_id = "connectionId_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Initiates the process of capturing a data snapshot of a specified type for a company
        api_response = api_instance.companies_company_id_data_queue_data_type_post(company_id, data_type)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling DataApi->companies_company_id_data_queue_data_type_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Initiates the process of capturing a data snapshot of a specified type for a company
        api_response = api_instance.companies_company_id_data_queue_data_type_post(company_id, data_type, connection_id=connection_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling DataApi->companies_company_id_data_queue_data_type_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **data_type** | **str**|  |
 **connection_id** | **str**|  | [optional]

### Return type

[**CodatPublicApiModelsDataDataSet**](CodatPublicApiModelsDataDataSet.md)

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


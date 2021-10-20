# codat_python_sdk.DataTypesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_data_types_data_type_options_get**](DataTypesApi.md#companies_company_id_connections_connection_id_data_types_data_type_options_get) | **GET** /companies/{companyId}/connections/{connectionId}/dataTypes/{dataType}/options | Gets all available push options for the given data type
[**companies_company_id_connections_connection_id_data_types_data_type_options_post_get**](DataTypesApi.md#companies_company_id_connections_connection_id_data_types_data_type_options_post_get) | **GET** /companies/{companyId}/connections/{connectionId}/dataTypes/{dataType}/options/POST | Gets the POST push options for the given data type
[**companies_company_id_connections_connection_id_data_types_data_type_options_put_get**](DataTypesApi.md#companies_company_id_connections_connection_id_data_types_data_type_options_put_get) | **GET** /companies/{companyId}/connections/{connectionId}/dataTypes/{dataType}/options/PUT | Gets the PUT push options for the given data type


# **companies_company_id_connections_connection_id_data_types_data_type_options_get**
> CodatPublicApiModelsDataPushOptionsAggregate companies_company_id_connections_connection_id_data_types_data_type_options_get(company_id, connection_id, data_type)

Gets all available push options for the given data type

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import data_types_api
from codat_python_sdk.model.codat_public_api_models_data_push_options_aggregate import CodatPublicApiModelsDataPushOptionsAggregate
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
    api_instance = data_types_api.DataTypesApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    data_type = "dataType_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Gets all available push options for the given data type
        api_response = api_instance.companies_company_id_connections_connection_id_data_types_data_type_options_get(company_id, connection_id, data_type)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling DataTypesApi->companies_company_id_connections_connection_id_data_types_data_type_options_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **data_type** | **str**|  |

### Return type

[**CodatPublicApiModelsDataPushOptionsAggregate**](CodatPublicApiModelsDataPushOptionsAggregate.md)

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

# **companies_company_id_connections_connection_id_data_types_data_type_options_post_get**
> CodatDataContractsPushPushOption companies_company_id_connections_connection_id_data_types_data_type_options_post_get(company_id, connection_id, data_type)

Gets the POST push options for the given data type

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import data_types_api
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

# Configure OAuth2 access token for authorization: Codat Login
configuration = codat_python_sdk.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with codat_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_types_api.DataTypesApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    data_type = "dataType_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Gets the POST push options for the given data type
        api_response = api_instance.companies_company_id_connections_connection_id_data_types_data_type_options_post_get(company_id, connection_id, data_type)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling DataTypesApi->companies_company_id_connections_connection_id_data_types_data_type_options_post_get: %s\n" % e)
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

[API Key Auth](../README.md#API Key Auth), [Codat Login](../README.md#Codat Login)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_data_types_data_type_options_put_get**
> CodatDataContractsPushPushOption companies_company_id_connections_connection_id_data_types_data_type_options_put_get(company_id, connection_id, data_type)

Gets the PUT push options for the given data type

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import data_types_api
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

# Configure OAuth2 access token for authorization: Codat Login
configuration = codat_python_sdk.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with codat_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_types_api.DataTypesApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    data_type = "dataType_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Gets the PUT push options for the given data type
        api_response = api_instance.companies_company_id_connections_connection_id_data_types_data_type_options_put_get(company_id, connection_id, data_type)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling DataTypesApi->companies_company_id_connections_connection_id_data_types_data_type_options_put_get: %s\n" % e)
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

[API Key Auth](../README.md#API Key Auth), [Codat Login](../README.md#Codat Login)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


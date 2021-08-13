# codat_python_sdk.DataTypesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_data_types_data_type_options_get**](DataTypesApi.md#companies_company_id_connections_connection_id_data_types_data_type_options_get) | **GET** /companies/{companyId}/connections/{connectionId}/dataTypes/{dataType}/options | Gets all available push options for the given data type
[**companies_company_id_connections_connection_id_data_types_data_type_options_post_get**](DataTypesApi.md#companies_company_id_connections_connection_id_data_types_data_type_options_post_get) | **GET** /companies/{companyId}/connections/{connectionId}/dataTypes/{dataType}/options/POST | Gets the POST push options for the given data type
[**companies_company_id_connections_connection_id_data_types_data_type_options_put_get**](DataTypesApi.md#companies_company_id_connections_connection_id_data_types_data_type_options_put_get) | **GET** /companies/{companyId}/connections/{connectionId}/dataTypes/{dataType}/options/PUT | Gets the PUT push options for the given data type

# **companies_company_id_connections_connection_id_data_types_data_type_options_get**
> CodatPublicApiModelsDataPushOptionsAggregate companies_company_id_connections_connection_id_data_types_data_type_options_get(company_id, connection_id, data_type)

Gets all available push options for the given data type

### Example
```python
from __future__ import print_function
import time
import codat_python_sdk
from codat_python_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key Auth
configuration = codat_python_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = codat_python_sdk.DataTypesApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
data_type = 'data_type_example' # str | 

try:
    # Gets all available push options for the given data type
    api_response = api_instance.companies_company_id_connections_connection_id_data_types_data_type_options_get(company_id, connection_id, data_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTypesApi->companies_company_id_connections_connection_id_data_types_data_type_options_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **data_type** | **str**|  | 

### Return type

[**CodatPublicApiModelsDataPushOptionsAggregate**](CodatPublicApiModelsDataPushOptionsAggregate.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_data_types_data_type_options_post_get**
> CodatDataContractsPushPushOption companies_company_id_connections_connection_id_data_types_data_type_options_post_get(company_id, connection_id, data_type)

Gets the POST push options for the given data type

### Example
```python
from __future__ import print_function
import time
import codat_python_sdk
from codat_python_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key Auth
configuration = codat_python_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = codat_python_sdk.DataTypesApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
data_type = 'data_type_example' # str | 

try:
    # Gets the POST push options for the given data type
    api_response = api_instance.companies_company_id_connections_connection_id_data_types_data_type_options_post_get(company_id, connection_id, data_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTypesApi->companies_company_id_connections_connection_id_data_types_data_type_options_post_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **data_type** | **str**|  | 

### Return type

[**CodatDataContractsPushPushOption**](CodatDataContractsPushPushOption.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_data_types_data_type_options_put_get**
> CodatDataContractsPushPushOption companies_company_id_connections_connection_id_data_types_data_type_options_put_get(company_id, connection_id, data_type)

Gets the PUT push options for the given data type

### Example
```python
from __future__ import print_function
import time
import codat_python_sdk
from codat_python_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key Auth
configuration = codat_python_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = codat_python_sdk.DataTypesApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
data_type = 'data_type_example' # str | 

try:
    # Gets the PUT push options for the given data type
    api_response = api_instance.companies_company_id_connections_connection_id_data_types_data_type_options_put_get(company_id, connection_id, data_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTypesApi->companies_company_id_connections_connection_id_data_types_data_type_options_put_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **data_type** | **str**|  | 

### Return type

[**CodatDataContractsPushPushOption**](CodatDataContractsPushPushOption.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# codat_python_sdk.PushApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_options_data_type_get**](PushApi.md#companies_company_id_connections_connection_id_options_data_type_get) | **GET** /companies/{companyId}/connections/{connectionId}/options/{dataType} | Gets the push options for the given data type
[**companies_company_id_push_get**](PushApi.md#companies_company_id_push_get) | **GET** /companies/{companyId}/push | Gets paged push operation records
[**companies_company_id_push_push_operation_key_get**](PushApi.md#companies_company_id_push_push_operation_key_get) | **GET** /companies/{companyId}/push/{pushOperationKey} | Gets a single push operation record

# **companies_company_id_connections_connection_id_options_data_type_get**
> CodatDataContractsPushPushOption companies_company_id_connections_connection_id_options_data_type_get(company_id, connection_id, data_type)

Gets the push options for the given data type

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
api_instance = codat_python_sdk.PushApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
data_type = 'data_type_example' # str | 

try:
    # Gets the push options for the given data type
    api_response = api_instance.companies_company_id_connections_connection_id_options_data_type_get(company_id, connection_id, data_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PushApi->companies_company_id_connections_connection_id_options_data_type_get: %s\n" % e)
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

# **companies_company_id_push_get**
> SystemObjectPushOperationPagedResponseModel companies_company_id_push_get(company_id, page, page_size=page_size, query=query, order_by=order_by)

Gets paged push operation records

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
api_instance = codat_python_sdk.PushApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Company Id
page = 56 # int | Page
page_size = 100 # int | Page size (optional) (default to 100)
query = 'query_example' # str | Data query (optional)
order_by = 'order_by_example' # str | Order by property (ascending) (optional)

try:
    # Gets paged push operation records
    api_response = api_instance.companies_company_id_push_get(company_id, page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PushApi->companies_company_id_push_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)| Company Id | 
 **page** | **int**| Page | 
 **page_size** | **int**| Page size | [optional] [default to 100]
 **query** | **str**| Data query | [optional] 
 **order_by** | **str**| Order by property (ascending) | [optional] 

### Return type

[**SystemObjectPushOperationPagedResponseModel**](SystemObjectPushOperationPagedResponseModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_push_push_operation_key_get**
> SystemObjectPushOperation companies_company_id_push_push_operation_key_get(company_id, push_operation_key)

Gets a single push operation record

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
api_instance = codat_python_sdk.PushApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
push_operation_key = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Gets a single push operation record
    api_response = api_instance.companies_company_id_push_push_operation_key_get(company_id, push_operation_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PushApi->companies_company_id_push_push_operation_key_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **push_operation_key** | [**str**](.md)|  | 

### Return type

[**SystemObjectPushOperation**](SystemObjectPushOperation.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


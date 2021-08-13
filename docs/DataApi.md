# codat_python_sdk.DataApi

All URIs are relative to */*

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
api_instance = codat_python_sdk.DataApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Initiates the process of capturing a new data snapshot for a company
    api_instance.companies_company_id_data_all_post(company_id)
except ApiException as e:
    print("Exception when calling DataApi->companies_company_id_data_all_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_data_history_dataset_id_get**
> CodatPublicApiModelsDataDataSet companies_company_id_data_history_dataset_id_get(company_id, dataset_id)

Fetch metadata on a single data synchronisation

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
api_instance = codat_python_sdk.DataApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
dataset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Fetch metadata on a single data synchronisation
    api_response = api_instance.companies_company_id_data_history_dataset_id_get(company_id, dataset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->companies_company_id_data_history_dataset_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **dataset_id** | [**str**](.md)|  | 

### Return type

[**CodatPublicApiModelsDataDataSet**](CodatPublicApiModelsDataDataSet.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_data_history_get**
> CodatPublicApiModelsDataDataSetPagedResponseModel companies_company_id_data_history_get(company_id, page, page_size=page_size, query=query, order_by=order_by)

Fetch a list of all data snapshots captured for a company

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
api_instance = codat_python_sdk.DataApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
page = 1 # int |  (default to 1)
page_size = 100 # int |  (optional) (default to 100)
query = 'query_example' # str |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Fetch a list of all data snapshots captured for a company
    api_response = api_instance.companies_company_id_data_history_get(company_id, page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->companies_company_id_data_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **page** | **int**|  | [default to 1]
 **page_size** | **int**|  | [optional] [default to 100]
 **query** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**CodatPublicApiModelsDataDataSetPagedResponseModel**](CodatPublicApiModelsDataDataSetPagedResponseModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_data_queue_data_type_post**
> CodatPublicApiModelsDataDataSet companies_company_id_data_queue_data_type_post(company_id, data_type, connection_id=connection_id)

Initiates the process of capturing a data snapshot of a specified type for a company

Initiates the synchronisation for a specified data type

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
api_instance = codat_python_sdk.DataApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
data_type = 'data_type_example' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)

try:
    # Initiates the process of capturing a data snapshot of a specified type for a company
    api_response = api_instance.companies_company_id_data_queue_data_type_post(company_id, data_type, connection_id=connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->companies_company_id_data_queue_data_type_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **data_type** | **str**|  | 
 **connection_id** | [**str**](.md)|  | [optional] 

### Return type

[**CodatPublicApiModelsDataDataSet**](CodatPublicApiModelsDataDataSet.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


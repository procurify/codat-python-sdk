# codat_python_sdk.DirectCostsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_data_direct_costs_direct_cost_id_get**](DirectCostsApi.md#companies_company_id_connections_connection_id_data_direct_costs_direct_cost_id_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/directCosts/{directCostId} | Gets the specified direct cost for a given company.
[**companies_company_id_connections_connection_id_data_direct_costs_get**](DirectCostsApi.md#companies_company_id_connections_connection_id_data_direct_costs_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/directCosts | Gets the direct costs for the company.
[**companies_company_id_connections_connection_id_push_direct_costs_post**](DirectCostsApi.md#companies_company_id_connections_connection_id_push_direct_costs_post) | **POST** /companies/{companyId}/connections/{connectionId}/push/directCosts | Posts a new direct cost to the accounting package for a given company.

# **companies_company_id_connections_connection_id_data_direct_costs_direct_cost_id_get**
> CodatDataContractsDatasetsDirectCost companies_company_id_connections_connection_id_data_direct_costs_direct_cost_id_get(company_id, direct_cost_id, connection_id)

Gets the specified direct cost for a given company.

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
api_instance = codat_python_sdk.DirectCostsApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
direct_cost_id = 'direct_cost_id_example' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Gets the specified direct cost for a given company.
    api_response = api_instance.companies_company_id_connections_connection_id_data_direct_costs_direct_cost_id_get(company_id, direct_cost_id, connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectCostsApi->companies_company_id_connections_connection_id_data_direct_costs_direct_cost_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **direct_cost_id** | **str**|  | 
 **connection_id** | [**str**](.md)|  | 

### Return type

[**CodatDataContractsDatasetsDirectCost**](CodatDataContractsDatasetsDirectCost.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_data_direct_costs_get**
> CodatDataContractsDatasetsDirectCostPagedResponseModel companies_company_id_connections_connection_id_data_direct_costs_get(company_id, connection_id, page, page_size=page_size, query=query, order_by=order_by)

Gets the direct costs for the company.

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
api_instance = codat_python_sdk.DirectCostsApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
page = 1 # int |  (default to 1)
page_size = 100 # int |  (optional) (default to 100)
query = 'query_example' # str |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Gets the direct costs for the company.
    api_response = api_instance.companies_company_id_connections_connection_id_data_direct_costs_get(company_id, connection_id, page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectCostsApi->companies_company_id_connections_connection_id_data_direct_costs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **page** | **int**|  | [default to 1]
 **page_size** | **int**|  | [optional] [default to 100]
 **query** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**CodatDataContractsDatasetsDirectCostPagedResponseModel**](CodatDataContractsDatasetsDirectCostPagedResponseModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_push_direct_costs_post**
> CodatDataContractsDatasetsDirectCostPushOperation companies_company_id_connections_connection_id_push_direct_costs_post(company_id, connection_id, body=body, timeout_in_minutes=timeout_in_minutes)

Posts a new direct cost to the accounting package for a given company.

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
api_instance = codat_python_sdk.DirectCostsApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = codat_python_sdk.CodatDataContractsDatasetsDirectCost() # CodatDataContractsDatasetsDirectCost |  (optional)
timeout_in_minutes = 56 # int |  (optional)

try:
    # Posts a new direct cost to the accounting package for a given company.
    api_response = api_instance.companies_company_id_connections_connection_id_push_direct_costs_post(company_id, connection_id, body=body, timeout_in_minutes=timeout_in_minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectCostsApi->companies_company_id_connections_connection_id_push_direct_costs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **body** | [**CodatDataContractsDatasetsDirectCost**](CodatDataContractsDatasetsDirectCost.md)|  | [optional] 
 **timeout_in_minutes** | **int**|  | [optional] 

### Return type

[**CodatDataContractsDatasetsDirectCostPushOperation**](CodatDataContractsDatasetsDirectCostPushOperation.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

